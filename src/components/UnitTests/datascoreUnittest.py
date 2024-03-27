import unittest
from datascore import DataScore

class TestDataScore(unittest.TestCase):

    def setUp(self):
        """Set up a fresh DataScore instance for each test."""
        self.data_score = DataScore()

    def test_add_score(self):
        """Test adding a score."""
        self.data_score.add_score(100)
        self.assertIn(100, self.data_score.scores)

    def test_get_high_score_empty(self):
        """Test getting high score when no scores are present."""
        self.assertEqual(self.data_score.get_high_score(), 0)

    def test_get_high_score_non_empty(self):
        """Test getting the high score correctly."""
        scores = [10, 200, 30]
        for score in scores:
            self.data_score.add_score(score)
        self.assertEqual(self.data_score.get_high_score(), 200)

    def test_clear_scores(self):
        """Test clearing all scores."""
        self.data_score.add_score(100)
        self.data_score.clear_scores()
        self.assertEqual(len(self.data_score.scores), 0)

if __name__ == '__main__':
    unittest.main()
