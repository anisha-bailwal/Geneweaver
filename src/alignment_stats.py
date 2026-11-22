def validate_alignment(aligned1, aligned2):
    if not aligned1 or not aligned2:
        raise ValueError("Aligned sequences cannot be empty")

    if len(aligned1) != len(aligned2):
        raise ValueError("Sequences must have equal length")

    if set(aligned1.upper()) - set("ATGC-"):
        raise ValueError("Invalid characters in sequence 1")

    if set(aligned2.upper()) - set("ATGC-"):
        raise ValueError("Invalid characters in sequence 2")


def calculate_alignment_stats(aligned1, aligned2):
    validate_alignment(aligned1, aligned2)

    matches = 0
    mismatches = 0
    gaps = 0

    for base1, base2 in zip(aligned1.upper(), aligned2.upper()):
        if base1 == "-" or base2 == "-":
            gaps += 1
        elif base1 == base2:
            matches += 1
        else:
            mismatches += 1

    total = len(aligned1)

    identity = (matches / total) * 100
    gap_percentage = (gaps / total) * 100
    mismatch_percentage = (mismatches / total) * 100

    return {
        "length": total,
        "matches": matches,
        "mismatches": mismatches,
        "gaps": gaps,
        "identity_percentage": round(identity, 2),
        "gap_percentage": round(gap_percentage, 2),
        "mismatch_percentage": round(mismatch_percentage, 2)
    }


def print_alignment_stats(aligned1, aligned2):
    stats = calculate_alignment_stats(aligned1, aligned2)

    print("=" * 35)
    print("       ALIGNMENT STATISTICS")
    print("=" * 35)

    print(f"Alignment Length: {stats['length']}")
    print(f"Matches: {stats['matches']}")
    print(f"Mismatches: {stats['mismatches']}")
    print(f"Gaps: {stats['gaps']}")

    print("-" * 35)
    print(f"Sequence Identity: {stats['identity_percentage']}%")
    print(f"Mismatch Percentage: {stats['mismatch_percentage']}%")
    print(f"Gap Percentage: {stats['gap_percentage']}%")
    print("=" * 35)


if __name__ == "__main__":
    sequence1 = "ATGCTAGC"
    sequence2 = "ATGATAGC"

    print_alignment_stats(sequence1, sequence2)