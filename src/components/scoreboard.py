#Emily & Andy
from components.datascore import DataScore
from pydantic import BaseModel
from typing import Dict, Optional


#we should clarify the logic for this file, it doesnt really make senses now
#I reread what we wrote here

#model representation of what the scoreboard 
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
    
  def showScores(self):
    for name, score in self.board.items():
      print(f"Name: {name}, Score: {score}")

  # def showScores(self):
  #   print(self.board)

  def getPlayer(self, name : str) -> DataScore:
        score = self.board.get(name)
        if score:
            print(score)
        else:
            print(f"No player with the name {name} found.")
        return score

  # def getPlayer(self, name : str) -> DataScore:
  #   score = self.board[name]
  #   print(score)
  #   return score


# added/what it does - 
  # load scores from csv
  #   - load score method reads the data from the file
  #   - opens file in read mode (iterates over each row in the file)
  #   - in each row, grabs the data for a players Scoreboard
  #   - creates a dataScore object
  #   - adds dataScore to the board dict of Scoreboard (using player as the key)
  
  # displayingscores
  #   - showScores interates over each item in the board dict
  #   - print each players name and their DataScore
  
  # retriving the score
  #   - get player takes a players name as an input
  #   - retrieves the datascore object associated with the players name from board dict
  #   - if found, prints score; if not, says no player found
   
  # storing a new score in the csv
  #   - storeScore takes the Datascore object (player) and a filename (optionally) as inputs
  #   - opens csv in append mode
  #   - creates a csv writer object to write data to the file
  #   - writes a new row to the csv file from datascore (name, score, etc), storing the new score