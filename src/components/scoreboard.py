#Emily & Andy
from datascore import DataScore
from pydantic import BaseModel
from typing import Dict

#object to get all the data in csv file and logic

class Scoreboard(BaseModel):
  #total players
  numberPlayer : int
  userType : int
  Board : list[DataScore]

  #current player
  score : int
  currentPlayer : DataScore

  #returns 0 if user is true or 1 if user is false
  def isPlayer(self):
    if self.userType == 1:
      return True

  def isInstructor(self):
    if self.userType == 0:
      return True

  def showScores(self):
    print(self.Board)

  def getPlayer(self, name : str) -> DataScore:
    pass

  #this should just store the current player store and data.
  def storeScore(self, player : DataScore) -> None:
    pass





