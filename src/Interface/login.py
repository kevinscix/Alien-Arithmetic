import sys
import os
import pygame
from Interface.state_machine import State
from Interface.menu import MenuState
from Interface.instructorDashboard import instructorState
from Interface.modules.state import SaveState
from PygameUIKit import Group, button, text_input

class LoginState(State):
    """
    Represents the login state of the application, providing interfaces for user authentication.
    
    This state allows users to log in as either students or instructors, providing different
    functionalities based on the role. It also provides a quit option to exit the application.
    """
    def __init__(self, engine):
        """
        Initializes the LoginState with necessary UI components and assets.

        Args:
            engine: The game engine instance responsible for managing states.
        """
        super().__init__(engine)
        # Resolve paths for assets
        parent_dir = os.path.dirname(os.path.dirname(__file__))  

        # Paths for UI elements such as buttons and backgrounds
        student_login_path = os.path.join(parent_dir, "assets", "visuals", "buttons", "text buttons", "studentLogin.png")
        teacher_login_image_path = os.path.join(parent_dir, "assets", "visuals", "buttons", "text buttons", "instructorLogin.png")
        quit_game_image_path = os.path.join(parent_dir, "assets", "visuals", "buttons", "text buttons", "exitButton.png")
        loginImagePath = os.path.join(parent_dir, "assets", "visuals", "pages - backgrounds", "log in page.png")
        # Path for the font used in the login screen
        self.font_path = os.path.join(parent_dir,"assets", "visuals", "fonts", "PressStart2P-Regular.ttf")
        # Load images and scale them to appropriate sizes
        self.teacher_login_image = pygame.image.load(os.path.normpath(teacher_login_image_path))
        self.teacher_login_image = pygame.transform.scale(self.teacher_login_image, (250, 100))
        self.student_login_image = pygame.image.load(os.path.normpath(student_login_path))
        self.student_login_image = pygame.transform.scale(self.student_login_image, (200, 100))
        self.quit_game_image = pygame.image.load(os.path.normpath(quit_game_image_path))
        self.quit_game_image = pygame.transform.scale(self.quit_game_image, (100, 75))
        self.loginImage = pygame.image.load(os.path.normpath(loginImagePath))
        self.loginImage = pygame.transform.scale(self.loginImage, (800, 600))

        #UI Group to manage UI elements
        self.ui = Group() 

        # Define default instructor state for quick access
        self.instructor : SaveState = SaveState(
            name="Instructor",
            score=000,
            level=[3,3], # Max level so they have access to all levels
            highScore=0000,
            questionsCompleted=000,
            incorrectAmt=0000,
            correctAmt=000,
            overallGrade=0000,
            loggedIn=True
        )

        self.font = pygame.font.Font(self.font_path, 25)
        
        # Initialize UI components like buttons and text inputs
        self.text_input = text_input.TextInput(placeholder="Username/Password",
                                               fixed_width=400,
                                               border_radius=2,
                                               ui_group=self.ui,
                                               font=pygame.font.Font(self.font_path, 23))

        self.btn_student_login = button.ButtonPngIcon(
            self.student_login_image,
            self.change_state_student,
            ui_group=self.ui
        )
        self.btn_teacher_login = button.ButtonPngIcon(
            self.teacher_login_image,
            self.change_state_instructor,
            ui_group=self.ui
        )
        self.btn_quit_game = button.ButtonPngIcon(
            self.quit_game_image,
            self.quit_game,
            ui_group=self.ui
        )

        self.error_messages = [] # For displaying error messages to the user


        # Initialize background music and sound effects
        from components.media import music, sfx
        self.music = music()
        self.music.menu_music()
        self.sfx = sfx()

    #pulls the player data with the empty player pull function
    def change_state_student(self):
        """
        Changes the current state to a student-specific state, after validating user input.
        
        If the user input is valid, the state is changed to a student-specific menu state.
        Otherwise, error messages are updated to reflect the issue.
        """
        self.sfx.button_sound()
        from Interface.modules.state import ScoreboardState
        bo = ScoreboardState()
        if self.text_input.get_text():
            if self.text_input.get_text() == "dev123": # Developer mode password
                self.engine.machine.next_state = MenuState(self.engine, self.instructor)
            elif len(self.text_input.get_text()) > 7: # 
                msg = {
                    'message' : self.font.render("Exceeds max name 7", True, (255, 0, 0)),
                }
                self.error_messages = msg
                print("too big")
            else:
                Player = bo.getPlayer(playerName=self.text_input.get_text())
                self.engine.machine.next_state = MenuState(self.engine, Player)
        else:
            msg = {
                    'message' : self.font.render("Empty Username", True, (255, 0, 0)),
                }
            self.error_messages = msg

    #loads a instrctor model
    def change_state_instructor(self):
        """
        Changes the current state to an instructor-specific state after verifying the password.

        The instructor state provides different functionalities tailored for instructors. If the
        password input does not match the expected value, an error message is displayed.
        """
        self.sfx.button_sound()
        if self.text_input.get_text() == "2212Admin": # Password for instructor 
            self.engine.machine.next_state = instructorState(self.engine)
        else:
            msg = {
                    'message' :  self.font.render("Wrong password", True, (255, 0, 0)),
                }
            self.error_messages = msg

    def quit_game(self):
        """
        Exits the game cleanly by stopping all Pygame modules.

        This method is triggered when the quit button is clicked or ESC key is pressed.
        """
        self.sfx.button_sound()

        pygame.quit()


    def on_draw(self, surface):
        """
        Draws the login state's UI elements onto the given surface.

        This includes the background, buttons, text input field, and any error messages.

        Args:
            surface: The Pygame surface to draw the UI elements on.
        """
        # Draw background image
        surface.blit(self.loginImage, (0, 0))
        self.btn_student_login.draw(surface, 125, 450)
        self.btn_teacher_login.draw(surface, 427, 450)
        self.btn_quit_game.draw(surface, 0, 525)
        # Draw UI elements: student login, instructor login, and quit game buttons
        pygame.draw.rect(surface, "gray31", pygame.Rect(180, 350, 400, 34))
        self.text_input.draw(surface, 180, 350)

        # Draw any error messages
        try:
            surface.blit(self.error_messages['message'], [190,400])
        except:
            # No error messages to display
            pass
        pygame.display.flip()


    def on_event(self, event):
        """
        Handles events such as keyboard input and button clicks within the login state.

        This method processes user interactions and triggers corresponding actions, such as
        changing states or updating the text input field.

        Args:
            event: The Pygame event to handle.
        """
        if event.type == pygame.KEYDOWN:
            # Exit the game if the ESC key is pressed
            if event.key == pygame.K_ESCAPE:
                print("Returning to menu screen")
                self.quit_game()
            # Attempts to login as a student when the Enter key is pressed
            if event.key == pygame.K_RETURN:
                self.change_state_student()
        self.ui.handle_event(event)
        # Pass the event to the UI elements for further processing
        self.text_input._handle_event(event)
        # Additional logic for text input handling (e.g., key presses for username/password)
        if not self.text_input.active:
            return
        for key in [pygame.K_BACKSPACE, pygame.K_LEFT, pygame.K_RIGHT] + [i for i in range(32, 127)]:
            pressed = pygame.key.get_pressed()
        for key in [pygame.K_BACKSPACE, pygame.K_LEFT, pygame.K_RIGHT] + [i for i in range(32, 127)]:
            if not pressed[key] or not self.text_input.should_handle_key(key):
                continue
            self.text_input.handle_key(key)
        
