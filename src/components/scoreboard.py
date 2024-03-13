#Emily & Andy
from datascore import DataScore
from pydantic import BaseModel
from typing import Dict, Optional
import csv

#object to get all the data in csv file and logic

class Scoreboard(BaseModel):

  #total players
  numberPlayer : Optional[int] = None
  userType : Optional[int] = None

  #current player
  score : Optional[int] = None

  #currentPlayer : DataScore
  board : Optional[DataScore] = None

  # currentPlayer : DataScore --
  board : Dict[str, DataScore] = {}

  #returns 0 if user is true or 1 if user is false 
  def isPlayer(self):
    if self.userType == 1:
      return True

  def isInstructor(self):
    if self.userType == 0:
      return True
    
  # A different way?
  # def showScores(self):
  #   for name, score in self.board.items():
  #     print(f"Name: {name}, Score: {score}")

  def showScores(self):
    print(self.board)

  

  def getPlayer(self, name : str) -> DataScore:
    score = self.board[name]
    print(score)
    return score

  #load Score function load into -> self.board so data -> datascore -> append board
  def loadScore(self) -> None:
    pass


  #this code can be written better without the extra rows -> look for a better lib or smth online
  #this should just store the current player store and data.
  def storeScore(self, player : DataScore,  filename: str = ".\src\database.csv") -> None:
    print(player.fields())
    with open(filename, "a") as fileObj:
      writer = csv.writer(fileObj)
      writer.writerow(player.fields())


if __name__ == "__main__":
  print("Test case for scoreboard.")

  board = Scoreboard()

  AndyScore = DataScore(
    name="Andy",
    highScore=100,
    questionsCompleted=5,
    incorrectAmt=10,
    correctAmt=30,
    overallGrade=40,
    loggedIn=True
  )

  board.storeScore(player=AndyScore)

# load info 
  # each row - data score class, andy score: every element per row - create a data score for each row
  # improve score
  # load and store


