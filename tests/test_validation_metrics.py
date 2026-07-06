from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.validation_metrics import (
    assign_consensus_label,
    calculate_final_score,
    calculate_percent_agreement,
    create_validation_metrics,
)


def test_calculate_percent_agreement():
    labels = ["strong", "strong", "acceptable"]
    assert calculate_percent_agreement(labels) == 0.67


def test_assign_consensus_label():
    labels = ["needs_revision", "acceptable", "acceptable"]
    assert assign_consensus_label(labels) == "acceptable"


def test_calculate_final_score():
    row = {
        "completeness": "4",
        "scientific_accuracy": "4",
        "tone": "5",
        "actionability": "3",
        "clarity": "4",
    }

    assert calculate_final_score(row) == 4.0


def test_create_validation_metrics():
    rows = [
        {
            "case_id": "case_001",
            "rater_id": "rater_001",
            "completeness": "5",
            "scientific_accuracy": "5",
            "tone": "5",
            "actionability": "4",
            "clarity": "5",
            "expert_final_label": "strong",
        },
        {
            "case_id": "case_001",
            "rater_id": "rater_002",
            "completeness": "4",
            "scientific_accuracy": "5",
            "tone": "5",
            "actionability": "4",
            "clarity": "5",
            "expert_final_label": "strong",
        },
    ]

    metrics = create_validation_metrics(rows)

    assert metrics[0]["case_id"] == "case_001"
    assert metrics[0]["number_of_raters"] == 2
    assert metrics[0]["consensus_label"] == "strong"
    assert metrics[0]["label_percent_agreement"] == 1.0
    assert metrics[0]["mean_expert_score"] == 4.7
