
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DNASequence:
    sequence_id: str
    sequence: str


VALID_BASES = {"A", "T", "G", "C"}


def validate_sequence(sequence):
    sequence = sequence.upper()

    if not sequence:
        raise ValueError("DNA sequence cannot be empty")

    invalid_bases = set(sequence) - VALID_BASES

    if invalid_bases:
        raise ValueError(
            f"Invalid DNA bases found: {invalid_bases}"
        )

    return sequence


def parse_fasta(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"FASTA file not found: {file_path}"
        )

    sequences = []
    current_id = None
    current_sequence = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if current_id is not None:
                    sequence = validate_sequence(
                        "".join(current_sequence)
                    )
                    sequences.append(
                        DNASequence(current_id, sequence)
                    )

                current_id = line[1:].split()[0]
                current_sequence = []

            else:
                if current_id is None:
                    raise ValueError("FASTA header missing")

                current_sequence.append(line)

    if current_id is not None:
        sequence = validate_sequence(
            "".join(current_sequence)
        )
        sequences.append(
            DNASequence(current_id, sequence)
        )

    if not sequences:
        raise ValueError("No DNA sequences found in file")

    return sequences


if __name__ == "__main__":
    fasta_file = "data/sample_sequences.fasta"

    records = parse_fasta(fasta_file)

    print("GeneWeaver FASTA Parser")
    print("----------------------")
    print(f"Total sequences: {len(records)}")

    for record in records:
        print(f"{record.sequence_id}: {record.sequence}")
