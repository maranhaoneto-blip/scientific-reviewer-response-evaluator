from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.evaluate_responses import (
    assign_adequacy_decision,
    assign_evaluation_summary,
    assign_label,
    assign_ready_to_send,
    assign_recommendation,
    calculate_final_score,
    identify_main_issue,
    suggest_fix,
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


def test_assign_adequacy_decision():
    assert assign_adequacy_decision("strong") == "adequate"
    assert assign_adequacy_decision("acceptable") == "adequate_with_minor_edits"
    assert assign_adequacy_decision("needs_revision") == "not_ready"
    assert assign_adequacy_decision("poor") == "not_adequate"


def test_assign_ready_to_send():
    assert assign_ready_to_send("strong") == "yes"
    assert assign_ready_to_send("acceptable") == "conditional"
    assert assign_ready_to_send("needs_revision") == "no"
    assert assign_ready_to_send("poor") == "no"


def test_assign_evaluation_summary():
    assert "ready for submission" in assign_evaluation_summary("strong")
    assert "minor improvements" in assign_evaluation_summary("acceptable")
    assert "substantive revision" in assign_evaluation_summary("needs_revision")
    assert "incomplete" in assign_evaluation_summary("poor")


def test_identify_main_issue():
    row = {
        "completeness": "5",
        "scientific_accuracy": "5",
        "tone": "4",
        "actionability": "2",
        "clarity": "3",
    }

    assert identify_main_issue(row) == "unclear_revision_or_missing_manuscript_change"


def test_identify_main_issue_no_major_issue():
    row = {
        "completeness": "5",
        "scientific_accuracy": "5",
        "tone": "5",
        "actionability": "5",
        "clarity": "5",
    }

    assert identify_main_issue(row) == "no_major_issue"


def test_identify_main_issue_minor_issue():
    row = {
        "completeness": "5",
        "scientific_accuracy": "5",
        "tone": "5",
        "actionability": "4",
        "clarity": "5",
    }

    assert identify_main_issue(row) == "minor_specificity_or_traceability_issue"


def test_suggest_fix():
    fix = suggest_fix("incomplete_response")
    assert "Address every part" in fix
