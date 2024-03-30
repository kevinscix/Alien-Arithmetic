from Interface.state_machine import State, DisplayEngine
from PygameUIKit import Group, button
import pygame
import os

#comments
# do we need any interactions from this state


class TutorialState(State):
    def __init__(self, engine, user):
        super().__init__(engine)

        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        self.user = user

        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        tutorialImagePath = os.path.join(currentPath, "..", "assets", "visuals", "pages - backgrounds", "tutorial page.png")
        # Normalize the path to remove any '..'
        self.tutorialImage = pygame.image.load(os.path.normpath(tutorialImagePath))
        self.tutorialImage = pygame.transform.scale(self.tutorialImage, (860, 600))

        backButtonPath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "logOutButton.png")
        self.backButtonImage = pygame.image.load(os.path.normpath(backButtonPath))
        self.backButtonImage = pygame.transform.scale(self.backButtonImage, (150, 100))

       # Back button 
        #needs to set up the correct location for and settings 
        self.btn_back = button.ButtonPngIcon(
            self.backButtonImage, 
            self.change_state_menu, 
            ui_group=self.ui
        )
    

    def change_state_menu(self):
        from Interface.menu import MenuState
        self.engine.machine.next_state = MenuState(self.engine, self.user)


    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.tutorialImage, (-30, 0))
        #add the buttons we need should be 3 for the diff levels
        #change the values to make it better placed
        self.btn_back.draw(surface, 0, 500)
        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Returning to menu screen")
                self.go_back_menu()
        self.ui.handle_event(event)
