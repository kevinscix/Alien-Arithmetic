#AndyD
from pydantic import BaseModel
from typing import Dict

#represents a single data model for a player to be filled out per user
#might be user to call this the user model

class DataScore(BaseModel):
  _name : str
  _highScore : int
  _questionsCompleted : int
  _incorrectAmt : int
  _correctAmt : int
  _overallGrade : int
  _loggedIn : bool


  def setName(self, name: str) -> None:
    self._name = name

  def setHighScore(self, score: int) -> None:
    self._highScore = score

  def setQuestionsCompleted(self, questions) -> None:
    self._questionsCompleted = questions

  # # Do we need to create these each time?
  # def getPlayer(self, player: str) -> None:

if __name__ == "__main__":
  print("Test cases for DataScore model")
