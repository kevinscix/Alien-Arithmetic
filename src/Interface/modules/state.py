import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)  # Moves up to 'interface'
src_dir = os.path.dirname(parent_dir)  # Moves up to 'src'
sys.path.append(src_dir)

from pydantic import BaseModel
import json
from components.scoreboard import Scoreboard
from typing import List



#this file represents the possible states which these objects should have
#save state is all possible states a "save/player should have"
#scoreboard state handles all the possible state for all users.

#should handle the state of the saves
#handle the interface, player?
class State():
    def __init__(self) -> None:
        self.pause = 0
        self.run = 1

    #placeholder methods
    def save_settings(self, settings, filename, file_path=os.path.join(src_dir, 'saves/')):
        with open(file_path + filename, 'w') as file:
            json.dump(settings, file)

    def load_settings(self, filename, file_path=os.path.join(src_dir, 'saves/')):
        try:
            with open(file_path + filename, 'r') as file:
                settings = json.load(file)
                return settings
        except FileNotFoundError:
            print("Settings file not found.")
            return None

#I want to make this change but I will keep this for now

#this is the actual contents of the basemodel of the content we want
#handles the level, access level, and maybe logged in?
class SaveModel(BaseModel):
    name : str
    score : int
    level : List[int]

    #question
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

class SaveState(SaveModel, State):
  def __str__(self) -> str:
     return "{} with a score of {}.".format(self.name, self.score)
  pass

import os


class ScoreboardState(Scoreboard, State):

  def loadScore(self):
    database : List[SaveState]  = []
    for root, dirs, files in os.walk(os.path.join(src_dir, 'saves/')):
        for file in files:
            try:
              print(file)
              if not file == ".DS_Store":
                user = SaveState.model_validate_json(self.load_settings(file))
                database.append(user)
            except:
              print(file)
              print("will catch the error when we return nonetype after iterating over the file")
              pass
    return sorted(database, key=lambda x: x.score, reverse=True)


  def getPlayer(self, playerName):
    saves = self.loadScore()
    for playerSave in saves:
      if playerSave.name == playerName:
        return playerSave

    #if player is not in the data base we should save them a new file for their save
    newPlayerSave = SaveState(
      name=playerName,
      score=000,
      level=[1,1], #max level so they have access to all
      highScore=0000,
      questionsCompleted=000,
      incorrectAmt=0000,
      correctAmt=000,
      overallGrade=0000,
      loggedIn=True
    )

    newPlayerSave.save_settings(newPlayerSave.model_dump_json(), playerName)
    return newPlayerSave

if __name__ == "__main__":
  print("Test cases for DataScore model")
  state = State()

  #example of loading all the save states using the information
  board = ScoreboardState()
  scoreboard : List[SaveState] = board.loadScore()

  for s in scoreboard:
    print(s)
