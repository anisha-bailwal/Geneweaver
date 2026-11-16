
def calculate_length(sequence):
    return len(sequence)


def count_bases(sequence):
    sequence = sequence.upper()
    if not sequence:
        raise ValueError("DNA sequence cannot be empty")
    valid_bases = {"A", "T", "G", "C"}
    if set(sequence) - valid_bases:
       raise ValueError("Invalid DNA sequence")

    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }


def calculate_gc_content(sequence):
    sequence = sequence.upper()

    if not sequence:
        raise ValueError("DNA sequence cannot be empty")

    gc_count = sequence.count("G") + sequence.count("C")

    return (gc_count / len(sequence)) * 100
