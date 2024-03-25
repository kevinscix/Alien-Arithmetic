
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
class InnerLevelState(State):
    def __init__(self, engine):
        super().__init__(engine)

        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        self.levelSelect = os.path.join(currentPath, "..","components", "Images", "innerLevelSelect.png")
        # Normalize the path to remove any '..'
        self.levelSelect = pygame.image.load(os.path.normpath(self.levelSelect))
        self.levelSelect= pygame.transform.scale(self.levelSelect, (800, 600))

        self.user : SaveModel = None

       # Student Login button
        self.btn_level_one = button.ButtonText(
            "Student Login", 
            self.start_game_state, 
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )

        self.btn_level_two = button.ButtonText(
            "Student Login", 
            self.start_game_state, 
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
    
        #and so on, must wait to understand how this work before we continue

    def start_game_state(self):
        self.engine.machine.next_state = GameState(self.engine)


    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.levelSelect , (0, 0))

        #add the buttons we need should be 3 for the diff levels
        pygame.display.flip()

    def on_event(self, event):
        self.ui.handle_event(event)



class OutterLevelState(State):
    def __init__(self, engine):
        super().__init__(engine)

        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        menuImagePath = os.path.join(currentPath, "..","components", "Images", "outterLevelSelect.png")
        # Normalize the path to remove any '..'
        self.levelSelect = pygame.image.load(os.path.normpath(menuImagePath))
        self.levelSelect= pygame.transform.scale(self.levelSelect, (800, 600))

        self.user : SaveModel = None

       # Student Login button
        self.btn_level_one = button.ButtonText(
            "Student Login", 
            self.start_inner_state, 
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )

        self.btn_level_two = button.ButtonText(
            "Student Login", 
            self.start_inner_state, 
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
    
        #and so on, must wait to understand how this work before we continue

    def start_inner_state(self):
        self.engine.machine.next_state = InnerLevelState(self.engine)


    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.levelSelect , (0, 0))


        
        #add the buttons we need should be 3 for the diff levels
        pygame.display.flip()

    def on_event(self, event):
        self.ui.handle_event(event)

