from src.alignment import (
    create_matrix,
    initialize_matrix,
    fill_matrix
)


def get_scoring_matrix(seq1, seq2):
    rows = len(seq1) + 1
    cols = len(seq2) + 1

    matrix = create_matrix(rows, cols)
    initialize_matrix(matrix, rows, cols)
    fill_matrix(seq1, seq2, matrix)

    return matrix


def format_scoring_matrix(seq1, seq2, matrix):
    if len(matrix) != len(seq1) + 1:
        raise ValueError("Matrix row count does not match sequence 1")

    if any(len(row) != len(seq2) + 1 for row in matrix):
        raise ValueError("Matrix column count does not match sequence 2")

    cell_width = max(
        4,
        max(len(str(value)) for row in matrix for value in row) + 2
    )

    header = [" "] + ["-"] + list(seq2)

    output = []
    output.append("NEEDLEMAN-WUNSCH SCORING MATRIX")
    output.append("=" * (cell_width * len(header)))

    output.append("".join(
        str(item).rjust(cell_width) for item in header
    ))

    for i, row in enumerate(matrix):
        label = "-" if i == 0 else seq1[i - 1]

        output.append(
            str(label).rjust(cell_width)
            + "".join(
                str(value).rjust(cell_width)
                for value in row
            )
        )

    output.append("=" * (cell_width*len(header)))
    output.append(f"Matrix Size: {len(matrix)} x {len(matrix[0])}")
    output.append(f"Sequence 1: {seq1}")
    output.append(f"Sequence 2: {seq2}")

    return "\n".join(output)


def visualize_scoring_matrix(seq1, seq2):
    matrix = get_scoring_matrix(seq1, seq2)
    return format_scoring_matrix(seq1, seq2, matrix)


if __name__ == "__main__":
    sequence1 = "ATGC"
    sequence2 = "ATCC"

    print(visualize_scoring_matrix(sequence1, sequence2))