from collections import Counter
from pathlib import Path
import csv


PROJECT_ROOT = Path(__file__).resolve().parents[1]

EXPERT_RATINGS_FILE = PROJECT_ROOT / "data" / "sample_expert_ratings.csv"
VALIDATION_OUTPUT_FILE = PROJECT_ROOT / "outputs" / "validation_metrics.csv"


SCORE_COLUMNS = [
    "completeness",
    "scientific_accuracy",
    "tone",
    "actionability",
    "clarity",
]


def calculate_percent_agreement(labels):
    """Calculate the proportion of ratings matching the modal label."""
    if not labels:
        return 0

    counts = Counter(labels)
    modal_count = counts.most_common(1)[0][1]
    return round(modal_count / len(labels), 2)


def calculate_final_score(row):
    """Calculate a rater-level final score from rubric criteria."""
    scores = [float(row[column]) for column in SCORE_COLUMNS]
    return round(sum(scores) / len(scores), 2)


def assign_consensus_label(labels):
    """Assign the most common expert label for a case."""
    if not labels:
        return ""

    counts = Counter(labels)
    top_count = counts.most_common(1)[0][1]
    top_labels = sorted(label for label, count in counts.items() if count == top_count)
    return top_labels[0]


def group_ratings_by_case(rows):
    """Group expert ratings by case identifier."""
    grouped = {}

    for row in rows:
        case_id = row["case_id"]
        grouped.setdefault(case_id, []).append(row)

    return grouped


def create_validation_metrics(rows):
    """Create case-level validation metrics from expert ratings."""
    grouped = group_ratings_by_case(rows)
    metrics = []

    for case_id, case_rows in grouped.items():
        labels = [row["expert_final_label"] for row in case_rows if row["expert_final_label"]]
        final_scores = [calculate_final_score(row) for row in case_rows]

        metric = {
            "case_id": case_id,
            "number_of_raters": len(case_rows),
            "consensus_label": assign_consensus_label(labels),
            "label_percent_agreement": calculate_percent_agreement(labels),
            "mean_expert_score": round(sum(final_scores) / len(final_scores), 2),
        }

        metrics.append(metric)

    return metrics


def write_validation_metrics(metrics):
    """Write validation metrics to CSV."""
    VALIDATION_OUTPUT_FILE.parent.mkdir(exist_ok=True)

    fieldnames = [
        "case_id",
        "number_of_raters",
        "consensus_label",
        "label_percent_agreement",
        "mean_expert_score",
    ]

    with open(VALIDATION_OUTPUT_FILE, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(metrics)


def main():
    with open(EXPERT_RATINGS_FILE, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    metrics = create_validation_metrics(rows)
    write_validation_metrics(metrics)

    print("Validation metrics completed.")
    print(f"Validation metrics saved to: {VALIDATION_OUTPUT_FILE}")


if __name__ == "__main__":
    main()
