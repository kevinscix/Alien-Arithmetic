import pygame
from components.player import Player
from components.gameGUI import GameGUI
from components.projectile import Projectile
import os

MENU = 0
LOGIN = 1
TEACHER = 2
TUTORIAL = 3
LEVELMAIN = 4
GAME = 5
SCOREBOARD = 6
LEVELPLUS = 7
LEVELMINUS = 8
LEVELX = 9

# pygame setup ---------------------
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0
game_state = MENU  # Start with the menu
# ---------------------

# Callback functions for GUI ---------------------
def start_game():
    global game_state
    # bring to level screen but since we don't have yet we will just bring to game screen
    game_state = GAME  # This changes the game state to the game screen

def quit_game():
    global running
    print("Quitting the game...")
    running = False

def highscores_game():
    global game_state
    game_state = SCOREBOARD
    print("Highscores...")

def tutorial_game():
    global game_state
    game_state = TUTORIAL

def load_game():
    #call some function to load game then level screen
    global game_state
    game_state = LEVELMAIN
    print("Loading game...")

def studentLogin_game():
    global game_state
    # ask for username of student before moving to new screen implement later
    game_state = LOGIN  

def teacherLogin_game():
    global game_state
    game_state = TEACHER
    
# ---------------------

# Create the GUI & set player location---------------------
gui = GameGUI(screen, start_game, quit_game, load_game, tutorial_game, highscores_game, studentLogin_game, teacherLogin_game)
player_pos = pygame.Vector2(screen.get_width() / 2, (screen.get_height() / 4) * 3 + 20) 
# ---------------------

#border for sprite ie like out of bounds since sprite can go out of screen
#changes to the movement needs to be made
#follow the game loop pattern a little better

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Press Escape to quit
                running = False
        


    currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script

    if game_state == MENU:
        gui.update_visibility(game_state)
        # Handle GUI events and draw the menu
        gui.handle_events(events)
        # Go up one level from 'currentPath' to 'src' and then into the 'Images' directory
        mainTitleImagePath = os.path.join(currentPath, "..", "src", "components", "Images", "titlePage.png")
        # Normalize the path to remove any '..'
        mainTitleImage = pygame.image.load(os.path.normpath(mainTitleImagePath))
        mainTitleImage = pygame.transform.scale(mainTitleImage, (screen.get_width(), screen.get_height()))
        screen.blit(mainTitleImage, (0, 0))
        gui.draw()

    elif game_state == LOGIN:
        screen.fill("white")
        gui.update_visibility(game_state)
        # Handle GUI events and draw the login screen
        gui.handle_events(events)
        gui.draw()

    elif game_state == TEACHER:
        screen.fill("purple")

    elif game_state == TUTORIAL:
        tutorialImagePath = os.path.join(currentPath, "..", "src", "components", "Images", "tutorialScreen.png")
        tutorialImage = pygame.image.load(os.path.normpath(tutorialImagePath))
        tutorialImage = pygame.transform.scale(tutorialImage, (screen.get_width(), screen.get_height()))
        screen.blit(tutorialImage, (0, 0))

    elif game_state == LEVELMAIN:
        levelSelectPath = os.path.join(currentPath, "..", "src", "components", "Images", "mainLevelSelect.png")
        levelSelectImage = pygame.image.load(os.path.normpath(levelSelectPath))
        levelSelectImage = pygame.transform.scale(levelSelectImage, (screen.get_width(), screen.get_height()))
        screen.blit(levelSelectImage, (0, 0))

    elif game_state == LEVELPLUS or game_state == LEVELMINUS or game_state == LEVELX:
        innerLevelSelectPath = os.path.join(currentPath, "..", "src", "components", "Images", "innerLevelSelect.png")
        innerLevelSelect = pygame.image.load(os.path.normpath(innerLevelSelectPath))
        innerLevelSelect = pygame.transform.scale(innerLevelSelect, (screen.get_width(), screen.get_height()))
        screen.blit(innerLevelSelect, (0, 0))

    
    elif game_state == GAME:
        gui.update_visibility(game_state)
        # Main game logic and rendering
        #if level is different we can use gameplay2.png or gameplay3.png image later on using if statement off the game_state variable
        gamePlay1Path = os.path.join(currentPath, "..", "src", "components", "Images", "gamePlay1.png")
        # Normalize the path to remove any '..'
        gamePlay1Image = pygame.image.load(os.path.normpath(gamePlay1Path))
        gamePlay1Image = pygame.transform.scale(gamePlay1Image, (screen.get_width(), screen.get_height()))
        screen.blit(gamePlay1Image, (0, 0))
        """substitute this with the media class later on returning the images"""
        pygame.draw.circle(screen, "red", (int(player_pos.x), int(player_pos.y)), 40)

        
        """make sure to implement movement restriction to specific area of the screen later on """
        keys = pygame.key.get_pressed()
        # WASD key movement
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
        # arrow key movement
        if keys[pygame.K_LEFT]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_RIGHT]:
            player_pos.x += 300 * dt

        # projectile input
        if keys[pygame.K_SPACE] or keys[pygame.K_SPACE] or keys[pygame.K_KP_ENTER]:
            print("pew pew") # debug print
            Player.shoot() # direct to the shoot method in player

    elif game_state == SCOREBOARD:
        screen.fill("black")
        
    else:
        print("Error: Invalid game state")

    # flip() the display to put your work on screen
    pygame.display.flip()

    # handle collisions and update the projectile movement
        
    # -----===== LUCA'S SHIT =====----- 

    # for asteroid in asteroids:
    #     if projectile.collisionDetect(asteroid.xPosition, asteroid.yPosition):
    #         pass # handle asteroid collisions

    # Projectile.updateFire()

    # -----===== END OF LUCA'S SHIT =====----- 


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


pygame.quit()