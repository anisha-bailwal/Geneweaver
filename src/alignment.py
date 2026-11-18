MATCH_SCORE = 2
MISMATCH_PENALTY = -1
GAP_PENALTY = -2

def create_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        matrix.append([0] * cols)

    return matrix

def initialize_matrix(matrix, rows, cols):
    for i in range(rows):
        matrix[i][0] = i * GAP_PENALTY

    for j in range(cols):
        matrix[0][j] = j * GAP_PENALTY

    return matrix

def calculate_score(base1, base2):
    if base1 == base2:
        return MATCH_SCORE

    return MISMATCH_PENALTY

def fill_matrix(seq1, seq2, matrix):
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):

            diagonal = matrix[i-1][j-1] + calculate_score(seq1[i-1], seq2[j-1])

            up = matrix[i-1][j] + GAP_PENALTY

            left = matrix[i][j-1] + GAP_PENALTY

            matrix[i][j] = max(diagonal, up, left)

    return matrix

def traceback(seq1, seq2, matrix):
    aligned1 = ""
    aligned2 = ""

    i = len(seq1)
    j = len(seq2)

    while i > 0 or j > 0:

        if i > 0 and j > 0 and matrix[i][j] == matrix[i-1][j-1] + calculate_score(seq1[i-1], seq2[j-1]):
            aligned1 = seq1[i-1] + aligned1
            aligned2 = seq2[j-1] + aligned2
            i -= 1
            j -= 1

        elif i > 0 and matrix[i][j] == matrix[i-1][j] + GAP_PENALTY:
            aligned1 = seq1[i-1] + aligned1
            aligned2 = "-" + aligned2
            i -= 1

        else:
            aligned1 = "-" + aligned1
            aligned2 = seq2[j-1] + aligned2
            j -= 1

    return aligned1, aligned2

def needleman_wunsch(seq1, seq2):
    rows = len(seq1) + 1
    cols = len(seq2) + 1

    matrix = create_matrix(rows, cols)

    initialize_matrix(matrix, rows, cols)

    fill_matrix(seq1, seq2, matrix)

    aligned1, aligned2 = traceback(seq1, seq2, matrix)

    final_score = matrix[rows - 1][cols - 1]

    return aligned1, aligned2, final_score
