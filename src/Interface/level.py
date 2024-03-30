import os
import sys

#change directory
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)  # Moves up to 'interface'
src_dir = os.path.dirname(parent_dir)  # Moves up to 'src'
sys.path.append(src_dir)

from Interface.state_machine import State
from Interface.modules.state import SaveModel
from Interface.game import GameState

from PygameUIKit import Group, button
import pygame
#use this to generate an asteroid list/dict might need to change


#this file is a quick scehem of how a state would look like for login and sign in state!

#this isn't importing properly???? ill figure it out or someone else can i give up

#need to talk to luca how this works
#this is like a bridging state to the game state
currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
quitImagePath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "exitButton.png")
quit_image = pygame.image.load(os.path.normpath(quitImagePath))
quit_image = pygame.transform.scale(quit_image, (150, 105))

class OuterLevelState(State):
    def __init__(self, engine, user):
        super().__init__(engine)

        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        self.user = user
        #make this into a utils function?
        levelImagePath = os.path.join(currentPath, "..","components", "Images", "outerLevelSelect.png")
        self.levelSelect = pygame.image.load(os.path.normpath(levelImagePath))
        self.levelSelect= pygame.transform.scale(self.levelSelect, (800, 600))
        xAsteroidPath = os.path.join(currentPath, "..", "assets", "visuals", "stage-level select", "xAsteroid.png")
        self.xAsteroid = pygame.image.load(os.path.normpath(xAsteroidPath))
        self.xAsteroid= pygame.transform.scale(self.xAsteroid, (125, 125))
        plusAsteroidPath = os.path.join(currentPath, "..","assets", "visuals", "stage-level select", "plusAsteroid.png")
        self.plusAsteroid = pygame.image.load(os.path.normpath(plusAsteroidPath))
        self.plusAsteroid= pygame.transform.scale(self.plusAsteroid, (125, 125))
        minusAsteroidPath = os.path.join(currentPath, "..","assets", "visuals", "stage-level select", "minusAsteroid.png")
        self.minusAsteroid = pygame.image.load(os.path.normpath(minusAsteroidPath))
        self.minusAsteroid= pygame.transform.scale(self.minusAsteroid, (125, 125))

       # Student Login button
        self.btn_level_x = button.ButtonPngIcon(
            self.xAsteroid, 
            lambda: self.start_inner_state("multiply"), 
            ui_group=self.ui
        )

        self.btn_level_plus = button.ButtonPngIcon(
            self.plusAsteroid, 
            lambda: self.start_inner_state("plus"), 
            ui_group=self.ui
        )

        self.btn_level_minus = button.ButtonPngIcon(
            self.minusAsteroid, 
            lambda: self.start_inner_state("minus"), 
            ui_group=self.ui
        )

        self.btn_quit = button.ButtonPngIcon(
            quit_image, 
            self.change_state_exit, 
            ui_group=self.ui
        )

    def start_inner_state(self, mode):
        self.engine.machine.next_state = InnerLevelState(self.engine, mode, self.user)
        print(mode)

    def change_state_exit(self):
        from Interface.menu import MenuState
        self.engine.machine.next_state = MenuState(self.engine, self.user)


    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.levelSelect , (0, 0))

        self.btn_level_plus.draw(surface, 260, 30)
        self.btn_level_minus.draw(surface, 415, 225)
        self.btn_level_x.draw(surface, 260, 435)
        self.btn_quit.draw(surface, 5, 485) 


        
        #add the buttons we need should be 3 for the diff levels
        pygame.display.flip()

    def on_event(self, event):
        self.ui.handle_event(event)

class InnerLevelState(State):
    def __init__(self, engine, mode, user):
        super().__init__(engine)

        self.mode = mode        
        self.user = user
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        #make this into a utils function?

        levelSelectPath = os.path.join(currentPath, "..", "components", "Images", "innerLevelSelect.png")
        self.levelSelect = pygame.image.load(os.path.normpath(levelSelectPath))
        self.levelSelect= pygame.transform.scale(self.levelSelect, (800, 600))
        levelOnePath = os.path.join(currentPath, "..", "assets", "visuals", "stage-level select", "levelOne.png")
        self.levelOne = pygame.image.load(os.path.normpath(levelOnePath))
        self.levelOne= pygame.transform.scale(self.levelOne, (150, 125))
        levelTwoPath = os.path.join(currentPath, "..","assets", "visuals", "stage-level select", "levelTwo.png")
        self.levelTwo = pygame.image.load(os.path.normpath(levelTwoPath))
        self.levelTwo = pygame.transform.scale(self.levelTwo, (150, 125))
        levelThreePath = os.path.join(currentPath, "..","assets", "visuals", "stage-level select", "levelThree.png")
        self.levelThree = pygame.image.load(os.path.normpath(levelThreePath))
        self.levelThree = pygame.transform.scale(self.levelThree, (150, 125))


       # Student Login button
        self.btn_level_one = button.ButtonPngIcon(
            self.levelOne, 
            lambda: self.start_game_state(), 
            ui_group=self.ui
        )

        self.btn_level_two = button.ButtonPngIcon(
            self.levelTwo, 
            lambda: self.start_game_state(), 
            ui_group=self.ui
        )

        self.btn_level_three = button.ButtonPngIcon(
            self.levelThree, 
            lambda: self.start_game_state(), 
            ui_group=self.ui
        )

        self.btn_quit = button.ButtonPngIcon(
            quit_image, 
            self.change_state_exit, 
            ui_group=self.ui
        )
        
    
        #and so on, must wait to understand how this work before we continue

    def start_game_state(self):
        self.engine.machine.next_state = GameState(self.engine, self.user, self.mode)

    def change_state_exit(self):
        self.engine.machine.next_state = OuterLevelState(self.engine, self.user)

    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.levelSelect , (0, 0))
        self.btn_level_one.draw(surface, 245, 35)
        self.btn_level_two.draw(surface, 405, 238)
        self.btn_level_three.draw(surface, 255, 445)
        self.btn_quit.draw(surface, 5, 485) 


        #add the buttons we need should be 3 for the diff levels
        pygame.display.flip()

    def on_event(self, event):
        self.ui.handle_event(event)
