from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.evaluate_responses import (
    assign_label,
    assign_recommendation,
    calculate_final_score,
)


def test_assign_label_strong():
    assert assign_label(4.5) == "strong"
    assert assign_label(5.0) == "strong"


def test_assign_label_acceptable():
    assert assign_label(3.5) == "acceptable"
    assert assign_label(4.4) == "acceptable"


def test_assign_label_needs_revision():
    assert assign_label(2.5) == "needs_revision"
    assert assign_label(3.4) == "needs_revision"


def test_assign_label_poor():
    assert assign_label(1.0) == "poor"
    assert assign_label(2.4) == "poor"


def test_calculate_final_score():
    row = {
        "completeness": "5",
        "scientific_accuracy": "5",
        "tone": "4",
        "actionability": "4",
        "clarity": "5",
    }

    assert calculate_final_score(row) == 4.6


def test_assign_recommendation():
    assert assign_recommendation("strong") == "ready_for_submission"
    assert assign_recommendation("acceptable") == "minor_revision"
    assert assign_recommendation("needs_revision") == "major_revision"
    assert assign_recommendation("poor") == "reject_response"