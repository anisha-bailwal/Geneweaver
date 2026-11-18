from Bio import SeqIO
from pathlib import Path


def parse_genome_fasta(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError("Genome FASTA file not found")

    records = list(SeqIO.parse(file_path, "fasta"))

    if not records:
        raise ValueError("No genome sequences found")

    return records