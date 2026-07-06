# Validation Plan

This document describes the methodological roadmap for evolving the project from a rule-based MVP into a validation-oriented evaluation tool for scientific reviewer responses.

The goal is not to claim that the tool is already validated. The goal is to define how validity and reliability evidence should be collected before the scores are used for higher-stakes decisions.

## Intended Use

The tool is intended to support low-stakes evaluation of AI-generated or human-drafted responses to scientific peer-review comments.

The intended uses are:

- screening reviewer responses for obvious weaknesses;
- providing structured feedback on response quality;
- identifying responses that may need revision before submission;
- supporting research on AI-assisted scientific writing evaluation.

The tool is not intended to replace expert editorial judgment, peer-review expertise, or final author responsibility.

## Construct Definition

The target construct is reviewer-response quality in scientific publication workflows.

In this project, reviewer-response quality is defined as the extent to which a response:

- addresses the reviewer's concern completely;
- remains scientifically and methodologically accurate;
- uses a diplomatic and professional tone;
- describes a clear revision or defensible rationale;
- communicates the response clearly.

## Methodological Foundation

The validation strategy adapts established approaches from measurement science, reliability studies, and human evaluation of AI systems.

| Source area | Adapted strategy | Application in this project |
|---|---|---|
| Measurement instrument validation | Define the construct, intended use, target population, and interpretation limits | Document the use case and avoid overclaiming validity |
| COSMIN-style measurement properties | Assess content validity, reliability, interpretability, and generalizability | Treat the rubric as a measurement instrument |
| Content validity methods | Ask experts to rate relevance and clarity of each criterion | Calculate item-level and scale-level content validity indices |
| GRRAS reliability reporting | Report rater sampling, case sampling, rating procedure, and agreement statistics | Make reliability evidence transparent and reproducible |
| Human evaluation of LLMs | Use independent expert ratings and predefined dimensions | Compare tool outputs against expert ratings rather than circular labels |

## Validation Phases

### Phase 1: Content Validity

Goal: determine whether the rubric criteria adequately represent reviewer-response quality.

Proposed procedure:

1. Recruit 3-5 subject-matter experts in scientific writing, peer review, epidemiology, clinical research, or publication strategy.
2. Ask experts to rate each rubric criterion for:
   - relevance;
   - clarity;
   - necessity;
   - missing dimensions.
3. Calculate item-level content validity indices for each criterion.
4. Revise the rubric based on quantitative ratings and qualitative comments.

Expected output:

- `outputs/content_validity_report.csv`
- revised `docs/RUBRIC.md`

### Phase 2: Expert-Rated Benchmark Set

Goal: replace circular expected labels with independent expert labels.

Proposed procedure:

1. Expand the dataset to include a balanced set of strong, acceptable, needs_revision, and poor responses.
2. Include borderline cases between adjacent labels.
3. Ask at least two independent raters to score each case using the rubric.
4. Resolve disagreement through consensus or majority rule when more than two raters are available.

Expected output:

- `data/expert_ratings.csv`
- `data/benchmark_cases.csv`

### Phase 3: Inter-Rater Agreement and Reliability

Goal: determine whether human raters can apply the rubric consistently.

Proposed metrics:

- percent agreement for final labels;
- criterion-level agreement;
- weighted kappa for ordinal scores;
- intraclass correlation coefficient for numeric final scores;
- Gwet agreement coefficient when labels are highly imbalanced.

Expected output:

- `outputs/inter_rater_reliability.csv`

### Phase 4: Tool-to-Expert Agreement

Goal: evaluate whether tool-generated labels align with expert-derived labels.

Proposed metrics:

- exact label agreement;
- adjacent-label agreement;
- confusion matrix;
- mean absolute error for final scores;
- criterion-level differences between tool and expert ratings.

Expected output:

- `outputs/tool_expert_agreement.csv`

### Phase 5: Robustness and Generalizability

Goal: test whether the tool performs consistently across realistic variations.

Proposed checks:

- paraphrased reviewer comments;
- different manuscript contexts;
- different scientific domains;
- short versus detailed AI responses;
- balanced versus imbalanced label distributions.

Expected output:

- `outputs/robustness_report.csv`

## Reporting Principles

All validation results should report:

- number and background of raters;
- number and type of cases;
- rating instructions;
- version of the rubric;
- scoring rules;
- missing data handling;
- agreement metrics;
- limitations.

## Current Status

The current project is a rule-based MVP with a small synthetic dataset.

The current labels are useful for testing the scoring pipeline, but they should not yet be interpreted as external validation evidence. The next methodological step is to collect independent expert ratings and compare the tool output against those ratings.

## Practical Next Step

The next implementation step is to use `data/expert_ratings_template.csv` to collect ratings from independent reviewers and then calculate initial agreement metrics with `src/validation_metrics.py`.
