# Example Evaluations

This document provides practical examples of how the Reviewer Response Readiness Checker evaluates proposed responses to scientific peer-review comments.

The examples are intended for portfolio and documentation purposes. They illustrate expected GPT behavior in common reviewer-response situations.

The goal is not to validate a new measurement instrument. The goal is to demonstrate practical publication-readiness evaluation.

## Example 1: Unsupported Causal Language

### Reviewer comment

Please clarify whether the conclusion should be interpreted causally.

### Manuscript context

The study is observational and reports adjusted associations.

### Proposed response

Thank you. We revised the conclusion to say that the intervention caused lower mortality.

### GPT assessment

Adequacy decision: not_adequate

Ready to send: no

Final label: poor

Main issue:

The proposed response introduces unsupported causal language that is inconsistent with the observational study design.

Suggested fix:

Revise the response to state that the conclusion was changed to use association-based language and explicitly acknowledge that causal inference is not supported by the study design.

### Improved response

Thank you for this important comment. We agree that our observational study, which reports adjusted associations, does not support causal inference. We have revised the conclusion to replace causal wording with association-based language so that it more accurately reflects the study design and findings. Specifically, we revised the Conclusion section to state that the intervention was associated with lower mortality rather than that it caused lower mortality.

### Why this matters

This example tests whether the GPT detects causal overclaiming, especially when the manuscript is observational and the reviewer explicitly asks for causal caution.

## Example 2: Vague Response About Missing Data

### Reviewer comment

The methods section does not explain how missing outcome data were handled.

### Manuscript context

Some 90-day outcome data are missing. The authors used complete-case analysis for the primary analysis and multiple imputation as a sensitivity analysis.

### Proposed response

Thank you. We improved the methods section and clarified the analysis.

### GPT assessment

Adequacy decision: not_ready

Ready to send: no

Final label: needs_revision

Main issue:

The response does not explain how missing outcome data were handled and provides no specific description of the manuscript revision.

Suggested fix:

State explicitly that the primary analysis used complete-case analysis, that multiple imputation was performed as a sensitivity analysis, and indicate where these details were added in the manuscript.

### Improved response

Thank you for this helpful comment. We have revised the Methods section to clarify how missing 90-day outcome data were handled. Specifically, we now state that the primary analysis was conducted using complete-case analysis. We also clarify that multiple imputation was performed as a sensitivity analysis to assess the robustness of the findings to missing outcome data. These revisions have been added to the Methods section [page X, lines Y-Z].

### Why this matters

This example tests whether the GPT penalizes vague responses such as “we improved the manuscript” when the reviewer needs a specific methodological clarification.

## Example 3: Defensive Disagreement With Reviewer Request

### Reviewer comment

Please include a sensitivity analysis excluding patients with missing baseline NIHSS.

### Manuscript context

The dataset does not allow reliable reconstruction of NIHSS for excluded patients. Excluding these patients would substantially reduce the sample size and may introduce selection bias.

### Proposed response

We do not think this analysis is necessary because the current analysis is already sufficient.

### GPT assessment

Adequacy decision: not_adequate

Ready to send: no

Final label: poor

Main issue:

The response dismisses the reviewer’s request without providing a scientific or methodological justification.

Suggested fix:

Acknowledge the reviewer’s suggestion respectfully, explain why the requested sensitivity analysis cannot be performed or would not provide a reliable assessment, and state how this limitation has been addressed in the manuscript.

### Improved response

Thank you for this helpful suggestion. We carefully considered performing a sensitivity analysis excluding patients with missing baseline NIHSS. However, the available dataset does not allow reliable reconstruction of baseline NIHSS for these patients. Restricting the analysis to patients with complete baseline NIHSS data would also substantially reduce the sample size and could introduce selection bias, potentially limiting the interpretability of the findings. For these reasons, we did not perform the requested sensitivity analysis. We have clarified this limitation in the Discussion/Limitations section [page X, lines Y-Z].

### Why this matters

This example tests whether the GPT understands that authors may reasonably disagree with a reviewer, but only when the disagreement is respectful, transparent, and methodologically justified.

## Example 4: Strong but Slightly Incomplete Response

### Reviewer comment

The authors should clarify whether the regression models were adjusted for baseline stroke severity.

### Manuscript context

The Methods section states that multivariable models were adjusted for age, sex, baseline NIHSS, pre-stroke mRS, and onset-to-treatment time.

### Proposed response

We thank the reviewer for this helpful comment. We have clarified in the Methods section that baseline stroke severity, measured by NIHSS, was included as an adjustment variable in all multivariable models.

### Expected assessment

Adequacy decision: adequate_with_minor_edits

Ready to send: conditional

Final label: acceptable

Main issue:

The response is scientifically appropriate and directly addresses the reviewer comment, but it would be stronger if it included the exact manuscript location.

Suggested fix:

Add page and line numbers, or the specific section where the clarification was made.

### Improved response

Thank you for this helpful comment. We have clarified in the Methods section [page X, lines Y-Z] that baseline stroke severity, measured by NIHSS, was included as an adjustment variable in all multivariable models.

### Why this matters

This example tests whether the GPT can recognize a mostly adequate response and avoid over-penalizing it, while still suggesting a practical traceability improvement.

## Example 5: Full Reviewer-Response Package

### Scenario

A full response letter includes multiple reviewer comments on study design, registry limitations, missing data, exploratory analyses, sensitivity analyses, and supplementary tables.

### Expected package-level assessment

Adequacy decision: adequate_with_minor_edits

Ready to send: conditional

Final label: acceptable

Main issue:

The responses are generally scientifically appropriate and complete, but several replies need clearer traceability to manuscript changes.

### Typical suggested fixes

Before submission, the response letter should:

- add page, line, table, or section references whenever manuscript changes are described;
- standardize wording such as “we added,” “we clarified,” and “we expanded”;
- distinguish exploratory analyses from confirmatory analyses;
- avoid overstating results from post hoc or subgroup analyses;
- clarify any limitations related to missing data or registry constraints;
- ensure that supplementary tables are clearly explained and consistent with the main analysis.

### Example improved package-level recommendation

The response package appears substantially ready for resubmission, with minor edits needed before sending. The main recommended improvement is to improve traceability by indicating where each change was made in the manuscript. Adding page and line references, table numbers, or section names would make it easier for the editor and reviewers to verify the revisions quickly.

### Why this matters

This example tests whether the GPT can evaluate a full response package, rather than only isolated reviewer-response pairs. It should identify package-level readiness while still detecting high-priority issues in individual replies.

## Summary

These examples demonstrate that the Reviewer Response Readiness Checker is designed to identify practical publication-readiness issues, including:

- unsupported causal language;
- vague descriptions of manuscript changes;
- missing methodological detail;
- defensive or dismissive tone;
- lack of traceability;
- overstatement of exploratory analyses;
- incomplete justification for not performing a requested analysis.

The tool is intended to support authors during manuscript resubmission preparation. It does not replace author judgment, editor judgment, statistical review, or subject-matter expertise.
