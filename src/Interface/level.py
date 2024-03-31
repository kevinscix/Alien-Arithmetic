import os
import sys
import pygame
from PygameUIKit import Group, button
from Interface.state_machine import State
from Interface.modules.state import SaveState
from Interface.game import GameState

parent_dir = os.path.dirname(os.path.dirname(__file__))  
quitImagePath = os.path.join(parent_dir, "assets", "visuals", "buttons", "text buttons", "exitButton.png")
quit_image = pygame.image.load(os.path.normpath(quitImagePath))
quit_image = pygame.transform.scale(quit_image, (150, 105))

class OuterLevelState(State):
    """
    Represents the state where users select the arithmetic operation mode (addition, subtraction, multiplication) for the game.

    Attributes:
        engine (Engine): The game engine instance responsible for managing states.
        user (SaveState): The current user's save state, containing user-specific data like name and progress.
        ui (Group): A group of UI elements used in the outer level state.
        level_select (Surface): The background image for level selection.
        x_asteroid, plus_asteroid, minus_asteroid (Surface): Images for the arithmetic operation selection buttons.
        btn_level_plus, btn_level_minus, btn_level_x (ButtonPngIcon): Buttons for selecting the arithmetic operation.
        btn_quit (ButtonPngIcon): Button to exit to the main menu.
        modes (dict): Dictionary mapping the operation modes to their corresponding integer values.
        max_level (int): The maximum level the user has unlocked.
    """
    def __init__(self, engine, user):
        """
        Initializes the OuterLevelState with the necessary UI components and assigns the current user's save state.

        Args:
            engine: The game engine instance responsible for managing states.
            user: The current user's save state.
        """
        super().__init__(engine)
        #UI Group to manage UI elements
        self.ui = Group()  
        self.user : SaveState = user

        # Load and scale images for level selection and operation buttons
        level_image_path = os.path.join(parent_dir, "assets", "visuals", "pages - backgrounds", "asteroid page.png")
        self.level_select = pygame.image.load(os.path.normpath(level_image_path))
        self.level_select= pygame.transform.scale(self.level_select, (800, 600))
        x_asteroid_path = os.path.join(parent_dir, "assets", "visuals", "stage-level select", "xAsteroid.png")
        self.x_asteroid = pygame.image.load(os.path.normpath(x_asteroid_path))
        self.x_asteroid= pygame.transform.scale(self.x_asteroid, (125, 125))
        plus_asteroid_path = os.path.join(parent_dir,"assets", "visuals", "stage-level select", "plusAsteroid.png")
        self.plus_asteroid = pygame.image.load(os.path.normpath(plus_asteroid_path))
        self.plus_asteroid= pygame.transform.scale(self.plus_asteroid, (125, 125))
        minus_asteroid_path = os.path.join(parent_dir,"assets", "visuals", "stage-level select", "minusAsteroid.png")
        self.minus_asteroid = pygame.image.load(os.path.normpath(minus_asteroid_path))
        self.minus_asteroid= pygame.transform.scale(self.minus_asteroid, (125, 125))

        self.modes = {
            "plus" : 1,
            "minus" : 2,
            "multiply" : 3
        }

        # Initialize operation selection buttons with their respective images and actions
        self.btn_level_plus = button.ButtonPngIcon(
            self.plus_asteroid,
            lambda: self.start_inner_state("plus"),
            ui_group=self.ui
        )

        self.btn_level_minus = button.ButtonPngIcon(
            self.minus_asteroid,
            lambda: self.start_inner_state("minus"),
            ui_group=self.ui
        )

        self.btn_level_x = button.ButtonPngIcon(
            self.x_asteroid,
            lambda: self.start_inner_state("multiply"),
            ui_group=self.ui
        )

        self.btn_quit = button.ButtonPngIcon(
            quit_image,
            self.change_state_exit,
            ui_group=self.ui
        )

        # Initialize sound effects and background music
        from components.media import music, sfx
        self.music = music()
        self.music.menu_music()
        self.sfx = sfx()


        # Determine the maximum level unlocked by the user and set button states accordingly
        self.max_level = self.user.level[0]
        if self.max_level == 1:
            self.btn_level_minus.hover_color = "red"
            self.btn_level_x.hover_color = "red"
        elif self.max_level == 2:
            self.btn_level_x.hover_color = "red"




    def start_inner_state(self, mode):
        """
        Transitions to the inner level state corresponding to the selected arithmetic operation mode.

        Args:
            mode (str): The selected arithmetic operation mode ('plus', 'minus', 'multiply').
        """
        # Button sound effect and logic to transition to the inner level state
        self.sfx.button_sound()
        if  self.modes[mode] <= self.max_level:
            self.engine.machine.next_state = InnerLevelState(self.engine, mode, self.user)


    def change_state_exit(self):
        """
        Transitions back to the main menu state.
        """
        # Button sound effect and logic to transition back to the menu state
        self.sfx.button_sound()
        from Interface.menu import MenuState
        self.engine.machine.next_state = MenuState(self.engine, self.user)

    def on_draw(self, surface):
        """
        Draws the outer level state's UI elements onto the given surface, including the background and operation selection buttons.

        Args:
            surface (pygame.Surface): The surface to draw the UI elements on.
        """
        # Logic to draw the background and operation selection buttons on the surface
        surface.blit(self.level_select , (0, 0))
        self.btn_level_plus.draw(surface, 260, 30)
        self.btn_level_minus.draw(surface, 415, 225)
        self.btn_level_x.draw(surface, 260, 435)
        self.btn_quit.draw(surface, 5, 485)
        pygame.display.flip()

    def on_event(self, event):
        """
        Handles events within the outer level state, such as button clicks and keyboard inputs, triggering appropriate actions.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        # Logic to handle events, including keyboard inputs for navigation and button clicks
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Returning to menu screen")
                self.change_state_exit()
        self.ui.handle_event(event)

      

class InnerLevelState(State):
    """
    Represents the state where users select the specific level within the chosen arithmetic operation mode.

    Attributes:
        engine (Engine): The game engine instance responsible for managing states.
        mode (str): The selected arithmetic operation mode.
        user (SaveState): The current user's save state.
        ui (Group): A group of UI elements used in the inner level state.
        level_select (Surface): The background image for specific level selection.
        levelOne, levelTwo, levelThree (Surface): Images for the specific level selection buttons.
        btn_level_one, btn_level_two, btn_level_three (ButtonPngIcon): Buttons for selecting a specific level.
        btn_quit (ButtonPngIcon): Button to exit to the outer level state.
        max_level (int): The maximum specific level the user has unlocked within the selected mode.
    """
    def __init__(self, engine, mode, user):
        """
        Initializes the InnerLevelState with the necessary UI components, the selected arithmetic operation mode, and the current user's save state.

        Args:
            engine: The game engine instance responsible for managing states.
            mode: The selected arithmetic operation mode.
            user: The current user's save state.
        """
        super().__init__(engine)
        self.mode = mode
        self.user :SaveState = user
        #UI Group to manage UI elements
        self.ui = Group()  
        # Load and scale images for specific level selection
        levelSelectPath = os.path.join(parent_dir, "assets", "visuals", "pages - backgrounds", "planet page.png")
        self.level_select = pygame.image.load(os.path.normpath(levelSelectPath))
        self.level_select= pygame.transform.scale(self.level_select, (800, 600))
        levelOnePath = os.path.join(parent_dir, "assets", "visuals", "stage-level select", "levelOne.png")
        self.levelOne = pygame.image.load(os.path.normpath(levelOnePath))
        self.levelOne= pygame.transform.scale(self.levelOne, (150, 125))
        levelTwoPath = os.path.join(parent_dir,"assets", "visuals", "stage-level select", "levelTwo.png")
        self.levelTwo = pygame.image.load(os.path.normpath(levelTwoPath))
        self.levelTwo = pygame.transform.scale(self.levelTwo, (150, 125))
        levelThreePath = os.path.join(parent_dir,"assets", "visuals", "stage-level select", "levelThree.png")
        self.levelThree = pygame.image.load(os.path.normpath(levelThreePath))
        self.levelThree = pygame.transform.scale(self.levelThree, (150, 125))


        # Initialize specific level selection buttons with their respective images and actions
        self.btn_level_one = button.ButtonPngIcon(
            self.levelOne,
            lambda: self.start_game_state(1),
            ui_group=self.ui
        )

        self.btn_level_two = button.ButtonPngIcon(
            self.levelTwo,
            lambda: self.start_game_state(2),
            ui_group=self.ui
        )

        self.btn_level_three = button.ButtonPngIcon(
            self.levelThree,
            lambda: self.start_game_state(3),
            ui_group=self.ui
        )

        self.btn_quit = button.ButtonPngIcon(
            quit_image,
            self.change_state_exit,
            ui_group=self.ui
        )
        # Initialize sound effects
        from components.media import sfx
        self.sfx = sfx()
        # Determine the maximum specific level unlocked by the user within the selected mode and set button states accordingly
        self.max_level = self.user.level[1]
        if self.max_level == 1:
            self.btn_level_two.hover_color = "red"
            self.btn_level_three.hover_color = "red"
        elif self.max_level == 2:
            self.btn_level_three.hover_color = "red"


    def start_game_state(self, level):
        """
        Transitions to the game state for the selected level and arithmetic operation mode.

        Args:
            level (int): The selected level number.
        """
        # Button sound effect and logic to transition to the game state
        self.sfx.button_sound()
        #if level is up to the required maxLevel then we can change the state else return locked
        if level <= self.max_level:
            self.engine.machine.next_state = GameState(self.engine, self.user, self.mode, level)


    def change_state_exit(self):
        """
        Transitions back to the outer level state.
        """
        # Button sound effect and logic to transition back to the outer level state
        self.sfx.button_sound()
        self.engine.machine.next_state = OuterLevelState(self.engine, self.user)

    def on_draw(self, surface):
        """
        Draws the inner level state's UI elements onto the given surface, including the background and specific level selection buttons.

        Args:
            surface (pygame.Surface): The surface to draw the UI elements on.
        """
        # Logic to draw the background and specific level selection buttons on the surface
        surface.blit(self.level_select , (0, 0))
        self.btn_level_one.draw(surface, 245, 35)
        self.btn_level_two.draw(surface, 405, 238)
        self.btn_level_three.draw(surface, 255, 445)
        self.btn_quit.draw(surface, 5, 485)
        pygame.display.flip()

    def on_event(self, event):
        """
        Handles events within the inner level state, such as button clicks and keyboard inputs, triggering appropriate actions.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        # Logic to handle events, including keyboard inputs for navigation and button clicks
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Returning to menu screen")
                self.change_state_exit()
        self.ui.handle_event(event)