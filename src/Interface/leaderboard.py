from Interface.state_machine import State, DisplayEngine
from PygameUIKit import Group, button
import pygame
from typing import List
import os



class LeaderboardState(State):
    """
    Represents the state of the application where the leaderboard is displayed, showing the top scores and the current user's score.

    Attributes:
        engine (Engine): The game engine instance responsible for managing states.
        user (User): The current user's data, passed through various states.
        ui (Group): A group of UI elements used in the leaderboard state.
        scoreboard_image (Surface): The background image for the leaderboard.
        back_button_image (Surface): The image for the back button.
        btn_back (ButtonPngIcon): The back button for returning to the main menu.
        leaderboard_data (List[SaveState]): A list containing the leaderboard data.
        font (Font): The font used for rendering the leaderboard text.
    """
    def __init__(self, engine, user):
        """
        Initializes the LeaderboardState with the necessary UI components and assigns the current user.

        Args:
            engine: The game engine instance responsible for managing states.
            user: The current user's data.
        """
        super().__init__(engine)

        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        self.user = user
        current_path = os.path.dirname(__file__)  
        parent_dir = os.path.dirname(current_path)  

        # Load and scale images for the leaderboard background and back button
        # Paths for UI elements such as buttons and backgrounds are defined here
        scoreboard_image_path = os.path.join(current_path, "..", "assets", "visuals", "pages - backgrounds", "student leaderboard page.png")
        back_button_path = os.path.join(current_path, "..", "assets", "visuals", "buttons", "text buttons", "exitButton.png")
        level_select_button_path = os.path.join(current_path, "..", "assets", "visuals", "buttons", "text buttons", "levelSelectButton.png")
        self.font_path = os.path.join(parent_dir, "assets", "visuals", "fonts", "PressStart2P-Regular.ttf")
        self.scoreboard_image = pygame.image.load(os.path.normpath(scoreboard_image_path))
        self.scoreboard_image = pygame.transform.scale(self.scoreboard_image, (830, 600))
        self.back_button_image = pygame.image.load(os.path.normpath(back_button_path))
        self.back_button_image = pygame.transform.scale(self.back_button_image, (150, 100))

        # Initialize the back button with its image and action
        self.btn_back = button.ButtonPngIcon(
            self.back_button_image, 
            self.change_state_menu, 
            ui_group=self.ui
        )

        # Initialize sound effects
        from components.media import sfx
        self.sfx = sfx()
        self.leaderboard_data = []
        # Create the leaderboard
        self.create_board()

    def create_board(self):
        """
        Fetches and prepares the leaderboard data for display.
        """
        # Logic to load scores and prepare leaderboard data
        # self.leaderboard_data is populated here
        from Interface.modules.state import ScoreboardState, SaveState
        self.scoreboard = ScoreboardState()
        scores : List[SaveState] = self.scoreboard.loadScore()
        self.leaderboard_data = []
        self.leaderboard_data = scores

    def change_state_menu(self):
        """
        Transitions back to the main menu state.
        """
        # Button sound effect and logic to transition back to the menu state
        from Interface.menu import MenuState
        self.sfx.button_sound()
        self.engine.machine.next_state = MenuState(self.engine, self.user)



    def on_draw(self, surface):
        """
        Draws the leaderboard state's UI elements onto the given surface, including the background, leaderboard text, and back button.

        Args:
            surface (pygame.Surface): The surface to draw the UI elements on.
        """
        # Logic to draw the background, leaderboard text, and back button on the surface
        #draws the titleImage on surface
        surface.blit(self.scoreboard_image, (-15, 0))

        y = 230
        self.font = pygame.font.Font(self.font_path, 25)

        for i, player in enumerate(self.leaderboard_data[:5], start=1):
            # Create text surfaces for the player's name, score, and logged-in status
            name_surface = self.font.render(f"{i}.{player.name}", True, (255, 255, 255))
            score_surface = self.font.render(str(player.score), True, (255, 255, 255))
            
            surface.blit(name_surface, (175, y))
            surface.blit(score_surface, (490, y))
            y += self.font.get_height() + 30

        main_score_surface = self.font.render(str(self.user.name) + ' score: ' + str(self.user.score), True, "red")
        surface.blit(main_score_surface, (160, 100))
        self.btn_back.draw(surface, 0, 500)
        pygame.display.flip()

    def on_event(self, event):
        """
        Handles events within the leaderboard state, such as button clicks and keyboard inputs, triggering appropriate actions.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        # Logic to handle events, including keyboard inputs for navigation and button clicks
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Returning to menu screen")
                self.change_state_menu()
        self.ui.handle_event(event)
