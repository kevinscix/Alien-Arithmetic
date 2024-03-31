from Interface.state_machine import State, DisplayEngine
from PygameUIKit import Group, button
import pygame
import os


class TutorialState(State):
    """
    Represents the tutorial state of the application, displaying tutorial pages to the user and allowing navigation between them.
    
    Attributes:
        engine (Engine): The game engine instance responsible for managing states.
        user (User): The current user's data, passed through various states.
        current_page (int): The index of the current tutorial page being displayed.
        ui (Group): A group of UI elements used in the tutorial state.
        tutorial_image_1, tutorial_image_2 (Surface): Images for the tutorial pages.
        back_button_image, left_button_image, right_button_image (Surface): Images for the navigation buttons.
        btn_back, btn_left, btn_right (ButtonPngIcon): Buttons for navigating the tutorial.
    """
    def __init__(self, engine, user):
        """
        Initializes the TutorialState with the necessary UI components and assigns the current user.
        
        Args:
            engine: The game engine instance responsible for managing states.
            user: The current user's data.
        """
        super().__init__(engine)
        # Initialize tutorial state attributes
        self.current_page = 0
        #UI Group to manage UI elements
        self.ui = Group()  
        self.user = user

        # Paths for UI elements such as buttons and backgrounds are defined here        
        # Load and scale images for tutorial pages and navigation buttons
        parent_dir = os.path.dirname(os.path.dirname(__file__) )  # __file__ is the path to the current script
        tutorial_image_path_1 = os.path.join(parent_dir,  "assets", "visuals", "pages - backgrounds", "tutorial page 1.png")
        self.tutorial_image_1 = pygame.image.load(os.path.normpath(tutorial_image_path_1))
        self.tutorial_image_1 = pygame.transform.scale(self.tutorial_image_1, (800, 600))
        tutorial_image_path_2 = os.path.join(parent_dir,  "assets", "visuals", "pages - backgrounds", "tutorial page 2.png")
        self.tutorial_image_2 = pygame.image.load(os.path.normpath(tutorial_image_path_2))
        self.tutorial_image_2 = pygame.transform.scale(self.tutorial_image_2, (800, 600))
        back_button_path = os.path.join(parent_dir,  "assets", "visuals", "buttons", "text buttons", "exitButton.png")
        self.back_button_image = pygame.image.load(os.path.normpath(back_button_path))
        self.back_button_image = pygame.transform.scale(self.back_button_image, (150, 100))
        left_button_path = os.path.join(parent_dir, "assets", "visuals", "buttons", "text buttons", "left button.png")
        right_button_path = os.path.join(parent_dir, "assets", "visuals", "buttons", "text buttons", "right button.png")
        self.left_button_image = pygame.image.load(os.path.normpath(left_button_path))
        self.left_button_image = pygame.transform.scale(self.left_button_image, (75, 100))
        self.right_button_image = pygame.image.load(os.path.normpath(right_button_path))
        self.right_button_image = pygame.transform.scale(self.right_button_image, (75, 100))

        # Initialize navigation buttons with their respective images and actions
        self.btn_back = button.ButtonPngIcon(
            self.back_button_image, 
            self.change_state_menu, 
            ui_group=self.ui
        )

        self.btn_left = button.ButtonPngIcon(
            self.left_button_image, 
            self.change_state_left, 
            ui_group=self.ui
        )
        self.btn_right = button.ButtonPngIcon(
            self.right_button_image, 
            self.change_state_right, 
            ui_group=self.ui
        )
        # Initialize sound effects
        from components.media import sfx
        self.sfx = sfx()
    

    def change_state_menu(self):
        """
        Transitions back to the main menu state.
        """
        # Button sound effect and logic to transition back to the menu state
        self.sfx.button_sound()
        from Interface.menu import MenuState
        self.engine.machine.next_state = MenuState(self.engine, self.user)
    

    def change_state_left(self):
        """
        Navigates to the next tutorial page if available.
        """
        # Button sound effect and logic for page navigation
        self.sfx.button_sound()
        if self.current_page == 1: 
            self.current_page -= 1

    def change_state_right(self):
        """
        Navigates to the next tutorial page if available.
        """
        # Button sound effect and logic for page navigation
        self.sfx.button_sound()
        if self.current_page == 0:  
            self.current_page += 1

    def on_draw(self, surface):
        """
        Draws the current tutorial page and navigation buttons onto the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the tutorial elements on.
        """
        # Logic to draw the tutorial page based on current page and navigation buttons on the surface
        if self.current_page == 0:
            surface.blit(self.tutorial_image_1, (0, 0))
            self.btn_right.draw(surface, 725, 275)
        else:
            surface.blit(self.tutorial_image_2, (0, 0))
            self.btn_left.draw(surface, 4, 260)
        self.btn_back.draw(surface, 0, 500)
        pygame.display.flip()

    def on_event(self, event):
        """
        Handles events within the tutorial state, such as button clicks and keyboard inputs, triggering appropriate navigation actions.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        # Logic to handle events, including keyboard inputs for navigation and button clicks
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Returning to menu screen")
                self.change_state_menu()
            if event.key == pygame.K_RIGHT:
                self.change_state_right()
            if event.key == pygame.K_LEFT:
                self.change_state_left()
        self.ui.handle_event(event)
