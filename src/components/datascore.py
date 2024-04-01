from pydantic import BaseModel
from typing import List
import unittest

#represents a single data model for a player to be filled out per user
#might be user to call this the user model
class SaveModel(BaseModel):
    name : str
    score : int
    level : List[int]
    #question
    questionsCompleted : int #
    correctAmt : int #

    def addOneCorrect(self):
      """
      Increments the number of correct answers by one.
      """
      self.correctAmt += 1

    def addOneQuestion(self):
      """
      Increments the number of questions completed by one.
      """
      self.questionsCompleted += 1

    def setName(self, name: str) -> None:
      """
        Sets the name of the player.
      Args:
        name (str): Name of the player.
      """
      self.name = name

    def setQuestionsCompleted(self, questions) -> None:
      """
        Sets the number of questions completed by the player.
        Args:
            questions (int): Number of questions completed.
        """
      self.questionsCompleted = questions

if __name__ == "__main__":
  print("Test cases for DataScore model")
  AndyScore = SaveModel(name="Andy", score=100, level=[1,2], questionsCompleted=5,correctAmt=30)


# automated testing

  class test_datascore(unittest.TestCase):
      def setUp(self):
          self.data = SaveModel(name="Jackson", score=100, level=[1,2], questionsCompleted=5,correctAmt=30)

      def test_setName(self):
         self.data.setName("Jackson")
         self.assertEqual(self.data.name, "Jackson", "name is not set")
      
      def test_setQuestionsCompleted(self):
         self.data.setQuestionsCompleted(10)
         self.assertEqual(self.data.questionsCompleted, 10, "questions completed not updated")

  unittest.main()