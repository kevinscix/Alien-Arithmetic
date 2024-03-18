import pygame
from components.player import Player
from module.gameGUI import GameGUI
from components.media import Media

MENU = 0
GAME = 1

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0
game_state = MENU  # Start with the menu


# Callback functions for GUI
def start_game():
    global game_state
    game_state = GAME  # This changes the game state to the game screen
    print("Starting the game...")

def quit_game():
    global running
    print("Quitting the game...")
    running = False

def highscore_game():
    pass

def tutorial_game():
    pass

def load_game():
    pass


# Create the GUI
gui = GameGUI(screen, start_game, quit_game, highscore_game, tutorial_game, load_game)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2 + screen.get_height() / 3)


#border for sprite ie like out of bounds since sprite can go out of screen
#changes to the movement needs to be made
#follow the game loop pattern a little bettert

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        #temp measure to quit game from fullscreen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Press Escape to quit
                running = False

    """substitute this with the media class later on returning the images"""
    screen.fill("blue")
    pygame.draw.circle(screen, "red", player_pos, 40)


    if game_state == MENU:
        # Handle GUI events and draw the menu
        gui.handle_events(events)
        # mainTitleImage = "group55/src/components/Images/mainPage.png"
        # Get the directory of the script
        script_dir = os.path.dirname(__file__)  # __file__ is the path to the current script

        # Go up one level from 'script_dir' to 'src' and then into the 'Images' directory
        mainTitleImagePath = os.path.join(script_dir, "..", "Images", "mainPage.png")

        # Normalize the path to remove any '..'
        mainTitleImage = os.path.normpath(mainTitleImagePath)
        mainTitle = Media(mainTitleImage)
        mainTitle.drawBackground(screen)
        gui.draw()
    elif game_state == GAME:
        # Main game logic and rendering
        screen.fill("black")
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

    # flip() the display to put your work on screen
    pygame.display.flip()


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000












    

pygame.quit()