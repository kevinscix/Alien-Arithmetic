import os
import sys

#change directory
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)  # Moves up to 'interface'
src_dir = os.path.dirname(parent_dir)  # Moves up to 'src'
sys.path.append(src_dir)

from Interface.state_machine import State
from Interface.modules.state import SaveModel
from components.asteroid import Asteroid

from PygameUIKit import Group, button
import pygame


#this file is a quick scehem of how a state would look like for login and sign in state!

#this isn't importing properly???? ill figure it out or someone else can i give up

class GameState(State):
    def __init__(self, engine):
        super().__init__(engine)
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter
        WIDTH, HEIGHT = 800, 600

        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        gameImagePath = os.path.join(currentPath, "..", "components", "Images", "gamePlay1.png")
        shotImagePath = os.path.join(current_dir, "..", "assets", "visuals", "projectiles", "red projectile icon.png")

        self.gamePlay1Image = pygame.image.load(os.path.normpath(gameImagePath))
        #we need someone to load in the bullets
        self.shotImage = pygame.image.load(os.path.normpath(shotImagePath))
        self.shotImage = pygame.transform.scale(self.shotImage, (50, 50))
        self.gamePlay1Image = pygame.transform.scale(self.gamePlay1Image, (WIDTH, HEIGHT))
        self.user : SaveModel = None
        self.border = pygame.rect.Rect(10, 10, 600, 20)

       # Start button
        self.btn_puase = button.ButtonText(
            "PAUSE",
            self.pause_callback,
            rect_color=(85, 145, 92),  # Green color
            fixed_width=200,
            border_radius=10,
            text_align="center",
            ui_group=self.ui
        )

        #game constants
        self.shots = []
        self.player_radius = 25
        self.player_speed = 5
        self.bullet_radius = 5

        #needs a better way to do the width and height
            # a big issue is how we pass the surface around this is causing problems
            # think of a work around
        self.player_pos = [WIDTH // 2, ((HEIGHT / 4) * 3 + 20)]

        self.asteroidMaster = Asteroid(1)
        self.asteroidMaster.generateAsteroids()

    #only button that exsit on the screen
    def pause_callback(self):
        pass

    #Game specific functions
    def create_shot(self, player_pos):
        #limits the number of bullets on screen to one
        if not (len(self.shots) > 0):
            bullet_pos = [player_pos[0], player_pos[1]]
            return {
                'surface' :  self.shotImage,
                'position' : bullet_pos,
                'speed' : 8,
                'radius' : self.bullet_radius,
            }

    def move_shot(self):
        for shot in self.shots:
            shot['position'][1] -= shot['speed']


    def remove_shot(self):
        for shot in self.shots:
            if shot['position'][1] < 0:
                self.shots.remove(shot)

    def get_rect(self, obj):
        return pygame.Rect(obj['position'][0],
                        obj['position'][1],
                        obj['surface'].get_width(),
                        obj['surface'].get_height())

    def shot_collided(self):
        try:
            shot_rect = self.get_rect(self.shots[0])
            for asteroid in self.asteroidMaster.asteroidArr:
                if shot_rect.colliderect(self.get_rect(asteroid)):
                    #write logic about point gain and lost for health if correct or not
                    if asteroid['correct']:
                        #gain health gain store
                        #how should we draw the health bar onto the screen
                        #remove asteroids and start new level
                        self.newRound()
                        pass
                    else:
                        #loss health
                        pass
                    return True
            return False
        except:
            pass



    def newRound(self):
        self.asteroidMaster.asteroidArr = []
        self.asteroidMaster.generateAsteroids()

    def on_draw(self, surface):
        #pops the screen up
        #problem is the the surface is only passed on surface we can either hard code the width or heights to reduce calling this function
        #over and over again. for the sake of prototyping ill leave it here cause ill figure it out later
        surface.blit(self.gamePlay1Image, (0, 0))

        #moves the bullets down the screen
        self.move_shot()
        self.remove_shot()
        self.asteroidMaster.move_asteroids()

        for shot in self.shots:
            surface.blit(shot['surface'], shot['position'])

            # pygame.draw.circle(surface, "black", shot['position'], shot['radius'])
        for asteroid in self.asteroidMaster.asteroidArr:
            surface.blit(asteroid['surface'], asteroid['position'])
            surface.blit(asteroid['number_surface'], asteroid['position'])

            # pygame.draw.circle(surface, "pink", asteroid['position'], 50)

        self.shot_collided()

        surface.blit(self.asteroidMaster.question_surface, [500, 300])

        pygame.draw.circle(surface, "red", self.player_pos, self.player_radius)
        pygame.draw.rect(surface, "red", self.border)
        pygame.display.flip()

    def on_event(self, event):
        #theres no keyboard condition or still need to be determined for menu
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("pew pew") # debug print
                shot = self.create_shot(player_pos=self.player_pos)
                if shot:
                    self.shots.append(shot)

        self.ui.handle_event(event)


    def handle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_pos[0] -= self.player_speed
        if keys[pygame.K_RIGHT]:
            self.player_pos[0] += self.player_speed

