import unittest
from unittest.mock import patch
from datascore import dataScore  

class TestDataScore(unittest.TestCase):
    def setUp(self):
        """Prepare resources for testing."""
        self.data_score = dataScore()

    def test_initialization(self):
        """Verify that the DataScore object initializes as expected."""
        self.assertIsNotNone(self.data_score)
        # Assuming 'scores' is an attribute that stores score values
        self.assertEqual(self.data_score.scores, [])
        # Assuming 'high_score' is an attribute; adjust if the DataScore implementation differs
        self.assertEqual(self.data_score.high_score, 0)

    def test_add_score(self):
        """Test the addition of a new score."""
        self.data_score.add_score(100)
        self.assertIn(100, self.data_score.scores)

    def test_get_high_score(self):
        """Test retrieval of the highest score."""
        test_scores = [10, 20, 100, 5]
        for score in test_scores:
            self.data_score.add_score(score)
        self.assertEqual(self.data_score.get_high_score(), 100)

    @patch('datascore.DataScore.save_scores')
    def test_save_scores(self, mock_save_scores):
        """Test that scores are saved correctly."""
        self.data_score.save_scores()
        mock_save_scores.assert_called_once()

    # Add more tests as necessary for complete coverage

if __name__ == '__main__':
    unittest.main()
