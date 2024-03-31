#AndyD
from pydantic import BaseModel
from typing import Dict
import unittest

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

# automated testing

  class test_datascore(unittest.TestCase):
      def setUp(self):
          self.data = DataScore(
               name="Andy",
               highScore=100,
               questionsCompleted=5,
               incorrectAmt=10,
               correctAmt=30,
               overallGrade=40,
               loggedIn=True
              )
      def test_setName(self):
         self.data.setName("Jackson")
         self.assertEqual(self.data.name, "Jackson", "name is not set")
      
      def test_setHighScore(self):
         self.data.setHighScore(10)
         self.assertEqual(self.data.highScore, 10, "high score not changed")
      
      def test_setQuestionsCompleted(self):
         self.data.setQuestionsCompleted(10)
         self.assertEqual(self.data.questionsCompleted, 10, "questions completed not updated")

  unittest.main()