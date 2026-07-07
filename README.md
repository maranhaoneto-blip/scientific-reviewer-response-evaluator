# Scientific Reviewer Response Evaluator

A lightweight evaluation framework for assessing the quality of reviewer responses in scientific manuscripts.

## Project goal

This project explores how structured evaluation methods can be applied to scientific writing and publication workflows.

The first version focuses on reviewer response letters. It evaluates whether a response to a reviewer comment is adequate for manuscript resubmission.

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

The practical adequacy criteria are available in `docs/PRACTICAL_CRITERIA.md`.

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
- assigns an adequacy decision;
- indicates whether the response is ready to send;
- identifies the main practical issue;
- suggests a concrete fix;
- adds a qualitative evaluation summary;
- compares the predicted label with the expected label;
- exports case-level and summary evaluation reports as CSV.

## Practical adequacy framework

This project adapts established guidance on responding to reviewer comments into a structured decision aid.

The practical framework emphasizes whether the response:

- addresses the reviewer comment directly;
- describes the manuscript change clearly;
- gives a defensible rationale when no change was made;
- remains scientifically and methodologically accurate;
- uses a professional, non-defensive tone;
- is actionable and traceable in the revised manuscript;
- is clear enough for the reviewer or editor to verify quickly.

The detailed practical criteria are available in `docs/PRACTICAL_CRITERIA.md`.

## Custom GPT Companion

A no-API Custom GPT companion was created to allow users to paste reviewer comments, manuscript context, and proposed author responses directly into ChatGPT.

The GPT returns a structured publication-readiness assessment, including:

- adequacy decision;
- ready-to-send status;
- criterion scores;
- main issue;
- suggested fix;
- evaluation summary;
- improved response.

This companion tool is intended as a practical publication-readiness aid. It is not a validated measurement instrument and does not replace author, editor, statistician, or subject-matter judgment.

Recommended GPT name:

```text
Reviewer Response Readiness Checker
```

## Project structure

```text
scientific-reviewer-response-evaluator/
|
├── data/
│   └── sample_reviewer_responses.csv
|
├── docs/
│   ├── PRACTICAL_CRITERIA.md
│   └── RUBRIC.md
|
├── outputs/
│   ├── evaluation_report.csv
│   └── summary_metrics.csv
|
├── src/
│   └── evaluate_responses.py
|
├── tests/
│   └── test_scoring.py
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
```

The case-level report includes:

- individual rubric scores;
- final average score;
- assigned quality label;
- practical recommendation label;
- adequacy decision;
- ready-to-send decision;
- qualitative evaluation summary;
- main issue;
- suggested fix;
- expected label;
- agreement between assigned and expected labels.

The summary metrics file includes aggregate results such as:

- total number of cases;
- label accuracy;
- average final score;
- average score for each rubric criterion;
- recommendation counts.

## Skills demonstrated

This MVP demonstrates:

- structured AI evaluation design;
- rubric-based assessment;
- scientific writing quality evaluation;
- practical reviewer-response readiness assessment;
- CSV data processing with Python;
- automated testing with pytest;
- basic software project organization;
- Git and GitHub version control;
- documentation of evaluation criteria.

## Roadmap

Planned next steps:

- expand the dataset with more realistic reviewer-response cases;
- add response-type categories such as methodological, statistical, interpretation, wording, and scope comments;
- improve main-issue detection using reviewer-comment and response text;
- add output tailored for authors preparing resubmission;
- compare different prompt strategies;
- create a simple dashboard;
- develop an API endpoint for automated evaluation.
