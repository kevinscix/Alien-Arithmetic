from Interface.state_machine import State, DisplayEngine
from PygameUIKit import Group, button
import pygame
from typing import List
import os

#comments
# do we need any interactions from this state


class instructorState(State):
    """
    Represents the state of the application where the instructor can view a leaderboard with detailed student performance metrics.

    Attributes:
        engine (Engine): The game engine instance responsible for managing states.
        currentPage (int): The current page of the leaderboard being displayed.
        ui (Group): A group of UI elements used in the instructor state.
        instructor_image (Surface): The background image for the instructor leaderboard.
        back_button_image, left_button_image, right_button_image (Surface): Images for navigation and logout buttons.
        btn_back, btn_left, btn_right (ButtonPngIcon): Buttons for navigation and logging out.
        leaderboard_data (List[SaveState]): A list containing the leaderboard data for all students.
        displayed_scores (List[SaveState]): A subset of `leaderboard_data` currently being displayed on the screen.
        start_index, end_index (int): Indices defining the range of scores currently displayed.
    """
    def __init__(self, engine):
        """
        Initializes the instructorState with the necessary UI components.

        Args:
            engine: The game engine instance responsible for managing states.
        """
        super().__init__(engine)
        # Initialize the current page of the leaderboard
        self.currentPage = 0  

        #UI Group to manage UI elements
        self.ui = Group() 
        parent_path = os.path.dirname(os.path.dirname(__file__))
        # Load and scale images for the leaderboard background and navigation/logout buttons
        instructor_image_path = os.path.join(parent_path, "assets", "visuals", "pages - backgrounds", "instructor leaderboard page.png")
        back_button_path = os.path.join(parent_path, "assets", "visuals", "buttons", "text buttons", "logOutButton.png")
        left_button_path = os.path.join(parent_path,"assets", "visuals", "buttons", "text buttons", "left button.png")
        right_button_path = os.path.join(parent_path,"assets", "visuals", "buttons", "text buttons", "right button.png")
        self.font_path = os.path.join(parent_path, "assets", "visuals", "fonts", "PressStart2P-Regular.ttf")
        self.instructor_image = pygame.image.load(os.path.normpath(instructor_image_path))
        self.instructor_image = pygame.transform.scale(self.instructor_image, (840, 600))
        self.back_button_image = pygame.image.load(os.path.normpath(back_button_path))
        self.back_button_image = pygame.transform.scale(self.back_button_image, (150, 100))
        self.left_button_image = pygame.image.load(os.path.normpath(left_button_path))
        self.left_button_image = pygame.transform.scale(self.left_button_image, (75, 100))
        self.right_button_image = pygame.image.load(os.path.normpath(right_button_path))
        self.right_button_image = pygame.transform.scale(self.right_button_image, (75, 100))




        # Initialize navigation and logout buttons with their respective images and actions
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
        self.leaderboard_data = []
        # Fetch and prepare the initial leaderboard data
        self.createBoard()

    def createBoard(self):
        """
        Fetches and prepares the leaderboard data for display, paginating results based on `currentPage`.
        """
        # Load scores and paginate them based on `currentPage`
        # Update `displayed_scores` to contain only the scores for the current page
        from Interface.modules.state import ScoreboardState, SaveState
        self.scoreboard = ScoreboardState()
        scores : List[SaveState] = self.scoreboard.loadScore()
        self.leaderboard_data = []
        self.leaderboard_data = scores
        self.start_index = self.currentPage * 5
        self.end_index = self.start_index + 5
        self.displayed_scores = self.leaderboard_data[self.start_index:self.end_index]

    def change_state_menu(self):
        """
        Transitions back to the login state, effectively logging the instructor out.
        """
        # Button sound effect and logic to transition back to the login state
        self.sfx.button_sound()
        from Interface.login import LoginState
        self.engine.machine.next_state = LoginState(self.engine)

    def change_state_left(self):
        """
        Navigates to the previous page of the leaderboard, if available.
        """
        # Button sound effect and logic for page navigation
        self.sfx.button_sound()
        if self.currentPage > 0: 
            self.currentPage -= 1

    def change_state_right(self):
        """
        Navigates to the next page of the leaderboard, if there are more pages available.
        """
        # Button sound effect and logic for page navigation
        self.sfx.button_sound()
        leaderboard_data = self.createBoard()
        total_pages = (len(self.leaderboard_data) + 4) // 5  
        if self.currentPage + 1 < total_pages:  
            self.currentPage += 1

    def on_draw(self, surface):
        """
        Draws the instructor state's UI elements onto the given surface, including the leaderboard, navigation buttons, and logout button.

        Args:
            surface (pygame.Surface): The surface to draw the UI elements on.
        """
        # Logic to draw the background, leaderboard data, and navigation/logout buttons on the surface
        #draws the titleImage on surface
        surface.blit(self.instructor_image, (-25, 0))

        leaderboard_data = self.createBoard()
        self.font = pygame.font.Font(self.font_path, 18)
        #change for loop to have the number 5 and its start be variables passed 
        #to a function that will change its numbers either 
        #+5 or -5 based on left or right button
        # initial y position for the first score
        y = 200
        try: 
            for i, player in enumerate(self.displayed_scores, start=self.start_index + 1):
                name_surface = self.font.render(f"{player.name}", True, (255, 255, 255))
                level_surface = self.font.render(f"{player.level}", True, (255, 255, 255))
                completed_surface = self.font.render(f"{player.questionsCompleted}", True, (255, 255, 255))
                correct_surface = self.font.render(f"{player.correctAmt}", True, (255, 255, 255))
                score_surface = self.font.render(str(player.score), True, (255, 255, 255))
                surface.blit(name_surface, (85, y))
                surface.blit(level_surface, (220, y))
                surface.blit(completed_surface, (500, y))
                surface.blit(correct_surface, (370, y))
                surface.blit(score_surface, (590, y))
                y += self.font.get_height() + 40

        except:
            pass
        self.btn_left.draw(surface, -3, 250)
        self.btn_right.draw(surface, 728, 250)
        self.btn_back.draw(surface, 0, 500)
        pygame.display.flip()

    def on_event(self, event):
        """
        Handles events within the instructor state, such as button clicks and keyboard inputs, triggering appropriate actions.

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
