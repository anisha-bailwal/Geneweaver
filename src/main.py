from src.fasta_parser import parse_fasta

from src.dna_analyzer import (
    calculate_length,
    count_bases,
    calculate_gc_content
)
fasta_file = "data/sample_sequences.fasta"

records = parse_fasta(fasta_file)
print("================================")
print("       GENEWEAVER REPORT")
print("================================")
print(f"Total sequences: {len(records)}")
for record in records:
    length = calculate_length(record.sequence)
    bases = count_bases(record.sequence)
    gc_content = calculate_gc_content(record.sequence)

    print("\n----------------------------")
    print(f"Sequence ID: {record.sequence_id}")
    print(f"Length: {length}")
    print(f"Base Count: {bases}")
    print(f"GC Content: {gc_content:.2f}%")