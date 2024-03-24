from state_machine import State, YourStateA, DisplayEngine
from PygameUIKit import Group, button
import pygame
import os

#comments
# do we need any interactions from this state


class TutorialState(State):
    def __init__(self, engine):
        super().__init__(engine)

        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
      
        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        tutorialImagePath = os.path.join(currentPath, "..", "src", "components", "Images", "tutorialScreen.png")
        self.tutorialScreen = pygame.image.load(os.path.normpath(tutorialImagePath))


       # Back button 
        #needs to set up the correct location for and settings 
        self.btn_back = button.ButtonText(
            "Go Back to Menu", 
            self.go_back_menu, 
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
    

    def go_back_menu(self):
        #should be like i think... we need to talk
        self.engine.machine.next_state = YourStateA(self.engine)


    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.tutorialScreen , (0, 0))
        #add the buttons we need should be 3 for the diff levels
        #change the values to make it better placed
        self.btn_back.draw(surface, *self.btn_start.surface.get_rect(center=(surface.get_height() // 2, surface.get_height()  // 2 - 50)).topleft)
        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Returning to menu screen")
                self.go_back_menu()
        self.ui.handle_event(event)
