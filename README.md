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
- assigns a practical recommendation label;
- compares the predicted label with the expected label;
- exports case-level and summary evaluation reports as CSV.

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
## Example output

The evaluation pipeline generates two output files:

```text
outputs/evaluation_report.csv
outputs/summary_metrics.csv
```

The case-level report includes:

- individual rubric scores;
- final average score;
- assigned quality label;
- practical recommendation label;
- expected label;
- agreement between assigned and expected labels.

The summary metrics file includes aggregate results such as:

- total number of cases;
- label accuracy;
- average final score;
- average score for each rubric criterion.

## Skills demonstrated

This MVP demonstrates:

- structured AI evaluation design;
- rubric-based assessment;
- scientific writing quality evaluation;
- CSV data processing with Python;
- automated testing with pytest;
- basic software project organization;
- Git and GitHub version control;
- documentation of evaluation criteria.

## Roadmap

Planned next steps:

- expand the evaluation dataset;
- add qualitative explanations for each score;
- add recommendation labels such as ready_for_submission, minor_revision, major_revision, and reject_response;
- compare different prompt strategies;
- add inter-rater agreement metrics;
- create a simple dashboard;
- develop an API endpoint for automated evaluation.