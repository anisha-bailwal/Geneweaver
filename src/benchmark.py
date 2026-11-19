import time
from src.alignment import needleman_wunsch


def benchmark_alignment(seq1, seq2):
    start_time = time.perf_counter()

    result = needleman_wunsch(seq1, seq2)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    return result, execution_time

def generate_dna(length):
    bases = "ATGC"
    return (bases * (length // 4 + 1))[:length]

def run_benchmarks():
    sizes = [100, 500, 1000]
    repetitions = 5

    for size in sizes:
        seq1 = generate_dna(size)
        seq2 = generate_dna(size)

        total_time = 0
        scores = []

        for run in range(repetitions):
            result, elapsed = benchmark_alignment(seq1, seq2)

            total_time += elapsed
            scores.append(result[2])

        average_time = total_time / repetitions

        print(f"Sequence Size: {size}")
        print(f"Number of Runs: {repetitions}")
        print(f"Average Execution Time: {average_time:.6f} seconds")
        print(f"Alignment Score: {scores[0]}")
        print("--------------------------")