
import unittest
from pathlib import Path

from src.fasta_parser import parse_fasta, validate_sequence


class TestFastaParser(unittest.TestCase):

    def test_valid_sequence(self):
        result = validate_sequence("ATGC")
        self.assertEqual(result, "ATGC")

    def test_lowercase_sequence(self):
        result = validate_sequence("atgc")
        self.assertEqual(result, "ATGC")

    def test_invalid_sequence(self):
        with self.assertRaises(ValueError):
            validate_sequence("ATGX")

    def test_empty_sequence(self):
        with self.assertRaises(ValueError):
            validate_sequence("")

    def test_parse_multiple_sequences(self):
        test_file = Path("tests/temp.fasta")

        test_file.write_text(
            ">seq1\nATGC\n>seq2\nGCTA\n"
        )

        try:
            records = parse_fasta(test_file)

            self.assertEqual(len(records), 2)
            self.assertEqual(records[0].sequence_id, "seq1")
            self.assertEqual(records[1].sequence, "GCTA")

        finally:
            test_file.unlink(missing_ok=True)

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            parse_fasta("tests/missing.fasta")

    def test_duplicate_sequence_ids(self):
        test_file = Path("tests/temp_duplicate.fasta")

        test_file.write_text(
            ">seq1\nATGC\n>seq1\nGCTA\n"
        )

        try:
            with self.assertRaisesRegex(
                ValueError, "Duplicate sequence ID"
            ):
                parse_fasta(test_file)

        finally:
            test_file.unlink(missing_ok=True)


    def test_missing_header(self):
        test_file = Path("tests/temp_no_header.fasta")

        test_file.write_text("ATGC\nGCTA\n")

        try:
           with self.assertRaisesRegex(ValueError, "FASTA header missing"):
            parse_fasta(test_file)

        finally:
           test_file.unlink(missing_ok=True)

    def test_empty_sequence_id(self):
        test_file = Path("tests/temp_empty_id.fasta")

        test_file.write_text(">\nATGC\n")

        try:
           with self.assertRaisesRegex(
              ValueError, "Sequence ID cannot be empty"
        ):
            parse_fasta(test_file)

        finally:
            test_file.unlink(missing_ok=True)  

    
    def test_empty_fasta_sequence(self):
        test_file = Path("tests/temp_empty_sequence.fasta")

        test_file.write_text(">seq1\n")

        try:
           with self.assertRaisesRegex(
            ValueError, "DNA sequence cannot be empty"
        ):
            parse_fasta(test_file)

        finally:
           test_file.unlink(missing_ok=True)             

    
    def test_empty_sequence_before_next_header(self):
        test_file = Path("tests/temp_empty_before_next.fasta")

        test_file.write_text(
            ">seq1\n>seq2\nATGC\n"
        )

        try:
            with self.assertRaisesRegex(
                ValueError, "DNA sequence cannot be empty"
            ):
                parse_fasta(test_file)

        finally:
            test_file.unlink(missing_ok=True)

if __name__ == "__main__":
    unittest.main()

