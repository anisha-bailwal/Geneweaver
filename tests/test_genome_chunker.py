import pytest

from src.genome_chunker import chunk_sequence


def test_chunk_sequence():
    chunks = chunk_sequence("ATGCATGC", 4)

    assert len(chunks) == 2
    assert chunks[0]["sequence"] == "ATGC"
    assert chunks[1]["sequence"] == "ATGC"


def test_last_incomplete_chunk():
    chunks = chunk_sequence("ATGCATG", 3)

    assert len(chunks) == 3
    assert chunks[2]["sequence"] == "G"


def test_empty_sequence():
    with pytest.raises(ValueError):
        chunk_sequence("", 5)