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
        self.projY_change = 1 # speed of the projectile
        self.fired = False

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
        

# Initialize Pygame
pygame.init()

# Set up the screen
screenWidth = 800 #alter to screen width
screenHeight = 600 #alter to screen width
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Alien Arthmetic")

player = Player()
projectile = Projectile()

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not projectile.fired:
                # Fire projectile when spacebar is pressed
                projectile.fire()
                projectile.trajectory(player)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    # Update projectile
    projectile.updateFire()

    # Draw player
    player.draw(screen)

    # Draw projectile
    if projectile.fired:
        pygame.draw.rect(screen, (255, 255, 255), (projectile.projX, projectile.projY, 5, 10))

    pygame.display.flip()

pygame.quit()





    