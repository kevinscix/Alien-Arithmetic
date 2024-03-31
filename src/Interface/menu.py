import os
import sys
import pygame
from PygameUIKit import Group, button
from Interface.state_machine import State
from Interface.modules.state import SaveState
from Interface.tutorial import TutorialState
from Interface.leaderboard import LeaderboardState
from Interface.game import GameState
from Interface.level import OuterLevelState



class MenuState(State):
    """
    Represents the main menu state of the application, providing the user with various options like starting a new game,
    loading an existing game, accessing the tutorial, viewing high scores, or exiting the game.
    
    Attributes:
        engine (Engine): The game engine instance responsible for managing states.
        user (SaveState): The current user's save state, containing user-specific data like name and progress.
        ui (Group): A group of UI elements used in the menu state.
        menuImage (Surface): The background image for the menu.
        start_image, load_image, tutorial_image, highscores_image, quit_image (Surface): Images for the menu buttons.
        btn_start, btn_load, btn_tutorial, btn_highscores, btn_quit (ButtonPngIcon): Buttons for the menu options.
    """
    def __init__(self, engine, user):
        """
        Initializes the MenuState with the necessary UI components and assigns the current user's save state.

        Args:
            engine: The game engine instance responsible for managing states.
            user: The current user's save state, used to tailor the menu options.
        """
        super().__init__(engine)
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter
        self.user : SaveState = user


        # Load and scale images for the menu background and buttons
        # Paths for UI elements such as buttons and backgrounds are defined here
        # Loaded and scaled images accordingly
        parent_dir = os.path.dirname(os.path.dirname(__file__))  
        menu_image_path = os.path.join(parent_dir, "assets", "visuals", "pages - backgrounds", "main page.png")
        start_image_path = os.path.join(parent_dir, "assets", "visuals", "buttons", "text buttons", "startButton.png")
        load_image_path = os.path.join(parent_dir, "assets", "visuals", "buttons", "text buttons", "loadButton.png")
        tutorial_image_path = os.path.join(parent_dir, "assets", "visuals", "buttons", "text buttons", "tutorialButton.png")
        highscores_image_path = os.path.join(parent_dir, "assets", "visuals", "buttons", "text buttons", "leaderboardButton.png")
        quit_image_path = os.path.join(parent_dir, "assets", "visuals", "buttons", "text buttons", "exitButton.png")

        self.menu_image = pygame.image.load(os.path.normpath(menu_image_path))
        self.menu_image = pygame.transform.scale(self.menu_image, (800, 600))
        self.start_image = pygame.image.load(os.path.normpath(start_image_path))
        self.start_image = pygame.transform.scale(self.start_image, (225, 100))
        self.load_image = pygame.image.load(os.path.normpath(load_image_path))
        self.load_image = pygame.transform.scale(self.load_image, (225, 100))
        self.tutorial_image = pygame.image.load(os.path.normpath(tutorial_image_path))
        self.tutorial_image = pygame.transform.scale(self.tutorial_image, (75, 100))
        self.highscores_image = pygame.image.load(os.path.normpath(highscores_image_path))
        self.highscores_image = pygame.transform.scale(self.highscores_image, (240, 100))
        self.quit_image = pygame.image.load(os.path.normpath(quit_image_path))
        self.quit_image = pygame.transform.scale(self.quit_image, (150, 105))

        # Initialize buttons with their respective images and actions
        self.btn_start = button.ButtonPngIcon(
            self.start_image,
            self.change_state_start,
            ui_group=self.ui
        )
        self.btn_load = button.ButtonPngIcon(
            self.load_image,
            self.change_state_load,
            ui_group=self.ui
        )
        self.btn_tutorial = button.ButtonPngIcon(
            self.tutorial_image,
            self.change_state_tutorial,
            ui_group=self.ui
        )
        self.btn_highscores = button.ButtonPngIcon(
            self.highscores_image,
            self.change_state_highscore,
            ui_group=self.ui
        )
        self.btn_quit = button.ButtonPngIcon(
            self.quit_image,
            self.change_state_exit,
            ui_group=self.ui
        )
        # Initialize sound effects
        from components.media import sfx
        self.sfx = sfx()


    def change_state_start(self):
        """
        Transitions to the game start state, either by creating a new save state for a regular user
        or continuing with the instructor's save state.
        """
        # Button sound effect and logic to transition to the game start state
        if not self.user.name == "Instructor":
            self.sfx.button_sound()
            #give a clear savestate for user to start new
            newSave = SaveState(
                name=self.user.name,
                score=000,
                level=[1,1], #max level so they have access to all
                highScore=0000,
                questionsCompleted=000,
                incorrectAmt=0000,
                correctAmt=000,
                overallGrade=0000,
                loggedIn=True
            )
            newSave.save_settings(newSave.model_dump_json(), "{}".format(self.user.name))
            self.engine.machine.next_state = OuterLevelState(self.engine, newSave)
        else:
            self.engine.machine.next_state = OuterLevelState(self.engine, self.user)

    def change_state_load(self):
        """
        Transitions to the game load state, allowing the user to continue with their current save state.
        """
        # Button sound effect and logic to transition to the game load state
        self.sfx.button_sound()
        self.engine.machine.next_state = OuterLevelState(self.engine, self.user)


    #call the tutorial state which will be just an image for now?
    def change_state_tutorial(self):
        """
        Transitions to the tutorial state, where users can learn about the game's mechanics.
        """
        # Button sound effect and logic to transition to the tutorial state
        self.sfx.button_sound()
        self.engine.machine.next_state = TutorialState(self.engine, self.user)


    def change_state_highscore(self):
        """
        Transitions to the high score state, displaying the top scores from various users.
        """
        # Button sound effect and logic to transition to the high score state
        self.sfx.button_sound()
        self.engine.machine.next_state = LeaderboardState(self.engine, self.user)


    def change_state_exit(self):
        """
        Transitions back to the login state, effectively serving as an 'exit' or 'log out' option.
        """
        # Button sound effect and logic to transition back to the login state
        self.sfx.button_sound(  )
        from Interface.login import LoginState
        self.engine.machine.next_state = LoginState(self.engine)

    def on_draw(self, surface):
        """
        Draws the menu state's UI elements onto the given surface, including the background, buttons, and any other visuals.

        Args:
            surface (pygame.Surface): The surface to draw the UI elements on.
        """
        # Logic to draw the background, buttons, and potentially other UI elements on the surface

        surface.blit(self.menu_image, (0, 0))

        self.btn_start.draw(surface, 290, 180)
        self.btn_load.draw(surface, 290, 325)
        self.btn_tutorial.draw(surface, 710, 373)
        self.btn_highscores.draw(surface, 550, 487)
        self.btn_quit.draw(surface, 5, 485)

        pygame.display.flip()

    def on_event(self, event):
        """
        Handles events within the menu state, such as button clicks and keyboard inputs, triggering appropriate actions.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        # Logic to handle events, including keyboard inputs and button clicks
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Returning to menu screen")
                self.change_state_exit()
        self.ui.handle_event(event)