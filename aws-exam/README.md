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

## Taking the external practice exams

`tools/` grades the 23 CLF-C02 practice exams published by
[kananinirav/aws-certified-cloud-practitioner-notes](https://github.com/kananinirav/aws-certified-cloud-practitioner-notes)
(MIT licensed, ~1,140 questions). The corpus is not vendored here — only the
tooling is. Clone it first:

```bash
git clone --depth 1 \
  https://github.com/kananinirav/aws-certified-cloud-practitioner-notes ~/aws-cp-notes
export PRACTICE_EXAM_DIR=~/aws-cp-notes/practice-exam
```

Then:

```bash
python3 tools/practice.py show 5 --from 1 --to 10   # questions, no answer key
python3 tools/practice.py grade 5 "1A 2D 3B 4BE"    # score + domain breakdown
python3 tools/practice.py grade 5 "..." --show      # plus the missed questions in full
```

Answers parse leniently — `1A`, `1. A`, `1 - A` and `4BE` / `4 B and E` all work.
Grading reports an overall score, a per-domain breakdown, the topics you missed
ranked weakest first, and every missed question with your answer beside the
correct one.

`tools/parse_practice_exams.py` does the extraction and tags each question with a
domain and topic by keyword. Two notes on that corpus: several files use lazy
Markdown numbering (every item written as `1.`), so questions are renumbered by
document order; and the domain tagging is a keyword heuristic, useful for
grouping but not authoritative.

## Study guides

| File | What it covers |
| --- | --- |
| `question-targeting-guide.html` | How to read a CLF-C02 question in Domains 1 and 2: question anatomy, signal-word tables, the shared responsibility line across EC2/RDS/Lambda, and the eight trap pairs. Written from the exam guide. |
| `review-packet.html` | Personal review packet built from the 48 questions missed across practice exams 9, 17 and 20: the seven recurring concept gaps, a signal-word table, and 30 targeted practice problems with an answer key. |
| `corpus-patterns-guide.html` | What the external corpus actually repeats, measured rather than assumed: the most-repeated questions, per-service decoy rates, the shared responsibility inventory, and the stem-phrase-to-service map. Derived by counting across all 1,142 questions. |

The second guide's numbers come from the analysis in `tools/`; re-run
`parse_practice_exams.py` after any parser change to confirm they still hold.
