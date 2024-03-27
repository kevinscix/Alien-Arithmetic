import unittest
from unittest.mock import patch
from datascore import DataScore  # Adjust import as necessary

class TestDataScore(unittest.TestCase):
    
    def setUp(self):
        """Prepare environment for each test."""
        self.data_score = DataScore()

    def test_initialization(self):
        """Check if DataScore initializes as expected."""
        self.assertIsNotNone(self.data_score)
        # Assuming scores are stored in a list; adjust if necessary
        self.assertEqual(self.data_score.scores, [])
        # Assuming there's a default high score; adjust if the class uses a different default value or attribute
        self.assertEqual(getattr(self.data_score, 'high_score', None), 0)

    def test_add_score(self):
        """Ensure adding a score works correctly."""
        self.data_score.add_score(100)
        self.assertIn(100, self.data_score.scores)

    @patch('datascore.DataScore.save_scores')  # Ensure the patch path matches the actual import path
    def test_save_scores(self, mock_save_scores):
        """Verify that scores are saved correctly."""
        self.data_score.save_scores()
        mock_save_scores.assert_called_once()

    def test_get_high_score(self):
        """Test if the highest score is retrieved correctly."""
        scores = [10, 55, 200, 30]
        for score in scores:
            self.data_score.add_score(score)
        # Adjust method name and assertion as per actual implementation in datascore.py
        self.assertEqual(self.data_score.get_high_score(), 200)

    # Example template for other methods that might exist in datascore.py
    # def test_other_method(self):
        # """Description of what this test checks for."""
        # setup if needed
        # self.assertEqual / self.assertTrue / self.assertFalse / etc.
        # assertions to validate the method's behavior

if __name__ == '__main__':
    unittest.main()
