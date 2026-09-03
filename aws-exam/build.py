#!/usr/bin/env python3
"""Build the printable and interactive versions of a practice exam.

Reads a question bank (exam_01.json) and writes:

  * <slug>.md    - a printable exam paper plus a separate answer key
  * <slug>.html  - a self-contained interactive exam (question bank inlined)

Usage:
    python3 build.py [exam_01.json]
"""

import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent


def load(path):
    data = json.loads(Path(path).read_text())
    validate(data)
    return data


def validate(data):
    """Fail loudly if the bank drifts away from the official exam composition."""
    exam, questions = data["exam"], data["questions"]
    errors = []

    if len(questions) != exam["question_count"]:
        errors.append(
            f"expected {exam['question_count']} questions, found {len(questions)}"
        )

    counts = Counter(q["domain"] for q in questions)
    for domain in exam["domains"]:
        actual = counts[domain["id"]]
        if actual != domain["questions"]:
            errors.append(
                f"domain {domain['id']} ({domain['name']}): "
                f"expected {domain['questions']} questions, found {actual}"
            )

    if sum(d["weight"] for d in exam["domains"]) != 100:
        errors.append("domain weights do not sum to 100%")

    for q in questions:
        if not q["answers"]:
            errors.append(f"Q{q['id']}: no correct answer marked")
        if q["type"] == "multi" and len(q["answers"]) < 2:
            errors.append(f"Q{q['id']}: multi-response question with one answer")
        if q["type"] == "single" and len(q["answers"]) != 1:
            errors.append(f"Q{q['id']}: single-response question with {len(q['answers'])} answers")
        for letter in q["answers"]:
            if letter not in q["options"]:
                errors.append(f"Q{q['id']}: answer {letter} is not an available option")

    if errors:
        raise SystemExit("Question bank failed validation:\n  - " + "\n  - ".join(errors))


def render_markdown(data):
    exam, questions = data["exam"], data["questions"]
    domains = {d["id"]: d for d in exam["domains"]}
    out = []
    w = out.append

    w(f"# {exam['title']}\n")
    w(f"**Certification:** {exam['certification']} ({exam['exam_code']})  ")
    w(f"**Questions:** {exam['question_count']}  ")
    w(f"**Time limit:** {exam['time_limit_minutes']} minutes  ")
    w(f"**Passing score:** {exam['passing_score']}\n")
    w(exam["note"] + "\n")

    w("## Exam composition\n")
    w("| Domain | Official weighting | Questions in this exam |")
    w("| --- | --- | --- |")
    for d in exam["domains"]:
        w(f"| {d['id']}. {d['name']} | {d['weight']}% | {d['questions']} |")
    w(f"| **Total** | **100%** | **{exam['question_count']}** |\n")

    w("Answer every question. Questions that say *Choose TWO* require exactly two")
    w("selections and are scored all-or-nothing, exactly as on the real exam.\n")
    w("---\n")
    w("## Questions\n")

    for q in questions:
        marker = " *(Choose TWO.)*" if q["type"] == "multi" and "Choose TWO" not in q["stem"] else ""
        w(f"**{q['id']}.** {q['stem']}{marker}\n")
        for letter, text in q["options"].items():
            w(f"- {letter}. {text}")
        w("")

    w("---\n")
    w("## Answer key\n")
    w("| # | Domain | Answer | Topic |")
    w("| --- | --- | --- | --- |")
    for q in questions:
        w(f"| {q['id']} | {domains[q['domain']]['name']} | "
          f"{', '.join(q['answers'])} | {q['topic']} |")
    w("")

    w("---\n")
    w("## Explanations\n")
    for q in questions:
        w(f"### {q['id']}. {q['topic']}\n")
        w(f"**Correct answer: {', '.join(q['answers'])}** "
          f"— *Domain {q['domain']}: {domains[q['domain']]['name']}*\n")
        for letter in q["answers"]:
            w(f"> {letter}. {q['options'][letter]}\n")
        w(q["explanation"] + "\n")
        w(f"**Why the other options are wrong:** {q['distractors']}\n")

    w("---\n")
    w("## Scoring this exam\n")
    w("Mark each question right or wrong, then score by domain to find where to study:\n")
    w("| Domain | Questions | Your score | % correct |")
    w("| --- | --- | --- | --- |")
    for d in exam["domains"]:
        w(f"| {d['id']}. {d['name']} | {d['questions']} | ____ | ____ |")
    w(f"| **Total** | **{exam['question_count']}** | ____ | ____ |\n")
    w("The real exam is scaled to 100-1000 with a pass at 700, which works out to")
    w("roughly 70% of the scored questions. Treat anything under 80% on this practice")
    w("exam as a signal to review that domain before booking the real thing.\n")

    return "\n".join(out)


def render_html(data, template):
    payload = json.dumps(data, indent=2)
    if "/*__EXAM_DATA__*/" not in template:
        raise SystemExit("template.html is missing the /*__EXAM_DATA__*/ placeholder")
    return template.replace("/*__EXAM_DATA__*/", payload)


def main():
    source = Path(sys.argv[1] if len(sys.argv) > 1 else HERE / "exam_01.json")
    data = load(source)
    slug = "AWS-CLF-C02-Practice-Exam-01"

    md_path = HERE / f"{slug}.md"
    md_path.write_text(render_markdown(data) + "\n")
    print(f"wrote {md_path.relative_to(HERE.parent)}")

    template_path = HERE / "template.html"
    if template_path.exists():
        html_path = HERE / f"{slug}.html"
        html_path.write_text(render_html(data, template_path.read_text()))
        print(f"wrote {html_path.relative_to(HERE.parent)}")

    counts = Counter(q["domain"] for q in data["questions"])
    print(f"validated {len(data['questions'])} questions: "
          + ", ".join(f"D{d}={counts[d]}" for d in sorted(counts)))


if __name__ == "__main__":
    main()
