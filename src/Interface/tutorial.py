from Interface.state_machine import State, DisplayEngine
from PygameUIKit import Group, button
import pygame
import os


class TutorialState(State):
    def __init__(self, engine, user):
        super().__init__(engine)
        self.currentPage = 0
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        self.user = user

        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        tutorialImagePath1 = os.path.join(currentPath, "..", "assets", "visuals", "pages - backgrounds", "tutorial page 1.png")
        self.tutorialImage1 = pygame.image.load(os.path.normpath(tutorialImagePath1))
        self.tutorialImage1 = pygame.transform.scale(self.tutorialImage1, (800, 600))
        tutorialImagePath2 = os.path.join(currentPath, "..", "assets", "visuals", "pages - backgrounds", "tutorial page 2.png")
        self.tutorialImage2 = pygame.image.load(os.path.normpath(tutorialImagePath2))
        self.tutorialImage2 = pygame.transform.scale(self.tutorialImage2, (800, 600))


        backButtonPath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "exitButton.png")
        self.backButtonImage = pygame.image.load(os.path.normpath(backButtonPath))
        self.backButtonImage = pygame.transform.scale(self.backButtonImage, (150, 100))
        leftButtonPath = os.path.join(currentPath, "..","assets", "visuals", "buttons", "text buttons", "left button.png")
        rightButtonPath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "right button.png")
        self.leftButtonImage = pygame.image.load(os.path.normpath(leftButtonPath))
        self.leftButtonImage = pygame.transform.scale(self.leftButtonImage, (75, 100))
        self.rightButtonImage = pygame.image.load(os.path.normpath(rightButtonPath))
        self.rightButtonImage = pygame.transform.scale(self.rightButtonImage, (75, 100))

       # Back button 
        #needs to set up the correct location for and settings 
        self.btn_back = button.ButtonPngIcon(
            self.backButtonImage, 
            self.change_state_menu, 
            ui_group=self.ui
        )

        self.btn_left = button.ButtonPngIcon(
            self.leftButtonImage, 
            self.change_state_left, 
            ui_group=self.ui
        )
        self.btn_right = button.ButtonPngIcon(
            self.rightButtonImage, 
            self.change_state_right, 
            ui_group=self.ui
        )
    

    def change_state_menu(self):
        from Interface.menu import MenuState
        self.engine.machine.next_state = MenuState(self.engine, self.user)
    

    def change_state_left(self):
        if self.currentPage == 1: 
            self.currentPage -= 1

    def change_state_right(self):
        if self.currentPage == 0:  
            self.currentPage += 1

    def on_draw(self, surface):
        if self.currentPage == 0:
            surface.blit(self.tutorialImage1, (0, 0))
            self.btn_right.draw(surface, 725, 275)
        else:
            surface.blit(self.tutorialImage2, (0, 0))
            self.btn_left.draw(surface, 4, 260)
        self.btn_back.draw(surface, 0, 500)
        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Returning to menu screen")
                self.go_back_menu()
        self.ui.handle_event(event)
