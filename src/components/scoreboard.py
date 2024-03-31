#Emily & Andy
from components.datascore import SaveModel
from pydantic import BaseModel
from typing import Dict, Optional, List
from Interface.state_machine import State, DisplayEngine
import json
import os
import unittest


#we should clarify the logic for this file, it doesnt really make senses now
#I reread what we wrote here

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

  # def showScores(self):
  #   print(self.board)

  def getPlayer(self, name : str) -> SaveModel:
        score = self.board.get(name)
        if score:
            print(score)
        else:
            print(f"No player with the name {name} found.")
        return score

  # def getPlayer(self, name : str) -> SaveModel:
  #   score = self.board[name]
  #   print(score)
  #   return score

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

# class TestScoreboard(unittest.TestCase):

#     def setUp(self):
#         # Initialize the Scoreboard object
#         self.scoreboard = Scoreboard()

#     def test_initialization(self):
#         # Test that the Scoreboard is initialized with default values
#         self.assertIsNone(self.scoreboard.numberPlayer, "numberPlayer should initially be None")
#         self.assertIsNone(self.scoreboard.userType, "userType should initially be None")

#     def test_add_score(self):
#         # Assuming there's a method to add a score which we'll need to define based on actual implementation
#         pass

#     def test_get_player_info(self):
#         # Assuming there's a method to get player information which we'll need to define based on actual implementation
#         pass

# if __name__ == "__main__":
#     unittest.main()
    
class TestScoreboard(unittest.TestCase):

    def setUp(self):
        # Initialize the Scoreboard object
        self.scoreboard = Scoreboard()
        # Assuming the Scoreboard class can handle multiple players, represented in some form of collection

    def test_initialization(self):
        # Test that the Scoreboard is initialized properly
        self.assertIsInstance(self.scoreboard, Scoreboard, "Scoreboard instance is not created correctly")

    def test_add_score(self):
        # Test adding a score for a new player
        self.scoreboard.add_score("Emily", 100)
        player_info = self.scoreboard.get_player_info("Emily")
        self.assertEqual(player_info['score'], 100, "Score for Emily was not added correctly")

        # Test updating the score for an existing player
        self.scoreboard.add_score("Emily", 150)
        updated_info = self.scoreboard.get_player_info("Emily")
        self.assertEqual(updated_info['score'], 150, "Score for Emily was not updated correctly")

    def test_get_player_info(self):
        # Test retrieving player information
        self.scoreboard.add_score("Bob", 200)
        bob_info = self.scoreboard.get_player_info("Bob")
        self.assertEqual(bob_info['score'], 200, "Failed to retrieve correct score for Bob")

    def test_remove_player(self):
        # Testing the method to remove a player
        self.scoreboard.add_score("Emily", 50)
        self.scoreboard.remove_player("Emily")
        with self.assertRaises(KeyError):
            self.scoreboard.get_player_info("Emily")

    def test_list_scores(self):
        # Testing the method to list all scores
        self.scoreboard.add_score("Emily", 100)
        self.scoreboard.add_score("Bob", 200)
        scores = self.scoreboard.list_scores()
        self.assertIn(("Emily", 100), scores, "Alice's score is not listed correctly")
        self.assertIn(("Bob", 200), scores, "Bob's score is not listed correctly")

if __name__ == "__main__":
    unittest.main()