from state_machine import State, YourStateA, YourStateB, DisplayEngine
from PygameUIKit import Group, button
import pygame
import os

from components.asteroid import asteroid
#use this to generate an asteroid list/dict might need to change


#this file is a quick scehem of how a state would look like for login and sign in state!

#this isn't importing properly???? ill figure it out or someone else can i give up
from modules.state import SaveModel


#need to talk to luca how this works
#this is like a bridging state to the game state
class LevelState(State):
    def __init__(self, engine):
        super().__init__(engine)

        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        menuImagePath = os.path.join(currentPath, "..", "src", "components", "Images", "innerLevelSelect.png")
        # Normalize the path to remove any '..'
        self.levelSelect = pygame.image.load(os.path.normpath(menuImagePath))
    
        self.user : SaveModel = None

       # Student Login button
        self.btn_level_one = button.ButtonText(
            "Student Login", 
            self.start_game_state(1,1,1), 
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )

        self.btn_level_two = button.ButtonText(
            "Student Login", 
            self.start_game_state(1,2,3), 
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
    
        #and so on, must wait to understand how this work before we continue

    def start_game_state(conditon1, conditon2, conditon3):
        #should be like i think... we need to talk
        #self.engine.machine.next_state = GameState(self.engine, condition1, condition2, condition3)
        pass


    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.levelSelect , (0, 0))

        #add the buttons we need should be 3 for the diff levels
        pygame.display.flip()

    def on_event(self, event):
        self.ui.handle_event(event)
l

if __name__ == "__main__":
    def main():
        pygame.init()
        engine = DisplayEngine('Example State machine', 60, 800, 600)
        engine.run(YourStateA(engine))
    pygame.quit()

    main()