from components.datascore import SaveModel
from pydantic import BaseModel
from typing import Dict, Optional, List
from Interface.state_machine import State, DisplayEngine
import json
import os
import unittest

#model representation of what the scoreboard 
class Scoreboard(BaseModel):

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
    if self.userType == 1:
      return True

  def isInstructor(self):
    if self.userType == 0:
      return True
    
  def showScores(self):
    for name, score in self.board.items():
      print(f"Name: {name}, Score: {score}")

  def getPlayer(self, name : str) -> SaveModel:
        score = self.board.get(name)
        if score:
            print(score)
        else:
            print(f"No player with the name {name} found.")
        return score

class ScoreboardState(State):
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
        src_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Path to the 'src' directory
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
        top_scores = self.scores[:5]

        if self.current_player_score and self.current_player_score not in top_scores:
            top_scores.append(self.current_player_score)

        return top_scores

    def display_leaderboard(self, screen):
        leaderboard = self.get_leaderboard()
        x = 20
        y = 20
        for i, score in enumerate(leaderboard, start=1):
            text = f"{i}. {score.name} - Score: {score.score}"
            text_surface = self.font.render(text, True, (255, 255, 255))
            screen.blit(text_surface, (x, y))
            y += self.font.get_height() + 10

    def on_draw(self, surface):
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
    def setUp(self):
        self.board = Scoreboard()

    def test_isPlayer_True(self):
        self.board.userType = 1
        self.assertTrue(self.board.isPlayer(), "isPlayer should return True for userType 1")

    def test_isInstructor_True(self):
        self.board.userType = 0
        self.assertTrue(self.board.isInstructor(), "isInstructor should return True for userType 0")

    def test_getPlayer_Found(self):
        test_player = SaveModel(name="Test", score=100)
        self.board.board = {"Test": test_player}
        result = self.board.getPlayer("Test")
        self.assertIsNotNone(result, "getPlayer should return a player when the name matches")
        self.assertEqual(result.name, "Test", "getPlayer returned incorrect player details")

if __name__ == '__main__':
    unittest.main()
