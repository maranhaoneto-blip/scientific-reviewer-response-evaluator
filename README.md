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
| 4.5-5.0 | strong |
| 3.5-4.4 | acceptable |
| 2.5-3.4 | needs_revision |
| 1.0-2.4 | poor |

## Current MVP

The current version:

- reads a CSV dataset of reviewer comments and AI-generated responses;
- calculates a final score;
- assigns a quality label;
- assigns a practical recommendation label;
- adds a qualitative evaluation summary;
- includes a validation roadmap based on established measurement and reliability methods;
- provides a template for independent expert ratings;
- calculates initial expert-rating validation metrics;
- compares the predicted label with the expected label;
- exports case-level and summary evaluation reports as CSV.

## Methodological validation roadmap

This project is being extended using established methodological strategies from measurement instrument validation, reliability studies, and human evaluation of AI systems.

The validation roadmap adapts:

- content validity assessment using expert review;
- COSMIN-style thinking about measurement properties;
- GRRAS-style reporting for reliability and agreement studies;
- independent human ratings for AI evaluation;
- tool-to-expert agreement analysis.

The detailed roadmap is available in `docs/VALIDATION_PLAN.md`.

The current validation extension includes:

- `data/expert_ratings_template.csv` for collecting independent expert ratings;
- `data/sample_expert_ratings.csv` as a small runnable example;
- `src/validation_metrics.py` for calculating case-level expert consensus metrics;
- `outputs/validation_metrics.csv` as an example validation output.

## Project structure

```text
scientific-reviewer-response-evaluator/
|
├── data/
│   ├── expert_ratings_template.csv
│   ├── sample_expert_ratings.csv
│   └── sample_reviewer_responses.csv
|
├── docs/
│   ├── RUBRIC.md
│   └── VALIDATION_PLAN.md
|
├── outputs/
│   ├── evaluation_report.csv
│   ├── summary_metrics.csv
│   └── validation_metrics.csv
|
├── src/
│   ├── evaluate_responses.py
│   └── validation_metrics.py
|
├── tests/
│   ├── test_scoring.py
│   └── test_validation_metrics.py
|
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
outputs/validation_metrics.csv
```

The case-level report includes:

- individual rubric scores;
- final average score;
- assigned quality label;
- practical recommendation label;
- qualitative evaluation summary;
- expected label;
- agreement between assigned and expected labels.

The summary metrics file includes aggregate results such as:

- total number of cases;
- label accuracy;
- average final score;
- average score for each rubric criterion;
- recommendation counts.

The validation metrics file includes:

- number of expert raters per case;
- consensus expert label;
- label percent agreement;
- mean expert score.

## Skills demonstrated

This MVP demonstrates:

- structured AI evaluation design;
- rubric-based assessment;
- scientific writing quality evaluation;
- validation-oriented evaluation design;
- expert-rating workflow design;
- CSV data processing with Python;
- automated testing with pytest;
- basic software project organization;
- Git and GitHub version control;
- documentation of evaluation criteria.

## Roadmap

Planned next steps:

- expand the benchmark set with more realistic reviewer-response cases;
- collect independent expert ratings;
- calculate inter-rater agreement statistics;
- compare tool-generated labels with expert consensus labels;
- compare different prompt strategies;
- create a simple dashboard;
- develop an API endpoint for automated evaluation.
