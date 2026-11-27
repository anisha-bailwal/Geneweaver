import pytest

from src.alignment_matrix_visualizer import (
    get_scoring_matrix,
    format_scoring_matrix,
    visualize_scoring_matrix
)


def test_scoring_matrix_dimensions():
    matrix = get_scoring_matrix("AT", "AT")

    assert len(matrix) == 3
    assert len(matrix[0]) == 3


def test_scoring_matrix_final_score():
    matrix = get_scoring_matrix("ATGC", "ATCC")

    assert matrix[-1][-1] == 5


def test_matrix_initialization():
    matrix = get_scoring_matrix("AT", "AT")

    assert matrix[0] == [0, -2, -4]
    assert matrix[1][0] == -2


def test_matrix_visualization():
    output = visualize_scoring_matrix("AT", "AT")

    assert "NEEDLEMAN-WUNSCH SCORING MATRIX" in output
    assert "Matrix Size: 3 x 3" in output


def test_matrix_contains_sequences():
    output = visualize_scoring_matrix("ATGC", "ATCC")

    assert "Sequence 1: ATGC" in output
    assert "Sequence 2: ATCC" in output


def test_format_invalid_row_count():
    with pytest.raises(ValueError):
        format_scoring_matrix("AT", "AT", [[0, 0]])


def test_format_invalid_column_count():
    with pytest.raises(ValueError):
        format_scoring_matrix("AT", "AT", [[0, 0], [0, 0], [0, 0]])