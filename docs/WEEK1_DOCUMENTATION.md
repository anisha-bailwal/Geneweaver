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

## 4. CPU Baseline Performance Benchmarking

### Objective
Measure the execution time of the Needleman-Wunsch DNA alignment algorithm using pure Python.

### Implementation
A benchmarking module was created using Python's `time.perf_counter()` function.

DNA sequences of different lengths were generated and tested. Each test was executed five times to calculate the average execution time.

### Benchmark Results

| Sequence Size | Number of Runs | Average Execution Time | Alignment Score |
|---|---:|---:|---:|
| 100 | 5 | 0.003864 seconds | 200 |
| 500 | 5 | 0.087983 seconds | 1000 |
| 1000 | 5 | 0.439384 seconds | 2000 |

### Observation
Execution time increases as the DNA sequence length increases.

The collected CPU benchmark results will serve as a baseline for future performance comparisons with GPU-based implementations.

### Conclusion
CPU baseline benchmarking was successfully completed for three different sequence sizes.