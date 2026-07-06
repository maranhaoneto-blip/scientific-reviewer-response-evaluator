# Practical Adequacy Criteria

This project evaluates whether a response to a peer reviewer is adequate for manuscript resubmission.

The goal is practical readiness, not validation of a new measurement instrument.

The criteria below adapt established guidance on responding to reviewer comments into a structured evaluation framework.

## Core Decision

The central question is:

> Is this response adequate to send to the editor and reviewer?

The tool should help classify a response as:

- `adequate`
- `adequate_with_minor_edits`
- `not_ready`
- `not_adequate`

## Practical Criteria

### 1. Addresses the Reviewer Comment

An adequate response should directly address the specific concern raised by the reviewer.

Common problems:

- the response is too generic;
- the response avoids the actual concern;
- only part of the comment is addressed;
- the response says the manuscript was improved without saying how.

### 2. Describes the Manuscript Change

When a change was made, the response should specify what was changed.

Strong responses usually state:

- what was revised;
- where the revision was made;
- how the change addresses the concern.

### 3. Gives a Clear Rationale When No Change Was Made

Not every reviewer request must be accepted, but disagreement should be justified respectfully.

An adequate disagreement should:

- acknowledge the reviewer concern;
- explain why the requested change was not made;
- provide methodological, empirical, or scope-based reasoning;
- avoid defensive language.

### 4. Maintains Scientific Accuracy

The response should not overclaim, imply unsupported causality, misrepresent statistical findings, or introduce new inaccuracies.

This is especially important for:

- observational studies;
- causal wording;
- subgroup analyses;
- sensitivity analyses;
- missing data;
- statistical significance;
- limitations.

### 5. Uses a Professional Tone

The response should be polite, calm, and non-defensive.

Professional tone does not require excessive praise. It requires clarity, respect, and focus on the scientific issue.

### 6. Is Actionable and Traceable

The editor or reviewer should be able to understand what changed and verify it in the manuscript.

Useful details include:

- revised section;
- table or figure number;
- added sentence;
- changed terminology;
- new analysis;
- added limitation.

### 7. Is Clear and Concise

The response should be easy to review.

Common problems:

- vague wording;
- overly broad claims;
- unnecessary explanation;
- unclear link between the reviewer comment and the revision.

## Output Fields

The tool should generate:

| Field | Purpose |
|---|---|
| `adequacy_decision` | Practical decision about whether the response is adequate |
| `ready_to_send` | Whether the response can be submitted as written |
| `main_issue` | Main reason the response may not be ready |
| `suggested_fix` | Practical improvement before resubmission |

## Decision Mapping

| Final label | Adequacy decision | Ready to send |
|---|---|---|
| `strong` | `adequate` | `yes` |
| `acceptable` | `adequate_with_minor_edits` | `conditional` |
| `needs_revision` | `not_ready` | `no` |
| `poor` | `not_adequate` | `no` |

## Main Issue Mapping

| Main issue | Meaning |
|---|---|
| `no_major_issue` | The response appears adequate for resubmission |
| `minor_specificity_or_traceability_issue` | The response is broadly adequate but could better specify what changed or where |
| `incomplete_response` | The response does not address all parts of the reviewer comment |
| `scientific_or_methodological_accuracy_issue` | The response may be scientifically or methodologically inaccurate |
| `tone_or_defensiveness_issue` | The response may sound defensive or insufficiently professional |
| `unclear_revision_or_missing_manuscript_change` | The response does not clearly state what was changed in the manuscript |
| `clarity_or_specificity_issue` | The response is too vague or difficult to verify |

## Intended Use

This tool is intended as a practical decision aid for authors, researchers, editors, and scientific writing consultants.

It does not replace expert judgment. It helps identify whether a reviewer response is sufficiently complete, accurate, professional, and actionable before resubmission.
