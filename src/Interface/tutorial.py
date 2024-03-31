from Interface.state_machine import State, DisplayEngine
from PygameUIKit import Group, button
import pygame
import os


class TutorialState(State):
    def __init__(self, engine, user):
        super().__init__(engine)
        self.current_page = 0
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        self.user = user

        #make this into a utils function?
        current_path = os.path.dirname(__file__)  # __file__ is the path to the current script
        tutorial_image_path_1 = os.path.join(current_path, "..", "assets", "visuals", "pages - backgrounds", "tutorial page 1.png")
        self.tutorial_image_1 = pygame.image.load(os.path.normpath(tutorial_image_path_1))
        self.tutorial_image_1 = pygame.transform.scale(self.tutorial_image_1, (800, 600))
        tutorial_image_path_2 = os.path.join(current_path, "..", "assets", "visuals", "pages - backgrounds", "tutorial page 2.png")
        self.tutorial_image_2 = pygame.image.load(os.path.normpath(tutorial_image_path_2))
        self.tutorial_image_2 = pygame.transform.scale(self.tutorial_image_2, (800, 600))


        back_button_path = os.path.join(current_path, "..", "assets", "visuals", "buttons", "text buttons", "exitButton.png")
        self.back_button_image = pygame.image.load(os.path.normpath(back_button_path))
        self.back_button_image = pygame.transform.scale(self.back_button_image, (150, 100))
        left_button_path = os.path.join(current_path, "..","assets", "visuals", "buttons", "text buttons", "left button.png")
        left_button_path = os.path.join(current_path, "..", "assets", "visuals", "buttons", "text buttons", "right button.png")
        self.leftButtonImage = pygame.image.load(os.path.normpath(left_button_path))
        self.leftButtonImage = pygame.transform.scale(self.leftButtonImage, (75, 100))
        self.rightButtonImage = pygame.image.load(os.path.normpath(left_button_path))
        self.rightButtonImage = pygame.transform.scale(self.rightButtonImage, (75, 100))

       # Back button 
        #needs to set up the correct location for and settings 
        self.btn_back = button.ButtonPngIcon(
            self.back_button_image, 
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
        from components.media import sfx
        self.sfx = sfx()
    

    def change_state_menu(self):
        self.sfx.button_sound()
        from Interface.menu import MenuState
        self.engine.machine.next_state = MenuState(self.engine, self.user)
    

    def change_state_left(self):
        self.sfx.button_sound()
        if self.current_page == 1: 
            self.current_page -= 1

    def change_state_right(self):
        self.sfx.button_sound()
        if self.current_page == 0:  
            self.current_page += 1

    def on_draw(self, surface):
        if self.current_page == 0:
            surface.blit(self.tutorial_image_1, (0, 0))
            self.btn_right.draw(surface, 725, 275)
        else:
            surface.blit(self.tutorial_image_2, (0, 0))
            self.btn_left.draw(surface, 4, 260)
        self.btn_back.draw(surface, 0, 500)
        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Returning to menu screen")
                self.change_state_menu()
            if event.key == pygame.K_RIGHT:
                self.change_state_right()
            if event.key == pygame.K_LEFT:
                self.change_state_left()
        self.ui.handle_event(event)
