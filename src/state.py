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
    def save_settings(self, settings, filename):
        with open(filename, 'w') as file:
            json.dump(settings, file)

    def load_settings(self, filename):
        try:
            with open(filename, 'r') as file:
                settings = json.load(file)
                print(settings)
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
    level : list[int]

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


#all this stuff works just needs to make a saves folder cause its hitting requirements.txt, im going to ignore and foucs on other aspects
#scoreboard state -> should have just one txt file
class ScoreboardState(Scoreboard, State):
  def loadScore(self):
    txt_files = []
    database : List[SaveState]  = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".txt"):
                database.append(SaveState.model_validate_json(self.load_settings(file)))
                txt_files.append(os.path.join(root, file))
    print(database)
    return database



if __name__ == "__main__":
  print("Test cases for DataScore model")
  state = State()


  #Player example data
  AndyPlayer = SaveState(
    name="Andy",
    score=40,
    level=[2,1,3],
    highScore=50,
    questionsCompleted=3,
    incorrectAmt=1,
    correctAmt=10,
    overallGrade=50,
    loggedIn=True
  )

  #empty player/user data
  EmptyPlayer = SaveState(
    name="User",
    score=0,
    level=[0,0,0],
    highScore=0,
    questionsCompleted=0,
    incorrectAmt=0,
    correctAmt=0,
    overallGrade=0,
    loggedIn=False
    )

  #how saving workings and loading..
  EmptyPlayer.save_settings(AndyPlayer.model_dump_json(), "AndyPlayer.txt")
  EmptyPlayer.save_settings(EmptyPlayer.model_dump_json(), "EmptyPlayer.txt")
  data = EmptyPlayer.load_settings("EmptyPlayer.txt")
  andy = EmptyPlayer.load_settings("AndyPlayer.txt")

  #example of loading all the save states using the information
  board = ScoreboardState()
  scoreboard : List[SaveState] = board.loadScore()
  for score in scoreboard:
    print(score)




