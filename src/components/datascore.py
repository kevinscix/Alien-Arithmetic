#AndyD
from pydantic import BaseModel
from typing import Dict
import unittest

#represents a single data model for a player to be filled out per user

class DataScore(BaseModel):
  name : str
  high_score : int
  questions_completed : int
  incorrect_amt : int
  correct_amt : int
  overall_grade : int
  logged_in : bool


  def set_name(self, name: str) -> None:
    self.name = name

  def set_high_score(self, score: int) -> None:
    self.high_score = score

  def set_questions_completed(self, questions) -> None:
    self.questions_completed = questions


  def fields(self) -> list:
    fields = list()
    fields.append(self.name)
    fields.append(self.high_score)
    fields.append(self.questions_completed)
    fields.append(self.incorrect_amt)
    fields.append(self.correct_amt)
    fields.append(self.overall_grade)
    fields.append(self.logged_in)
    return fields

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
         self.data.set_name("Jackson")
         self.assertEqual(self.data.name, "Jackson", "name is not set")
      
      def test_setHighScore(self):
         self.data.set_high_score(10)
         self.assertEqual(self.data.highScore, 10, "high score not changed")
      
      def test_setQuestionsCompleted(self):
         self.data.set_questions_completed(10)
         self.assertEqual(self.data.questions_completed, 10, "questions completed not updated")

  unittest.main()