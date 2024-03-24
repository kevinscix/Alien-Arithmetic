from state_machine import State, YourStateA
from PygameUIKit import Group, button
from modules.state import SaveModel
import pygame
import os


#this file is a quick scehem of how a state would look like for login and sign in state!

#this isn't importing properly???? ill figure it out or someone else can i give up

class GameState(State):
    def __init__(self, engine):
        super().__init__(engine)
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter
       
    
        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        gamePlay1Path = os.path.join(currentPath, "..", "src", "components", "Images", "gamePlay1.png")
        gamePlay1Image = pygame.image.load(os.path.normpath(gamePlay1Path))
        self.user : SaveModel = None

       
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
        WIDTH, HEIGHT = 800, 600
        player_radius = 25
        player_speed = 5
        bullet_radius = 5

        #needs a better way to do the width and height 
            # a big issue is how we pass the surface around this is causing problems 
            # think of a work around
        self.player_pos = [WIDTH // 2, ((HEIGHT / 4) * 3 + 20)]
        self.gamePlay1Image = pygame.transform.scale(self.gamePlay1Image, (WIDTH, HEIGHT))

    #only button that exsit on the screen
    def pause_callback(self):
        pass
        
    #Game specific functions
    def create_shot(self, player_pos, surface):
        pygame.draw.circle(surface, "red", player_pos, self.bullet_radius)
        bullet_pos = [player_pos[0], player_pos[1]]
        return {
            'position' : bullet_pos,
            'speed' : 8,
            'radius' : self.bullet_radius,
        }

    def move_shot(self):
        for shot in self.shots:
            shot['position'][1] -= shot['speed']
        
    def on_draw(self, surface):
        #pops the screen up
        #problem is the the surface is only passed on surface we can either hard code the width or heights to reduce calling this function
        #over and over again. for the sake of prototyping ill leave it here cause ill figure it out later
        surface.blit(self.gamePlay1Image  , (0, 0))
        
        #moves the bullets down the screen
        self.move_shot()
        #draws the circles in the new position
        for shot in self.shots:
            pygame.draw.circle(surface, "black", shot['position'], shot['radius'])

        pygame.display.flip()

    def on_event(self, event):
        #theres no keyboard condition or still need to be determined for menu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player_pos[0] -= self.player_speed
            if event.key == pygame.K_RIGHT:
                self.player_pos[0] -= self.player_speed
        if event.type == pygame.KEYUP:
            print("pew pew") # debug print
            self.shots.append(self.create_shot(player_pos=self.player_pos))

        self.ui.handle_event(event)
