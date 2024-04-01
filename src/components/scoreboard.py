import os
import sys
import json
import unittest
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from components.datascore import SaveModel
from pydantic import BaseModel
from typing import Dict, Optional, List
from Interface.state_machine import State, DisplayEngine

#model representation of what the scoreboard 
class Scoreboard(BaseModel):
  """
    Represents a scoreboard for tracking player scores within the game. 

    Attributes:
        numberPlayer (Optional[int]): Total number of players.
        userType (Optional[int]): Type of user, where 1 represents a player and 0 an instructor.
        score (Optional[int]): The current player's score.
        board (Dict[str, SaveModel]): A dictionary mapping player names to their SaveModel instances.
    """

  #total players
  numberPlayer : Optional[int] = None
  userType : Optional[int] = None

  #current player
  score : Optional[int] = None

  #currentPlayer : SaveModel
  board : Optional[SaveModel] = None

  # currentPlayer : SaveModel --
  board : Dict[str, SaveModel] = {}

  #returns 0 if user is true or 1 if user is false 
  def isPlayer(self):
    """Checks if the current user is a player."""
    if self.userType == 1:
      return True

  def isInstructor(self):
    """Checks if the current user is an instructor."""
    if self.userType == 0:
      return True
    
  def showScores(self):
    """Prints the names and scores of all players in the scoreboard."""
    for name, score in self.board.items():
      print(f"Name: {name}, Score: {score}")

  def getPlayer(self, name : str) -> SaveModel:
    """
    Retrieves a player's SaveModel by name.

    Args:
        name (str): The name of the player.

    Returns:
        Optional[SaveModel]: The SaveModel of the player if found, otherwise None.
    """
    score = self.board.get(name)
    if score:
        print(score)
    else:
        print(f"No player with the name {name} found.")
    return score

class ScoreboardState(State):
    """
    Represents the state in the game where the scoreboard is displayed.

    Attributes:
        engine (DisplayEngine): The game engine instance.
        scores (List[SaveModel]): A list of all player scores.
        current_player_score (Optional[SaveModel]): The current player's score, if available.
    """
    def __init__(self, engine):
        super().__init__(engine)
        self.scores = []
        self.current_player_score = None
        self.load_scores()
        self.isPlayer()
        self.isInstructor()
        self.getPlayer()

    def isPlayer(self) -> bool:
        return self.engine.current_player_type == "player"

    def isInstructor(self) -> bool:
       
        return self.engine.current_player_type == "instructor"

    def getPlayer(self, name: str) -> Optional[SaveModel]:
        for score in self.scores:
            if score.name == name:
                return score
        return None

    def load_scores(self):
        """Loads player scores from saved files into the scoreboard."""
        src_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  
        database = []

        for root, dirs, files in os.walk(os.path.join(src_dir, 'saves/')):
            for file in files:
                if file.endswith(".txt"):
                    try:
                        with open(os.path.join(root, file), 'r') as f:
                            score_data = json.load(f)
                        data_score = SaveModel(**score_data)
                        database.append(data_score)
                        if data_score.name == self.engine.current_player:
                            self.current_player_score = data_score
                    except Exception as e:
                        print(f"Error loading file {file}: {e}")

        self.scores = sorted(database, key=lambda x: x.score, reverse=True)

    def get_leaderboard(self):
        """
        Retrieves the top scores for display on the leaderboard.

        Returns:
            List[SaveModel]: A list of top player scores.
        """
        top_scores = self.scores[:5]

        if self.current_player_score and self.current_player_score not in top_scores:
            top_scores.append(self.current_player_score)

        return top_scores

    def display_leaderboard(self, screen):
        """
        Renders the leaderboard on the provided screen.

        Args:
            screen: The screen or surface to render the leaderboard on.
        """
        leaderboard = self.get_leaderboard()
        x = 20
        y = 20
        for i, score in enumerate(leaderboard, start=1):
            text = f"{i}. {score.name} - Score: {score.score}"
            text_surface = self.font.render(text, True, (255, 255, 255))
            screen.blit(text_surface, (x, y))
            y += self.font.get_height() + 10

    def on_draw(self, surface):
        """
        Draws the state's UI elements onto the given surface.

        Args:
            surface: The surface to draw the UI elements on.
        """
        # Draw the background image
        surface.blit(self.scoreboardImage, (0, 0))
        # Draw the leaderboard
        self.display_leaderboard(surface)
        # Draw buttons
        self.btn_level_select.draw(surface, 275, 500)
        self.btn_back.draw(surface, 0, 500)
        pygame.display.flip()


#unit testing
class TestScoreboard(unittest.TestCase):
    """
    A set of unit tests for the Scoreboard class.
    """
    def setUp(self):
        """Sets up the test environment before each test."""
        self.board = Scoreboard()

    def test_isPlayer_True(self):
        """Tests that isPlayer returns True when userType is set to 1."""
        self.board.userType = 1
        self.assertTrue(self.board.isPlayer(), "isPlayer should return True for userType 1")

    def test_isInstructor_True(self):
        """Tests that isInstructor returns True when userType is set to 0."""
        self.board.userType = 0
        self.assertTrue(self.board.isInstructor(), "isInstructor should return True for userType 0")

    def test_getPlayer_NotFound(self):
        """Tests that getPlayer returns None when the name does not match any player."""
        self.board.board = {"Emily": SaveModel(name="Emily", score=100, level=[1], questionsCompleted=10, correctAmt=8)}
        result = self.board.getPlayer("NonExistentPlayer")
        self.assertIsNone(result, "getPlayer should return None for a non-existent player")

    def test_getPlayer_InvalidName(self):
        """Tests that getPlayer handles invalid names gracefully."""
        self.board.board = {"ValidName": SaveModel(name="ValidName", score=65, level=[1], questionsCompleted=10, correctAmt=5)}
        result = self.board.getPlayer("")
        self.assertIsNone(result, "getPlayer should return None for invalid player names")

    def test_getPlayer_WithMultiplePlayers(self):
        """Tests that getPlayer accurately retrieves the correct player among multiple."""
        player_one = SaveModel(name="Emily", score=80, level=[2], questionsCompleted=15, correctAmt=12)
        player_two = SaveModel(name="Kevin", score=90, level=[3], questionsCompleted=20, correctAmt=18)
        self.board.board = {"Emily": player_one, "Kevin": player_two}
        result = self.board.getPlayer("Kevin")
        self.assertIsNotNone(result, "getPlayer should accurately retrieve a player among multiple")
        self.assertEqual(result.name, "Kevin", "getPlayer returned the wrong player details among multiple players")


if __name__ == '__main__':
    unittest.main()
