import pygame
import random
import sys
import os

current_dir = os.path.dirname(__file__)
sys.path.append(current_dir)


class Settings():
  def __init__(self):
    redship  = os.path.join(current_dir, "assets", "visuals", "player ship", "ship red.png")
    blueship = os.path.join(current_dir, "assets", "visuals", "player ship", "ship blue.png")
    yellowship = os.path.join(current_dir, "assets", "visuals", "player ship", "ship yellow.png")

    blueBackground = os.path.join(current_dir,"assets", "visuals", "pages - backgrounds", "blue level page.png")
    redBackground = os.path.join(current_dir,"assets", "visuals", "pages - backgrounds", "red level page.png")
    yellowBackground = os.path.join(current_dir,"assets", "visuals", "pages - backgrounds", "yellow level page.png")

    self.pairs = [
      {
        'ship' :  pygame.image.load(os.path.normpath(redship)),
        'background' : pygame.image.load(os.path.normpath(redBackground))
      },
      {
        'ship' : pygame.image.load(os.path.normpath(blueship)),
        'background' : pygame.image.load(os.path.normpath(blueBackground))
      },
      {
        'ship' : pygame.image.load(os.path.normpath(yellowship)),
        'background' : pygame.image.load(os.path.normpath(yellowBackground))
      },
    ]

  def getbackground(self):
    return random.choice(self.pairs)


if __name__ == "__main__":
  setz = Settings()
  print(setz.getbackground())
