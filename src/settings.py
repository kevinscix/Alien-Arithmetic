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

    blueLevelUp = os.path.join(current_dir,"assets", "visuals", "pages - backgrounds", "level up blue.png")
    redLevelUp = os.path.join(current_dir,"assets", "visuals", "pages - backgrounds", "level up red.png")
    yellowLevelUp = os.path.join(current_dir,"assets", "visuals", "pages - backgrounds", "level up yellow.png")


    blueOver = os.path.join(current_dir,"assets", "visuals", "pages - backgrounds", "game over blue.png")
    redOver = os.path.join(current_dir,"assets", "visuals", "pages - backgrounds", "game over red.png")
    yellowOver = os.path.join(current_dir,"assets", "visuals", "pages - backgrounds", "game over yellow.png")


    redShot = os.path.join(current_dir, "assets", "visuals", "projectiles", "red projectile icon.png")
    blueShot = os.path.join(current_dir, "assets", "visuals", "projectiles", "blue projectile icon.png")
    yellowShot = os.path.join(current_dir, "assets", "visuals", "projectiles", "yellow projectile icon.png")


    self.pairs = [
      {
        'ship' :  pygame.image.load(os.path.normpath(redship)),
        'background' : pygame.image.load(os.path.normpath(redBackground)),
        'level' : pygame.image.load(os.path.normpath(redLevelUp)),
        'over' : pygame.image.load(os.path.normpath(redOver)),
        'shot' : pygame.image.load(os.path.normpath(redShot))
      },
      {
        'ship' : pygame.image.load(os.path.normpath(blueship)),
        'background' : pygame.image.load(os.path.normpath(blueBackground)),
        'level' : pygame.image.load(os.path.normpath(blueLevelUp)),
        'over' : pygame.image.load(os.path.normpath(blueOver)),
        'shot' : pygame.image.load(os.path.normpath(blueShot))
      },
      {
        'ship' : pygame.image.load(os.path.normpath(yellowship)),
        'background' : pygame.image.load(os.path.normpath(yellowBackground)),
        'level' : pygame.image.load(os.path.normpath(yellowLevelUp)),
        'over' : pygame.image.load(os.path.normpath(yellowOver)),
        'shot' : pygame.image.load(os.path.normpath(yellowShot))
      }
    ]

  def getbackground(self):
    return random.choice(self.pairs)


if __name__ == "__main__":
  setz = Settings()
  print(setz.getbackground())
