import pytest

from src.alignment_stats import (
    calculate_alignment_stats,
    validate_alignment
)


def test_perfect_match():
    stats = calculate_alignment_stats("ATGC", "ATGC")
    assert stats["matches"] == 4
    assert stats["identity_percentage"] == 100.0


def test_mismatch():
    stats = calculate_alignment_stats("ATGC", "ATCC")
    assert stats["mismatches"] == 1
    assert stats["identity_percentage"] == 75.0


def test_gap_count():
    stats = calculate_alignment_stats("AT-GC", "ATAGC")
    assert stats["gaps"] == 1
    assert stats["gap_percentage"] == 20.0


def test_alignment_length():
    stats = calculate_alignment_stats("ATGC", "ATGC")
    assert stats["length"] == 4


def test_empty_sequence():
    with pytest.raises(ValueError):
        calculate_alignment_stats("", "")


def test_different_lengths():
    with pytest.raises(ValueError):
        calculate_alignment_stats("ATGC", "ATG")


def test_invalid_character():
    with pytest.raises(ValueError):
        calculate_alignment_stats("ATGX", "ATGC")


def test_mismatch_percentage():
    stats = calculate_alignment_stats("AAAA", "AAAT")
    assert stats["mismatch_percentage"] == 25.0