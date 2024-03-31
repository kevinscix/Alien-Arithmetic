import os
import sys
import json
from components.scoreboard import Scoreboard
from typing import List
from components.datascore import SaveModel


#this file represents the possible states which these objects should have
#save state is all possible states a "save/player should have"
#scoreboard state handles all the possible state for all users.

#should handle the state of the saves
#handle the interface, player?
class State():
    """
    Represents the possible states for game objects.

    Attributes:
        pause (int): Represents the pause state.
        run (int): Represents the run state.
    """
    def __init__(self) -> None:
        """
        Initializes a State object with pause and run states.
        """
        self.pause = 0
        self.run = 1

    #placeholder methods
    def save_settings(self, settings, filename, file_path=os.path.join(src_dir, 'saves/')):
        """
        Saves settings to a JSON file.

        Args:
            settings: The settings to save.
            filename (str): The name of the file to save to.
            file_path (str, optional): The path to save the file to. Defaults to 'src/saves/'.
        """

        with open(file_path + filename, 'w') as file:
            json.dump(settings, file)

    def load_settings(self, filename, file_path=os.path.join(src_dir, 'saves/')):
        """
        Loads settings from a JSON file.

        Args:
            filename (str): The name of the file to load.
            file_path (str, optional): The path to load the file from. Defaults to 'src/saves/'.

        Returns:
            dict: The loaded settings.
        """
        try:
            with open(file_path + filename, 'r') as file:
                settings = json.load(file)
                return settings
        except FileNotFoundError:
            print("Settings file not found.")
            return None

#I want to make this change but I will keep this for now

class SaveState(SaveModel, State):
  """
  Represents the state of a save.

  Attributes:
      Inherits attributes and methods from SaveModel and State classes.
  """
  def __str__(self) -> str:
    """
    Returns a string representation of the SaveState object.

    Returns:
        str: A string representation of the SaveState object.
    """
    return "{} with a score of {}.".format(self.name, self.score)
  

import os


class ScoreboardState(Scoreboard, State):
  """
  Represents the state of the scoreboard.

  Attributes:
      Inherits attributes and methods from Scoreboard and State classes.
  """
  def loadScore(self):
    """
    Loads scores from saved files.

    Returns:
        List[SaveState]: A list of save states.
    """
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
    """
    Gets the player's save state.

    Args:
        playerName (str): The name of the player.

    Returns:
        SaveState: The player's save state.
    """
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
