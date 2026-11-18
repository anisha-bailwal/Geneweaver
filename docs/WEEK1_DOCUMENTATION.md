# GeneWeaver – Week 1 Documentation

## 1. Genome Data Pipeline

### Objective
To parse genome FASTA files using Biopython.

### Library Used
Biopython 1.88

### Implementation
The Bio.SeqIO module is used to read FASTA files
and extract sequence records.

### Validation
- Checks whether the FASTA file exists.
- Checks whether the file contains sequences.

## 2. Genome Chunking

### Objective
Divide large DNA sequences into smaller manageable chunks.

### Implementation
A custom Python function divides DNA sequences
using a configurable chunk size.

### Output
Each chunk stores:
- Starting position
- Ending position
- DNA subsequence

### Validation
- Empty sequences are rejected.
- Chunk size must be a positive integer.
### Test Cases
- Normal sequence chunking
- Last incomplete chunk handling
- Empty sequence validation

## 3. CPU-Based DNA Sequence Alignment

### Algorithm
Needleman-Wunsch Global Alignment

### Scoring Parameters
- Match Score: +2
- Mismatch Penalty: -1
- Gap Penalty: -2

### Objective
Align two DNA sequences using a pure Python implementation.