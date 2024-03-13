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
    
  # A different way --
  # def showScores(self):
  #   for name, score in self.board.items():
  #     print(f"Name: {name}, Score: {score}")

  def showScores(self):
    print(self.board)

  # A different way --
  # def getPlayer(self, name : str) -> DataScore:
  #       score = self.board.get(name)
  #       if score:
  #           print(score)
  #       else:
  #           print(f"No player with the name {name} found.")
  #       return score

  def getPlayer(self, name : str) -> DataScore:
    score = self.board[name]
    print(score)
    return score

  #load Score function load into -> self.board so data -> datascore -> append board
  def loadScore(self) -> None:
    pass

  # a different way --
  # load Score function load into -> self.board so data -> datascore -> append board
  # def loadScore(self, filename: str = ".\src\database.csv") -> None:
  #       with open(filename, "r") as fileObj:
  #           reader = csv.reader(fileObj)
  #           for row in reader:
  #               name, highScore, questionsCompleted, incorrectAmt, correctAmt, overallGrade, loggedIn = row
  #               score = DataScore(
  #                   name=name,
  #                   highScore=int(highScore),
  #                   questionsCompleted=int(questionsCompleted),
  #                   incorrectAmt=int(incorrectAmt),
  #                   correctAmt=int(correctAmt),
  #                   overallGrade=int(overallGrade),
  #                   loggedIn=bool(loggedIn)
  #               )
  #               self.board[name] = score

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

  # Load scores from the CSV file
  board.loadScore()

  # Display scores
  board.showScores()

  # Example of adding a new score and storing it in the CSV file
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

# added/what it does - 
  # load scores from csv
  #   - load score method reads the data from the file
  #   - opens file in read mode (iterates over each row in the file)
  #   - in each row, grabs the data for a players Scoreboard
  #   - creates a dataScore object
  #   - adds dataScore to the board dict of Scoreboard (using player as the key)
  
  # displayingscores
    # - showScores interates over each item in the board dict
    # - print each players name and their DataScore
  
  # retriving the score
  #   - get player takes a players name as an input
  #   - retrieves the datascore object associated with the players name from board dict
  #   - if found, prints score; if not, says no player found
   
  # storing a new score in the csv
  #   - storeScore takes the Datascore object (player) and a filename (optionally) as inputs
  #   - opens csv in append mode
  #   - creates a csv writer object to write data to the file
  #   - writes a new row to the csv file from datascore (name, score, etc), storing the new score