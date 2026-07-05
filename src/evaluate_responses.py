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

    for result in results:
        recommendation = result["recommendation"]
        recommendation_counts[recommendation] = recommendation_counts.get(recommendation, 0) + 1

    for recommendation, count in recommendation_counts.items():
        summary[f"count_{recommendation}"] = count

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