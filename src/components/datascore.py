#AndyD
from pydantic import BaseModel
from typing import Dict

#represents a single data model for a player to be filled out per user
#might be user to call this the user model

class DataScore(BaseModel):
  name : str
  highScore : int
  questionsCompleted : int
  incorrectAmt : int
  correctAmt : int
  overallGrade : int
  loggedIn : bool


  def setName(self, name: str) -> None:
    self.name = name

  def setHighScore(self, score: int) -> None:
    self.highScore = score

  def setQuestionsCompleted(self, questions) -> None:
    self.questionsCompleted = questions


  def fields(self) -> list:
    fields = list()
    fields.append(self.name)
    fields.append(self.highScore)
    fields.append(self.questionsCompleted)
    fields.append(self.incorrectAmt)
    fields.append(self.correctAmt)
    fields.append(self.overallGrade)
    fields.append(self.loggedIn)
    return fields
  # # Do we need to create these each time?
  # def getPlayer(self, player: str) -> None:

if __name__ == "__main__":
  print("Test cases for DataScore model")
  AndyScore = DataScore(
    name="Andy",
    highScore=100,
    questionsCompleted=5,
    incorrectAmt=10,
    correctAmt=30,
    overallGrade=40,
    loggedIn=True
  )

  print(AndyScore.fields())
