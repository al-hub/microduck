"""Acceptance tests for the isolated score-band agent experiment."""
import unittest
from score_band import score_band

class ScoreBandTests(unittest.TestCase):
    def test_boundaries(self):
        for score, expected in [(0,"low"),(39,"low"),(40,"mid"),(69,"mid"),(70,"high"),(100,"high")]:
            with self.subTest(score=score):
                self.assertEqual(score_band(score), expected)

    def test_range_errors(self):
        for score in [-1, 101]:
            with self.subTest(score=score):
                with self.assertRaises(ValueError):
                    score_band(score)

    def test_type_errors(self):
        for score in ["40", None, True, False, 40.0]:
            with self.subTest(score=repr(score)):
                with self.assertRaises(TypeError):
                    score_band(score)

if __name__ == "__main__":
    unittest.main()
