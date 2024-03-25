import os
import sys

#change directory
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)  # Moves up to 'interface'
src_dir = os.path.dirname(parent_dir)  # Moves up to 'src'
sys.path.append(src_dir)


#pygame imports
import pygame
from PygameUIKit import Group, button


#state imports
from Interface.state_machine import State
from Interface.modules.state import SaveModel
from Interface.tutorial import TutorialState
from Interface.game import GameState
from Interface.leaderboard import LeaderboardState
from Interface.level import LevelState

#this file is a quick scehem of how a state would look like for login and sign in state!

#this isn't importing properly???? ill figure it out or someone else can i give up

class MenuState(State):
    def __init__(self, engine):
        super().__init__(engine)
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter
        
        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script


        #do we want a title image page for this page?
        menuImagePath = os.path.join(currentPath, "..", "components", "Images", "menuPage.png")
        # Normalize the path to remove any '..'
        self.menuImage = pygame.image.load(os.path.normpath(menuImagePath))
        self.menuImage= pygame.transform.scale(self.menuImage, (800, 600))
    
        self.user : SaveModel = None
       
       # Start button
        self.btn_start = button.ButtonText(
            "Start", 
            self.start_callback, 
            rect_color=(85, 145, 92),  # Green color
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
        # Load Game button
        self.btn_load = button.ButtonText(
            "Load Game", 
            self.change_state_load, 
            rect_color=(85, 92, 145),  # Blue color
            fixed_width=220,  # Slightly wider
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
        # Tutorial button
        self.btn_tutorial = button.ButtonText(
            "Tutorial", 
            self.change_state_tutorial, 
            # rect_color=(145, 92, 85),  # Orange color
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
        # Highscores button
        self.btn_highscores = button.ButtonText(
            "Highscores", 
            self.change_state_highscore, 
            rect_color=(92, 145, 85),  # Different shade of green
            fixed_width=220,  # Slightly wider
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
        # Quit button
        self.btn_quit = button.ButtonText(
            "Exit", 
            self.change_state_exit, 
            rect_color=(181, 71, 71),  # Red color
            fixed_width=180, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )


    #implement game state file
    def start_callback(self):
        self.engine.machine.next_state = GameState(self.engine)
        
        
    #call the singin state?
    def change_state_load(self):
        self.engine.machine.next_state = LevelState(self.engine)


    #call the tutorial state which will be just an image for now?
    def change_state_tutorial(self):
        self.engine.machine.next_state = TutorialState(self.engine)


    #do we jsut want to do a table of the top scores for the first 10?
    def change_state_highscore(self):
        self.engine.machine.next_state = LeaderboardState(self.engine)


    #quit functionality you can implement yourself
    def change_state_exit(self):
        from Interface.login import LoginState
        self.engine.machine.next_state = LoginState(self.engine)
 

    #Notes
        #I got rid of the visibility since its redundant if each state just changes the buttons entirely.
        #so i think this is fine. I wont delete the gameUI yet cause it might be useful for later
    def on_draw(self, surface):
        #change to real background?
        surface.blit(self.menuImage, (0, 0))
        
        button_spacing = 60

        start_y = surface.get_height() // 2 - (button_spacing * 2)  # Start drawing from this y-coordinate
    
            # Start button
        self.btn_start.draw(surface, *self.btn_start.surface.get_rect(center=(surface.get_width() // 2, start_y)).topleft)

            # Load Game button
        self.btn_load.draw(surface, *self.btn_load.surface.get_rect(center=(surface.get_width() // 2, start_y + button_spacing)).topleft)

            # Tutorial button
        self.btn_tutorial.draw(surface, *self.btn_tutorial.surface.get_rect(center=(surface.get_width() // 2, start_y + button_spacing * 2)).topleft)
       
            # Highscores button
        self.btn_highscores.draw(surface, *self.btn_highscores.surface.get_rect(center=(surface.get_width() // 2, start_y + button_spacing * 3)).topleft)

            # draw button
        self.btn_quit.draw(surface, *self.btn_quit.surface.get_rect(center=(surface.get_width() // 2, start_y + button_spacing * 4)).topleft)

        pygame.display.flip()

    def on_event(self, event):
        #theres no keyboard condition or still need to be determined for menu
        self.ui.handle_event(event)
