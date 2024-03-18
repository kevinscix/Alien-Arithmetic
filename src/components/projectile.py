from player import *
import pygame

#added
import random
import math
from pygame import mixer

class Projectile:

    def __init__(self):
        # projImg = pygame.image.load('standard bullet 32.png') for later
        
        # by default, the proj is on the edge of the screen, will change when fired
        self.projX = 0 # x-coordinate of the projectile
        self.projY = 0 # y-coordinate of the projectile

        # the number of pixels the proj moves per frame
        self.projY_change = 1 # speed of the projectile


    # 
    def trajectory(self, Player):
        # proj spawns right above player
        self.projX = Player.xPos
        self.projY = Player.xPos # + some arbitrary number of pixels (for later)

        #added
        # Set the initial position of the projectile to be just above the player
        self.projX = Player.xPos + (Player.width // 2)  # Center the projectile horizontally
        self.projY = Player.yPos

    def updateFire(self):
        pass

    def collisionDetect(self):
        pass

    #might need
    def collision_detect(self, enemyX, enemyY):
        # Detect collision between the projectile and an enemy
        distance = math.sqrt((enemyX - self.projX) ** 2 + (enemyY - self.projY) ** 2)
        if distance < 27:  # Adjust the collision distance as needed
            return True
        else:
            return False




    