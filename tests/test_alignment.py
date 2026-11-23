import pytest

from src.alignment import (
    create_matrix,
    initialize_matrix,
    calculate_score,
    fill_matrix,
    traceback,
    needleman_wunsch
)


def test_create_matrix():
    matrix = create_matrix(3, 4)

    assert len(matrix) == 3
    assert len(matrix[0]) == 4
    assert matrix[0][0] == 0


def test_initialize_matrix():
    matrix = create_matrix(3, 3)
    initialize_matrix(matrix, 3, 3)

    assert matrix[0] == [0, -2, -4]
    assert matrix[1][0] == -2
    assert matrix[2][0] == -4


def test_calculate_match_score():
    assert calculate_score("A", "A") == 2


def test_calculate_mismatch_score():
    assert calculate_score("A", "T") == -1


def test_fill_matrix():
    matrix = create_matrix(3, 3)
    initialize_matrix(matrix, 3, 3)

    result = fill_matrix("AT", "AT", matrix)

    assert result[2][2] == 4


def test_traceback():
    matrix = create_matrix(3, 3)
    initialize_matrix(matrix, 3, 3)
    fill_matrix("AT", "AT", matrix)

    aligned1, aligned2 = traceback("AT", "AT", matrix)

    assert aligned1 == "AT"
    assert aligned2 == "AT"


def test_identical_sequences():
    aligned1, aligned2, score = needleman_wunsch("ATGC", "ATGC")

    assert aligned1 == "ATGC"
    assert aligned2 == "ATGC"
    assert score == 8


def test_mismatching_sequences():
    aligned1, aligned2, score = needleman_wunsch("ATGC", "ATCC")

    assert len(aligned1) == len(aligned2)
    assert score == 5


def test_different_length_sequences():
    aligned1, aligned2, score = needleman_wunsch("ATG", "ATGC")

    assert len(aligned1) == len(aligned2)
    assert isinstance(score, int)


def test_empty_sequences():
    aligned1, aligned2, score = needleman_wunsch("", "")

    assert aligned1 == ""
    assert aligned2 == ""
    assert score == 0


def test_one_empty_sequence():
    aligned1, aligned2, score = needleman_wunsch("AT", "")

    assert aligned1 == "AT"
    assert aligned2 == "--"
    assert score == -4


def test_alignment_with_gap():
    aligned1, aligned2, score = needleman_wunsch("ATGC", "ATC")

    assert len(aligned1) == len(aligned2)
    assert "-" in aligned1 or "-" in aligned2