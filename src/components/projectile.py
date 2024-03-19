from components.player import *
from src.main import *
import pygame
import math

class Projectile:

    def __init__(self):
        # projImg = pygame.image.load('standard bullet 32.png') for later
        
        # by default, the proj is on the edge of the screen, will change when fired
        self.projX = 0
        self.projY = 0

        # the number of pixels the proj moves per frame
        self.projY_change = 1 # speed of the projectile
        self.fired = False


    # 
    def trajectory(self, Player):

        # Set the initial position of the projectile to be just above the player
        self.projX = Player.xPos + (Player.width // 2)  # Center the projectile horizontally
        self.projY = Player.yPos

    def updateFire(self):
        if self.fired:
            # Move the projectile upwards only if it has been fired
            self.projY -= self.projY_change

            # Check if projectile is off the screen
            if self.projY < 0:
                # Reset position and fired status to allow shooting again
                self.projY = Player.yPos
                self.fired = False 

    def fire(self):
        # Set the fired flag to True when the projectile is fired
        self.fired = True

    #might need
    def collisionDetect(self, asteroidX, asteroidY):
        # Detect collision between the projectile and an asteroid
        distance = math.sqrt((asteroidX - self.projX) ** 2 + (asteroidY - self.projY) ** 2)
        if distance < 27:  # Adjust the collision distance as needed
            return True
        else:
            return False




    