import pygame
import random
import sys
import os
# Setup the environment by appending the current directory to the system path for asset access.
current_dir = os.path.dirname(__file__)
sys.path.append(current_dir)


class Settings():
  """
    A class to manage and provide settings and assets for the game, such as player ships, backgrounds, level-up screens, game over screens, and projectiles.

    Attributes:
        pairs (list): A list of dictionaries where each dictionary represents a theme set including ship, background, level-up screen, game over screen, and projectile image.
    """
  def __init__(self):
    """
    Initializes the Settings class by loading all necessary game assets from the assets directory and creating theme sets.
    """
    # Paths for various game assets are constructed here using `os.path.join`
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

    # Each game asset is loaded and stored in a list of dictionaries as pairs
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
    """
    Randomly selects and returns one theme set of game assets from the available sets.

    Returns:
      dict: A randomly selected theme set containing a ship, background, level-up screen, game over screen, and projectile image.
    """
    # Randomly select and return one theme set from `pairs`
    return random.choice(self.pairs)


if __name__ == "__main__":
  setz = Settings()
  print(setz.getbackground())
