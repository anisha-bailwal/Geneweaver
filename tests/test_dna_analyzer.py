
import unittest

from src.dna_analyzer import calculate_length , count_bases , calculate_gc_content


class TestDNAAnalyzer(unittest.TestCase):

    def test_calculate_length(self):
        result = calculate_length("ATGC")
        self.assertEqual(result, 4)

    def test_count_bases(self):
            result = count_bases("AATGCC")

            expected = {
                "A": 2,
                "T": 1,
                "G": 1,
                "C": 2
          }

            self.assertEqual(result, expected)

    def test_calculate_gc_content(self):
            result = calculate_gc_content("AATTGGCC")
            self.assertEqual(result, 50.0)  

    def test_empty_sequence_gc_content(self):
            with self.assertRaises(ValueError):
             calculate_gc_content("")   

    def test_empty_sequence_base_count(self):
            with self.assertRaises(ValueError):
             count_bases("")  

    def test_invalid_dna_sequence(self):
            with self.assertRaises(ValueError):
             count_bases("ATGX")                           

if __name__ == "__main__":
    unittest.main()
