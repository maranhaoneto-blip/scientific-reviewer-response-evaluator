from pathlib import Path
import csv


PROJECT_ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = PROJECT_ROOT / "data" / "sample_reviewer_responses.csv"
REPORT_FILE = PROJECT_ROOT / "outputs" / "evaluation_report.csv"
SUMMARY_FILE = PROJECT_ROOT / "outputs" / "summary_metrics.csv"


SCORE_COLUMNS = [
    "completeness",
    "scientific_accuracy",
    "tone",
    "actionability",
    "clarity",
]


def assign_label(final_score):
    """Assign a quality label based on the final average score."""
    if final_score >= 4.5:
        return "strong"
    elif final_score >= 3.5:
        return "acceptable"
    elif final_score >= 2.5:
        return "needs_revision"
    else:
        return "poor"


def assign_recommendation(final_label):
    """Assign a practical recommendation based on the final quality label."""
    recommendations = {
        "strong": "ready_for_submission",
        "acceptable": "minor_revision",
        "needs_revision": "major_revision",
        "poor": "reject_response",
    }

    return recommendations[final_label]


def assign_adequacy_decision(final_label):
    """Assign a practical adequacy decision based on the final quality label."""
    decisions = {
        "strong": "adequate",
        "acceptable": "adequate_with_minor_edits",
        "needs_revision": "not_ready",
        "poor": "not_adequate",
    }

    return decisions[final_label]


def assign_ready_to_send(final_label):
    """Indicate whether the response is ready for resubmission."""
    readiness = {
        "strong": "yes",
        "acceptable": "conditional",
        "needs_revision": "no",
        "poor": "no",
    }

    return readiness[final_label]


def assign_evaluation_summary(final_label):
    """Assign a qualitative summary based on the final quality label."""
    summaries = {
        "strong": (
            "The response is complete, scientifically accurate, clear, and ready "
            "for submission with minimal or no revision."
        ),
        "acceptable": (
            "The response is mostly adequate but would benefit from minor "
            "improvements in specificity, detail, or wording."
        ),
        "needs_revision": (
            "The response partially addresses the reviewer comment but requires "
            "substantive revision before submission."
        ),
        "poor": (
            "The response is incomplete, inaccurate, unclear, or not appropriate "
            "for inclusion in a reviewer response letter."
        ),
    }

    return summaries[final_label]


def identify_main_issue(row):
    """Identify the lowest-scoring rubric criterion as the main issue."""
    lowest_score = min(float(row[column]) for column in SCORE_COLUMNS)

    if lowest_score >= 4.5:
        return "no_major_issue"

    if lowest_score >= 4:
        return "minor_specificity_or_traceability_issue"

    issue_labels = {
        "completeness": "incomplete_response",
        "scientific_accuracy": "scientific_or_methodological_accuracy_issue",
        "tone": "tone_or_defensiveness_issue",
        "actionability": "unclear_revision_or_missing_manuscript_change",
        "clarity": "clarity_or_specificity_issue",
    }

    lowest_column = min(SCORE_COLUMNS, key=lambda column: float(row[column]))
    return issue_labels[lowest_column]


def suggest_fix(main_issue):
    """Suggest a practical fix for the main response issue."""
    fixes = {
        "no_major_issue": (
            "No major issue identified. The response appears adequate for "
            "resubmission."
        ),
        "minor_specificity_or_traceability_issue": (
            "Consider adding a little more specificity about the manuscript "
            "change or where the reviewer can find it."
        ),
        "incomplete_response": (
            "Address every part of the reviewer comment and make clear what was "
            "changed in the manuscript."
        ),
        "scientific_or_methodological_accuracy_issue": (
            "Revise the response to avoid unsupported claims and ensure the "
            "methodological explanation matches the study design and analysis."
        ),
        "tone_or_defensiveness_issue": (
            "Use a calmer and more professional tone, acknowledging the reviewer "
            "concern before explaining the revision or disagreement."
        ),
        "unclear_revision_or_missing_manuscript_change": (
            "Specify the concrete manuscript change, including the section, table, "
            "figure, analysis, or limitation that was revised."
        ),
        "clarity_or_specificity_issue": (
            "Make the response more specific and easier for the reviewer to verify."
        ),
    }

    return fixes[main_issue]


def calculate_final_score(row):
    """Calculate the mean score across all rubric criteria."""
    scores = []

    for column in SCORE_COLUMNS:
        value = float(row[column])
        scores.append(value)

    return round(sum(scores) / len(scores), 2)


def create_case_report(rows):
    """Create one evaluation result per case."""
    results = []

    for row in rows:
        final_score = calculate_final_score(row)
        final_label = assign_label(final_score)
        recommendation = assign_recommendation(final_label)
        adequacy_decision = assign_adequacy_decision(final_label)
        ready_to_send = assign_ready_to_send(final_label)
        evaluation_summary = assign_evaluation_summary(final_label)
        main_issue = identify_main_issue(row)
        suggested_fix = suggest_fix(main_issue)
        expected_label = row["expected_final_label"]

        result = {
            "case_id": row["case_id"],
            "completeness": row["completeness"],
            "scientific_accuracy": row["scientific_accuracy"],
            "tone": row["tone"],
            "actionability": row["actionability"],
            "clarity": row["clarity"],
            "final_score": final_score,
            "final_label": final_label,
            "recommendation": recommendation,
            "adequacy_decision": adequacy_decision,
            "ready_to_send": ready_to_send,
            "evaluation_summary": evaluation_summary,
            "main_issue": main_issue,
            "suggested_fix": suggested_fix,
            "expected_final_label": expected_label,
            "label_match": final_label == expected_label,
        }

        results.append(result)

    return results


def create_summary_metrics(results):
    """Create aggregate evaluation metrics."""
    total_cases = len(results)
    label_matches = sum(result["label_match"] for result in results)
    label_accuracy = label_matches / total_cases if total_cases > 0 else 0

    summary = {
        "total_cases": total_cases,
        "label_matches": label_matches,
        "label_accuracy": round(label_accuracy, 2),
        "average_final_score": round(
            sum(float(result["final_score"]) for result in results) / total_cases, 2
        ),
    }

    for column in SCORE_COLUMNS:
        summary[f"average_{column}"] = round(
            sum(float(result[column]) for result in results) / total_cases, 2
        )

    recommendation_counts = {}
    adequacy_counts = {}

    for result in results:
        recommendation = result["recommendation"]
        recommendation_counts[recommendation] = recommendation_counts.get(recommendation, 0) + 1

        adequacy_decision = result["adequacy_decision"]
        adequacy_counts[adequacy_decision] = adequacy_counts.get(adequacy_decision, 0) + 1

    for recommendation, count in recommendation_counts.items():
        summary[f"count_{recommendation}"] = count

    for adequacy_decision, count in adequacy_counts.items():
        summary[f"count_{adequacy_decision}"] = count

    return summary


def write_case_report(results):
    """Write the case-level evaluation report."""
    REPORT_FILE.parent.mkdir(exist_ok=True)

    fieldnames = [
        "case_id",
        "completeness",
        "scientific_accuracy",
        "tone",
        "actionability",
        "clarity",
        "final_score",
        "final_label",
        "recommendation",
        "adequacy_decision",
        "ready_to_send",
        "evaluation_summary",
        "main_issue",
        "suggested_fix",
        "expected_final_label",
        "label_match",
    ]

    with open(REPORT_FILE, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def write_summary_metrics(summary):
    """Write aggregate summary metrics."""
    with open(SUMMARY_FILE, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["metric", "value"])

        for metric, value in summary.items():
            writer.writerow([metric, value])


def main():
    with open(INPUT_FILE, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    results = create_case_report(rows)
    summary = create_summary_metrics(results)

    write_case_report(results)
    write_summary_metrics(summary)

    print("Evaluation completed.")
    print(f"Case-level report saved to: {REPORT_FILE}")
    print(f"Summary metrics saved to: {SUMMARY_FILE}")


if __name__ == "__main__":
    main()
