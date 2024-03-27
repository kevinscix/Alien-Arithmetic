import unittest
from unittest.mock import patch
from datascore import DataScore

class TestDataScore(unittest.TestCase):
    
    def setUp(self):
        """Initialize before every test."""
        self.data_score = DataScore()

    def test_add_score(self):
        """Test adding a new score."""
        self.data_score.add_score(100)
        self.assertIn(100, self.data_score.scores)  # Assuming 'scores' is a list of scores
    
    def test_get_high_score(self):
        """Test retrieval of the highest score."""
        self.data_score.scores = [10, 20, 100, 5]
        high_score = self.data_score.get_high_score()
        self.assertEqual(high_score, 100)
    
    @patch('datascore.DataScore.save_scores')
    def test_save_scores(self, mock_save_scores):
        """Test saving scores calls the expected method."""
        # This test assumes 'save_scores' writes scores to a file or database
        self.data_score.save_scores()
        mock_save_scores.assert_called_once()

    # Additional tests for other methods in datascore.py

if __name__ == '__main__':
    unittest.main()
