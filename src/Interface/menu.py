from state_machine import State, YourStateA, YourStateB, DisplayEngine
from PygameUIKit import Group, button
from modules.state import SaveModel
import pygame
import os


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
        mainTitleImagePath = os.path.join(currentPath, "..", "src", "components", "Images", "titlePage.png")
        # Normalize the path to remove any '..'
        self.mainTitleImage = pygame.image.load(os.path.normpath(mainTitleImagePath))
    
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
            self.load_callback, 
            rect_color=(85, 92, 145),  # Blue color
            fixed_width=220,  # Slightly wider
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
        # Tutorial button
        self.btn_tutorial = button.ButtonText(
            "Tutorial", 
            self.tutorial_callback, 
            # rect_color=(145, 92, 85),  # Orange color
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
        # Highscores button
        self.btn_highscores = button.ButtonText(
            "Highscores", 
            self.highscores_callback, 
            rect_color=(92, 145, 85),  # Different shade of green
            fixed_width=220,  # Slightly wider
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
        # Quit button
        self.btn_quit = button.ButtonText(
            "Quit", 
            self.quit_callback, 
            rect_color=(181, 71, 71),  # Red color
            fixed_width=180, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )


    #implement game state file
    def start_callback(self):
        pass
        
    #call the singin state?
    def load_callback(self):
        pass

    #call the tutorial state which will be just an image for now?
    def tutorial_callback(self):
        pass

    #do we jsut want to do a table of the top scores for the first 10?
    def highscores_callback(self):
        pass

    #quit functionality you can implement yourself
    def quit_callback(self):
        pass 


    #Notes
        #I got rid of the visibility since its redundant if each state just changes the buttons entirely.
        #so i think this is fine. I wont delete the gameUI yet cause it might be useful for later
    def on_draw(self, surface):
        #copy and pasted from the gameGUI
        
        button_spacing = 60

        start_y = self.window.get_height() // 2 - (button_spacing * 2)  # Start drawing from this y-coordinate
    
            # Start button
        self.btn_start.draw(self.window, *self.btn_start.surface.get_rect(center=(self.window.get_width() // 2, start_y)).topleft)

            # Load Game button
        self.btn_load.draw(self.window, *self.btn_load.surface.get_rect(center=(self.window.get_width() // 2, start_y + button_spacing)).topleft)

            # Tutorial button
        self.btn_tutorial.draw(self.window, *self.btn_tutorial.surface.get_rect(center=(self.window.get_width() // 2, start_y + button_spacing * 2)).topleft)
       
            # Highscores button
        self.btn_highscores.draw(self.window, *self.btn_highscores.surface.get_rect(center=(self.window.get_width() // 2, start_y + button_spacing * 3)).topleft)

            # draw button
        self.btn_quit.draw(self.window, *self.btn_quit.surface.get_rect(center=(self.window.get_width() // 2, start_y + button_spacing * 4)).topleft)

        pygame.display.flip()

    def on_event(self, event):
        #theres no keyboard condition or still need to be determined for menu
        self.ui.handle_event(event)
