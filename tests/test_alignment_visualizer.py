
import pytest

from src.alignment_visualizer import visualize_alignment


def test_visualize_matching_sequences():
    report = visualize_alignment("ATGC", "ATGC")

    assert "Matches: 4" in report
    assert "Mismatches: 0" in report


def test_visualize_mismatching_sequences():
    report = visualize_alignment("ATGC", "ATCC")

    assert "Matches: 3" in report
    assert "Mismatches: 1" in report


def test_visualize_sequences_with_gaps():
    report = visualize_alignment("AT-GC", "ATAGC")

    assert "Gaps: 1" in report


def test_visualize_alignment_score():
    report = visualize_alignment("ATGC", "ATCC", 5)

    assert "Alignment Score: 5" in report


def test_different_length_sequences():
    with pytest.raises(ValueError):
        visualize_alignment("ATGC", "ATG")


def test_empty_sequences():
    with pytest.raises(ValueError):
        visualize_alignment("", "")


def test_alignment_report_contains_sequences():
    report = visualize_alignment("ATGC", "ATCC")

    assert "Sequence 1: ATGC" in report
    assert "Sequence 2: ATCC" in report
