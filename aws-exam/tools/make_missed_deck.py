#!/usr/bin/env python3
"""Build an Anki deck from the questions you actually got wrong.

Reads graded answer files, finds every question in a chosen CLF-C02 domain that
was answered incorrectly, and makes one card per question:

    Front  the question stem, with its options unless --no-options is given
    Back   the correct answer, and nothing else

Notes are keyed by the source question rather than by the rendered card, so
switching between the two front formats updates the existing cards in Anki
instead of duplicating them.

Unlike the review-packet decks this one quotes the source corpus verbatim, so
the generated .apkg is personal study material and is not committed here.

Usage:
    python3 make_missed_deck.py --domain 2 --answers ~/answers/*.txt -o ~/decks
    python3 make_missed_deck.py --domain 2 --no-options --answers ~/answers/*.txt

Each answer file must be named so the exam number can be read out of it, e.g.
exam17-answers.txt, and contain answers in any format practice.py accepts.
"""

import argparse
import html
import re
import sys
from pathlib import Path

import genanki

sys.path.insert(0, str(Path(__file__).parent))
from parse_practice_exams import parse_file  # noqa: E402
from practice import parse_answers, default_dir, DOMAIN_NAMES  # noqa: E402

MODEL_ID = 1607392320
DECK_ID_BASE = 2059400200  # + domain id

MODEL = genanki.Model(
    MODEL_ID,
    "CLF-C02 Missed Question",
    fields=[{"name": "Question"}, {"name": "Answer"}, {"name": "Source"}],
    templates=[{
        "name": "Recall",
        "qfmt": '<div class="q">{{Question}}</div>',
        "afmt": '<div class="q">{{Question}}</div><hr id="answer">'
                '<div class="a">{{Answer}}</div>'
                '<div class="src">{{Source}}</div>',
    }],
    css="""
.card {
  font-family: -apple-system, "Segoe UI", Roboto, sans-serif;
  font-size: 18px; text-align: left; line-height: 1.5;
  color: #182430; background: #ffffff; padding: 18px 20px;
}
.q { font-size: 18px; }
.q .stem { margin-bottom: 12px; }
.q .opt { margin: 4px 0 4px 4px; color: #445260; }
.q .two { display: inline-block; font-size: 12px; letter-spacing: .08em;
  text-transform: uppercase; color: #b85c0c; border: 1px solid #b85c0c;
  border-radius: 3px; padding: 1px 6px; margin-left: 6px; }
.a { font-size: 20px; font-weight: 600; color: #b85c0c; }
.a div { margin: 3px 0; }
.src { font-size: 13px; color: #6b7a88; margin-top: 14px; }
hr#answer { border: 0; border-top: 1px solid #dce2e8; margin: 16px 0; }
.nightMode .card { color: #e6edf3; background: #18202a; }
.nightMode .q .opt { color: #a9b7c4; }
.nightMode .a { color: #e08b3e; }
.nightMode .q .two { color: #e08b3e; border-color: #e08b3e; }
.nightMode .src { color: #7d8c9a; }
.nightMode hr#answer { border-top-color: #2b3742; }
""",
)


def clean(text):
    """Collapse the corpus's inline <br/> markup and whitespace."""
    return re.sub(r"\s+", " ", re.sub(r"<br\s*/?>", " ", text)).strip()


def build_front(q, with_options=True):
    stem = html.escape(clean(re.sub(r"\(?(choose|select) two\.?\)?", "", q["stem"], flags=re.I)))
    tag = '<span class="two">Choose two</span>' if q["type"] == "multi" else ""
    front = f'<div class="stem">{stem}{tag}</div>'
    if not with_options:
        return front
    return front + "".join(
        f'<div class="opt">{letter}. {html.escape(clean(text))}</div>'
        for letter, text in sorted(q["options"].items())
    )


def build_back(q, with_letters=True):
    return "".join(
        f'<div>{letter + ". " if with_letters else ""}'
        f'{html.escape(clean(q["options"][letter]))}</div>'
        for letter in sorted(q["answers"]) if letter in q["options"]
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domain", type=int, default=2, help="CLF-C02 domain id (default 2)")
    ap.add_argument("--answers", nargs="+", required=True, help="graded answer files")
    ap.add_argument("--repo", default=default_dir(), help="the practice-exam folder")
    ap.add_argument("-o", "--out", default=".")
    ap.add_argument("--no-options", action="store_true",
                    help="put only the question on the front (free recall)")
    args = ap.parse_args()

    cards, seen = [], set()
    for path in sorted(args.answers):
        match = re.search(r"(\d+)", Path(path).name)
        if not match:
            print(f"skipping {path}: no exam number in the filename", file=sys.stderr)
            continue
        number = int(match.group(1))
        questions, _ = parse_file(Path(args.repo) / f"practice-exam-{number}.md")
        submitted = parse_answers(Path(path).read_text())

        for q in questions:
            if q["domain"] != args.domain or not q["options"] or not q["answers"]:
                continue
            given = submitted.get(q["number"], [])
            if not given or given == sorted(q["answers"]):
                continue  # unanswered questions were never really attempted
            key = clean(q["stem"]).lower()
            if key in seen:
                continue  # the corpus repeats questions across exams
            seen.add(key)
            cards.append((
                build_front(q, with_options=not args.no_options),
                build_back(q, with_letters=not args.no_options),
                f"Practice exam {number}, Q{q['number']} &middot; {q['topic']}",
                # Identity is the source question, not the rendered card, so
                # re-importing after a format change updates the existing note.
                genanki.guid_for(f"clf-c02-missed-{number}-{q['number']}"),
            ))

    name = f"AWS CLF-C02::5 Missed {DOMAIN_NAMES[args.domain]}"
    deck = genanki.Deck(DECK_ID_BASE + args.domain, name)
    for front, back, source, guid in cards:
        deck.add_note(genanki.Note(model=MODEL, fields=[front, back, source], guid=guid,
                                   tags=[f"domain-{args.domain}", "missed"]))

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    filename = out / f"5-Missed-Domain-{args.domain}.apkg"
    genanki.Package(deck).write_to_file(filename)
    print(f"{len(cards)} cards  ->  {filename}")


if __name__ == "__main__":
    main()
