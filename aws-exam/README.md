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
| `exam_01.json` | Full-length mock, all four domains. The question bank is the single source of truth: each question carries its domain, topic, type, options, answers, an explanation, and a note on why the other options are wrong. |
| `exam_02.json` | Focused drill on Domains 1 and 2 only. Adds a `signal` field per question naming the keyword tell in the stem. |
| `build.py` | Validates a bank and generates its two outputs. |
| `template.html` | Shared page template for the interactive exam; `build.py` inlines the bank and the page title into it. |
| `question-targeting-guide.html` | Study guide for Domains 1 and 2: how a CLF-C02 question is built, the signal-word tables, the eight trap pairs, and where keyword matching fails. |
| `AWS-CLF-C02-Practice-Exam-01.{md,html}` | Generated from `exam_01.json`. |
| `AWS-CLF-C02-Domains-1-2-Drill.{md,html}` | Generated from `exam_02.json`. |

The `.md` output is a printable exam paper with an answer key, per-question explanations and
a domain scoring sheet. The `.html` output is a self-contained interactive exam — countdown
timer, question navigator, flag-for-review, exam and study modes, and per-domain scoring.
Open it directly in a browser; no server needed.

Outputs are generated. Edit the JSON bank (or `template.html`), never the generated files,
then rebuild:

```bash
python3 build.py              # exam_01.json, the default
python3 build.py exam_02.json
```

`build.py` fails loudly if a bank drifts out of composition — wrong total, wrong count in a
domain, weights that do not sum to 100%, a declared weight that disagrees with the actual
question count, a question with no correct answer, or a multi-response question that does
not have two.

## Adding another exam

Copy a bank, replace the questions, and run `python3 build.py exam_03.json`. The `exam`
block drives everything: `file_slug` names the output files, `slug` keys the browser's saved
progress (give every exam a distinct one or two exams will overwrite each other's state),
and `page_title`, `eyebrow`, `heading`, `short_title` and `subtitle` supply the page copy.

For a focused drill covering a subset of domains, set each domain's `weight` to its share of
*that* exam and `official_weight` to its share of the real exam. Both outputs then show the
two side by side.

## Scoring

The real exam is scaled to 100–1000 with a pass at 700, roughly 70% of the scored
questions. Both outputs report plain percentages and mark 70% as the line. Score by domain
rather than overall — a gap in Cloud Technology and Services (34% of the exam) costs about
three times what the same gap costs in Billing, Pricing, and Support (12%).
