# Custom GPT Test Checklist

This checklist documents practical tests for the Reviewer Response Readiness Checker Custom GPT companion.

The goal is to verify whether the GPT behaves consistently with the intended publication-readiness use case:

Is this response to the reviewer adequate to send to the editor or reviewer?

## Expected Output Fields

The GPT should return:

- adequacy decision
- ready-to-send status
- final score
- final label
- main issue
- suggested fix
- criterion scores
- evaluation summary
- improved response

## Test Cases

| Test case | Expected decision | Key issue |
|---|---|---|
| Unsupported causal language in an observational study | not_ready or not_adequate | Causal overclaiming |
| Vague response about missing outcome data | not_ready | Missing methodological detail |
| Defensive disagreement with a reviewer request | not_ready or not_adequate | Insufficient rationale and tone issue |
| Strong response that directly addresses the reviewer | adequate or adequate_with_minor_edits | No major issue or minor traceability issue |
| Full reviewer-response package | adequate_with_minor_edits if mostly complete | Package-level traceability |

## Failure Modes to Watch

The GPT should be adjusted if it:

- approves vague responses that do not explain what changed
- fails to detect causal overclaiming in observational studies
- invents analyses, results, line numbers, or manuscript changes
- treats every reviewer request as mandatory even when justified disagreement is appropriate
- produces excessive praise instead of a professional response
- omits the improved response
- merges the improved response into the evaluation summary
