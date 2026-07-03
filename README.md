# Scientific Reviewer Response Evaluator

A lightweight evaluation framework for assessing the quality of reviewer responses in scientific manuscripts.

## Project goal

This project explores how AI evaluation methods can be applied to scientific writing and publication workflows.

The first version focuses on reviewer response letters. It evaluates whether a response to a reviewer comment is complete, scientifically accurate, diplomatic, actionable, and clear.

## Evaluation criteria

Each response is scored from 1 to 5 across five criteria:

1. Completeness
2. Scientific accuracy
3. Tone
4. Actionability
5. Clarity

The final score is calculated as the average of the five criteria.

## Rubric documentation

The full scoring rubric is available in `docs/RUBRIC.md`.

The rubric defines the scoring criteria, score levels, and final label rules used in the evaluation pipeline.

## Final labels

| Final score | Label |
|---|---|
| 4.5–5.0 | strong |
| 3.5–4.4 | acceptable |
| 2.5–3.4 | needs_revision |
| 1.0–2.4 | poor |

## Current MVP

The current version:

- reads a CSV dataset of reviewer comments and AI-generated responses;
- calculates a final score;
- assigns a quality label;
- compares the predicted label with the expected label;
- exports an evaluation report as CSV.

## Project structure

```text
scientific-reviewer-response-evaluator/
│
├── data/
│   └── sample_reviewer_responses.csv
│
├── docs/
│   └── RUBRIC.md
│
├── outputs/
│   ├── evaluation_report.csv
│   └── summary_metrics.csv
│
├── src/
│   └── evaluate_responses.py
│
├── tests/
│   └── test_scoring.py
│
├── .gitignore
├── README.md
└── requirements.txt
```
## Installation

Install the required Python packages with:

```bash
python -m pip install -r requirements.txt
```
