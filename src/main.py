#pygame game loop template from pydocs
import pygame
from components.player import Player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player = Player()

#border for sprite ie like out of bounds since sprite can go out of screen
#changes to the movement needs to be made
#follow the game loop pattern a little bettert


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    """substitute this with the media class later on returning the images"""
    screen.fill("black")
    pygame.draw.circle(screen, "red", player_pos, 40)


    """make sure to implement movement restriction to specific area of the screen later on """
    keys = pygame.key.get_pressed()
    # WASD key movement
    if keys[pygame.K_w]:
        player_pos.y -= player.getSpeed() * dt
    if keys[pygame.K_s]:
        player_pos.y += player.getSpeed() * dt
    if keys[pygame.K_a]:
        player_pos.x -= player.getSpeed() * dt
    if keys[pygame.K_d]:
        player_pos.x += player.getSpeed() * dt
    # arrow key movement
    if keys[pygame.K_UP]:
        player_pos.y -= player.getSpeed() * dt  
    if keys[pygame.K_DOWN]:
        player_pos.y += player.getSpeed() * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= player.getSpeed() * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += player.getSpeed() * dt

    # mouse movement  
    # if pygame.mouse.get_focused():
    #     mouseMovement = pygame.mouse.get_rel()
    #     player_pos.x += mouseMovement[0]
    #     player_pos.y += mouseMovement[1]

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()