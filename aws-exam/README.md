# AWS Certified Cloud Practitioner (CLF-C02) practice exam

A full-length practice exam built to the official CLF-C02 exam guide: 65 questions,
90 minutes, and the same number of questions drawn from each domain as the real exam's
published weightings.

## Exam composition

| Domain | Official weighting | Questions here |
| --- | --- | --- |
| 1. Cloud Concepts | 24% | 16 |
| 2. Security and Compliance | 30% | 19 |
| 3. Cloud Technology and Services | 34% | 22 |
| 4. Billing, Pricing, and Support | 12% | 8 |
| **Total** | **100%** | **65** |

Counts are the official percentages applied to 65 questions and rounded to the nearest
whole question. Six questions are multi-response (*Choose TWO*), scored all-or-nothing,
matching the format of the real exam.

The real exam mixes 15 unscored questions in with 50 scored ones. All 65 here are scored,
so you get feedback on every question.

## Files

| File | What it is |
| --- | --- |
| `exam_01.json` | The question bank — the single source of truth. Each question carries its domain, topic, type, options, answers, an explanation, and a note on why the other options are wrong. |
| `build.py` | Validates the bank and generates the two outputs below. |
| `template.html` | Page template for the interactive exam; `build.py` inlines the question bank into it. |
| `AWS-CLF-C02-Practice-Exam-01.md` | Printable exam paper, followed by an answer key, per-question explanations, and a domain scoring sheet. |
| `AWS-CLF-C02-Practice-Exam-01.html` | Self-contained interactive exam: countdown timer, question navigator, flag-for-review, and per-domain scoring. Open it directly in a browser. |

Both outputs are generated. Edit `exam_01.json` (or `template.html`), never the generated
files, then rebuild:

```bash
python3 build.py
```

`build.py` fails loudly if the bank drifts out of composition — wrong total, wrong count in
a domain, weights that do not sum to 100%, a question with no correct answer, or a
multi-response question that does not have two.

## Adding another exam

Copy `exam_01.json` to `exam_02.json`, replace the questions, and run
`python3 build.py exam_02.json`. Keep the `exam.domains` block intact so the new exam is
validated against the same composition.

## Scoring

The real exam is scaled to 100–1000 with a pass at 700, roughly 70% of the scored
questions. Both outputs report plain percentages and mark 70% as the line. Score by domain
rather than overall — a gap in Cloud Technology and Services (34% of the exam) costs about
three times what the same gap costs in Billing, Pricing, and Support (12%).
