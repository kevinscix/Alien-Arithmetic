from player import *
import pygame

class Projectile:

    def __init__(self):
        # projImg = pygame.image.load('standard bullet 32.png') for later
        
        # by default, the proj is on the edge of the screen, will change when fired
        self.projX = 0
        self.projY = 0

        # the number of pixels the proj moves per frame
        self.projY_change = 1


    # 
    def trajectory(self, Player):
        # proj spawns right above player
        self.projX = Player.xPos
        self.projY = Player.xPos # + some arbitrary number of pixels (for later)

    def updateFire(self):
        pass

    def collisionDetect(self):
        pass



    