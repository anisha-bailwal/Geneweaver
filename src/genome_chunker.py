def chunk_sequence(sequence, chunk_size=1000):
    if not sequence:
        raise ValueError("DNA sequence cannot be empty")

    if not isinstance(chunk_size, int) or chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer")

    chunks = []

    for start in range(0, len(sequence), chunk_size):
        end = start + chunk_size

        chunks.append({
            "start": start,
            "end": min(end, len(sequence)),
            "sequence": sequence[start:end]
        })

    return chunks