from components.player import *
import pygame
import math

class Projectile:

    def __init__(self):
        # projImg = pygame.image.load('standard bullet 32.png') for later
        
        # by default, the proj is on the edge of the screen, will change when fired
        self.projX  = 0 # x-coordinate of the projectile
        self.projY = 0 # y-coordinate of the projectile

        # the number of pixels the proj moves per frame
        self.projY_speed = 1 # speed of the projectile
        self.fired = False

    def trajectory(self, Player):
        # Set the initial position of the projectile to be just above the player
        self.projX = Player.xPos + (Player.width // 2)  # Center the projectile horizontally
        self.projY = Player.yPos

    def updateFire(self):
        if self.fired:
            # Move the projectile upwards only if it has been fired
            self.projY -= self.projY_speed

            # Check if projectile is off the screen
            if self.projY < 0:
                # Reset position and fired status to allow shooting again
                self.projY = Player.yPos
                self.fired = False 

    def collisionDetect(self, asteroidX, asteroidY):
        # Detect collision between the projectile and an asteroid
        distance = math.sqrt((asteroidX - self.projX) ** 2 + (asteroidY - self.projY) ** 2)
        if distance < 27:  # Adjust the collision distance as needed
            return True
        else:
            return False
        
 
# make projectile/player stuff compatible with main (its currently crashing)
        # use debug prints to help if you want
# make sure the firing/cooldown stuff works (i think its wrong now?)
# visually display the projectile with a small circle (you can borrow some of the code that they used for the ship)
# after all that, get in contact with jackson or andy to help you connect collisionDetect with the asteroid logic
        # i left some scrap code near the bottom of main that can help with this








