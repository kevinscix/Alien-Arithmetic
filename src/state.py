from pydantic import BaseModel
import json

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



if __name__ == "__main__":
  print("Test cases for DataScore model")
  state = State()


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



  EmptyPlayer.save_settings(AndyPlayer.model_dump_json(), "AndyPlayer.txt")
  EmptyPlayer.save_settings(EmptyPlayer.model_dump_json(), "EmptyPlayer.txt")
  data = EmptyPlayer.load_settings("EmptyPlayer.txt")
  andy = EmptyPlayer.load_settings("AndyPlayer.txt")
  if data:
    Player : SaveState = EmptyPlayer.model_validate_json(data)
    AndyPlaye : SaveState = EmptyPlayer.model_validate_json(andy)
    print(Player)
    print(AndyPlayer)



  # print(Player.model_dump_json() , Player.name)
  #testing the load function
  # jsonD = state.load_settings("Andy.txt")
  # Player : SaveState = EmptyPlayer.model_validate_json(jsonD)
  # print(Player.model_dump_json() , Player.name)



