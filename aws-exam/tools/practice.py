#!/usr/bin/env python3
"""Take and grade the practice exams from the kananinirav CLF-C02 notes repo.

    # print questions to answer (no answer key shown)
    python3 practice.py show 5
    python3 practice.py show 5 --from 1 --to 10

    # grade a set of answers, in more or less any format
    python3 practice.py grade 5 "1A 2D 3B 4BE 5A"
    python3 practice.py grade 5 --file my-answers.txt
    python3 practice.py grade 5 "..." --show      # print the missed questions in full

Answers are parsed leniently: "1A", "1. A", "1 - A", "1: A" all work, and a
multi-response answer can be written "4BE", "4 B,E" or "4 - B and E".

The exam corpus is not stored in this repo. Clone it first:

    git clone --depth 1 \\
      https://github.com/kananinirav/aws-certified-cloud-practitioner-notes \\
      ~/aws-cp-notes

then pass --repo ~/aws-cp-notes/practice-exam (or set PRACTICE_EXAM_DIR).
"""

import argparse
import os
import re
import sys
import textwrap
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from parse_practice_exams import parse_file  # noqa: E402

REPO_TAIL = "aws-certified-cloud-practitioner-notes/practice-exam"
CANDIDATE_DIRS = [
    Path("/home/user/kananinirav") / REPO_TAIL,
    Path("/home/user") / REPO_TAIL,
    Path.home() / REPO_TAIL,
    Path.home() / "aws-cp-notes/practice-exam",
]


def default_dir():
    """First clone location that actually exists, else the first candidate."""
    if "PRACTICE_EXAM_DIR" in os.environ:
        return os.environ["PRACTICE_EXAM_DIR"]
    for candidate in CANDIDATE_DIRS:
        if candidate.is_dir():
            return str(candidate)
    return str(CANDIDATE_DIRS[0])

DOMAIN_NAMES = {
    1: "Cloud Concepts",
    2: "Security and Compliance",
    3: "Cloud Technology and Services",
    4: "Billing, Pricing and Support",
    0: "Unclassified",
}

# One numbered answer: a question number, an optional separator, then a run of
# option letters. The run may be written "BE", "B,E", "B / E" or "B and E".
#
# The trailing (?![A-Za-z]) is what keeps prose out: it forces the run to end at
# a non-letter, so in "1 A because" the engine backtracks off "beca" and matches
# just "A". Without it, ordinary words get read as answers.
ANSWER_ITEM_RE = re.compile(
    r"(\d+)\s*[.:)\-=]?\s*([A-Ea-e](?:[\s,/&+]*[A-Ea-e])*)(?![A-Za-z])"
)


def load_exam(number, folder):
    path = Path(folder) / f"practice-exam-{number}.md"
    if not path.exists():
        available = sorted(
            int(re.search(r"(\d+)", p.stem).group(1))
            for p in Path(folder).glob("practice-exam-*.md")
        )
        raise SystemExit(
            f"no such exam: {path}\navailable exams: "
            + ", ".join(str(a) for a in available)
        )
    questions, problems = parse_file(path)
    for problem in problems:
        print(f"warning: {problem}", file=sys.stderr)
    return [q for q in questions if q["options"] and q["answers"]]


def parse_answers(text):
    """Return {question_number: [letters]} from free-form input."""
    # Drop the word "and" first: its letters are in the option range, so
    # "B and E" would otherwise terminate the run at the stray 'n'.
    text = re.sub(r"\band\b", " ", text, flags=re.I)
    found = {}
    for match in ANSWER_ITEM_RE.finditer(text):
        letters = sorted({c.upper() for c in re.findall(r"[A-Ea-e]", match.group(2))})
        if letters:
            found[int(match.group(1))] = letters
    return found


def cmd_show(args):
    questions = load_exam(args.exam, args.repo)
    lo = args.start or 1
    hi = args.end or len(questions)
    shown = [q for q in questions if lo <= q["number"] <= hi]

    print(f"# Practice Exam {args.exam} — questions {lo}–{min(hi, len(questions))} "
          f"of {len(questions)}\n")
    for q in shown:
        marker = "  (Choose TWO)" if q["type"] == "multi" else ""
        print(f"{q['number']}. {q['stem']}{marker}")
        for letter, text in sorted(q["options"].items()):
            print(f"    {letter}. {text}")
        print()
    print(f"Answer format: {lo}A {lo + 1}C {lo + 2}BE ...")


def cmd_grade(args):
    questions = load_exam(args.exam, args.repo)
    by_number = {q["number"]: q for q in questions}

    raw = Path(args.file).read_text() if args.file else args.answers
    submitted = parse_answers(raw or "")
    if not submitted:
        raise SystemExit("could not read any answers from the input")

    unknown = sorted(n for n in submitted if n not in by_number)
    if unknown:
        print(f"warning: ignoring answers for questions not in this exam: "
              f"{', '.join(map(str, unknown))}\n", file=sys.stderr)

    results = []
    for q in questions:
        given = submitted.get(q["number"], [])
        correct = sorted(q["answers"])
        ok = given == correct
        results.append((q, given, correct, ok))

    answered = [r for r in results if r[1]]
    right = [r for r in results if r[3]]
    total = len(results)
    pct = len(right) / total * 100

    print(f"PRACTICE EXAM {args.exam}")
    print("=" * 62)
    print(f"Score: {len(right)}/{total}  ({pct:.0f}%)   "
          f"{'PASS' if pct >= 70 else 'BELOW'} the ~70% line")
    if len(answered) < total:
        print(f"Unanswered: {total - len(answered)} "
              f"(counted wrong — there is no guessing penalty on the real exam)")
    print()

    # --- by domain ---
    dom_total, dom_right = Counter(), Counter()
    for q, _, _, ok in results:
        dom_total[q["domain"]] += 1
        dom_right[q["domain"]] += ok
    print("BY DOMAIN")
    print("-" * 62)
    for domain in sorted(dom_total, key=lambda d: (d == 0, d)):
        n, r = dom_total[domain], dom_right[domain]
        share = r / n * 100
        bar = "#" * round(share / 5) + "." * (20 - round(share / 5))
        print(f"  {DOMAIN_NAMES[domain]:<32} {bar} {r:>2}/{n:<3} {share:>3.0f}%")
    print()

    # --- by topic, worst first ---
    topic_total, topic_right = Counter(), Counter()
    for q, _, _, ok in results:
        key = (q["domain"], q["topic"])
        topic_total[key] += 1
        topic_right[key] += ok
    missed_topics = [
        (k, topic_right[k], topic_total[k])
        for k in topic_total if topic_right[k] < topic_total[k]
    ]
    if missed_topics:
        missed_topics.sort(key=lambda t: (t[1] / t[2], -(t[2] - t[1])))
        print("TOPICS WITH MISSES  (weakest first)")
        print("-" * 62)
        for (domain, topic), r, n in missed_topics:
            print(f"  D{domain}  {topic:<38} {r}/{n}")
        print()

    # --- the misses themselves ---
    misses = [r for r in results if not r[3]]
    if misses:
        print(f"MISSED QUESTIONS ({len(misses)})")
        print("-" * 62)
        for q, given, correct, _ in misses:
            you = "".join(given) if given else "—"
            print(f"  Q{q['number']:<3} you: {you:<4} correct: {''.join(correct):<4} "
                  f"[D{q['domain']} {q['topic']}]")
        print()

    if args.show and misses:
        print("MISSED QUESTIONS IN FULL")
        print("=" * 62)
        for q, given, correct, _ in misses:
            print(f"\n{q['number']}. " + textwrap.fill(q["stem"], 78,
                                                       subsequent_indent="   "))
            for letter, text in sorted(q["options"].items()):
                mark = " <- correct" if letter in correct else (
                    " <- your answer" if letter in given else "")
                print(textwrap.fill(f"    {letter}. {text}{mark}", 78,
                                    subsequent_indent="       "))
    return 0


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", default=default_dir(),
                        help="path to the repo's practice-exam folder")
    sub = parser.add_subparsers(dest="command", required=True)

    show = sub.add_parser("show", help="print an exam's questions")
    show.add_argument("exam", type=int)
    show.add_argument("--from", dest="start", type=int)
    show.add_argument("--to", dest="end", type=int)
    show.set_defaults(func=cmd_show)

    grade = sub.add_parser("grade", help="grade answers against an exam")
    grade.add_argument("exam", type=int)
    grade.add_argument("answers", nargs="?", default="")
    grade.add_argument("--file", help="read answers from a file instead")
    grade.add_argument("--show", action="store_true",
                       help="print the missed questions in full")
    grade.set_defaults(func=cmd_grade)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        os._exit(0)  # piped into head/less; nothing to flush
