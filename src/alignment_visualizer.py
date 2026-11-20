
def visualize_alignment(aligned1, aligned2, alignment_score=None):
    if len(aligned1) != len(aligned2):
        raise ValueError("Aligned sequences must have equal length")

    if not aligned1:
        raise ValueError("Aligned sequences cannot be empty")

    match_line = ""
    matches = 0
    mismatches = 0
    gaps = 0

    for base1, base2 in zip(aligned1, aligned2):

        if base1 == "-" or base2 == "-":
            match_line += " "
            gaps += 1

        elif base1 == base2:
            match_line += "|"
            matches += 1

        else:
            match_line += "."
            mismatches += 1

    report = [
        "================================",
        "       DNA ALIGNMENT REPORT",
        "================================",
        f"Sequence 1: {aligned1}",
        f"             {match_line}",
        f"Sequence 2: {aligned2}",
        "--------------------------------",
        f"Matches: {matches}",
        f"Mismatches: {mismatches}",
        f"Gaps: {gaps}",
    ]

    if alignment_score is not None:
        report.append(f"Alignment Score: {alignment_score}")

    report.append("================================")

    return "\n".join(report)
