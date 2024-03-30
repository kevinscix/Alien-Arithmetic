import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)  # Moves up to 'interface'
src_dir = os.path.dirname(parent_dir)  # Moves up to 'src'
sys.path.append(src_dir)

from Interface.state_machine import State
from Interface.menu import MenuState
from Interface.instructorDashboard import instructorState

from PygameUIKit import Group, button, text_input
import pygame

#this file is a quick scehem of how a state would look like for login and sign in state!

#this isn't importing properly???? ill figure it out or someone else can i give up
from Interface.modules.state import SaveState

class LoginState(State):
    def __init__(self, engine):
        super().__init__(engine)

        current_path = os.path.dirname(__file__)
        student_login_path = os.path.join(current_path, "..", "assets", "visuals", "buttons", "text buttons", "studentLogin.png")
        teacher_login_image_path = os.path.join(current_path, "..", "assets", "visuals", "buttons", "text buttons", "instructorLogin.png")
        quit_game_image_path = os.path.join(current_path, "..", "assets", "visuals", "buttons", "text buttons", "exitButton.png")
        loginImagePath = os.path.join(current_path, "..", "assets", "visuals", "pages - backgrounds", "log in page.png")

        self.teacher_login_image = pygame.image.load(os.path.normpath(teacher_login_image_path))
        self.teacher_login_image = pygame.transform.scale(self.teacher_login_image, (250, 100))
        self.student_login_image = pygame.image.load(os.path.normpath(student_login_path))
        self.student_login_image = pygame.transform.scale(self.student_login_image, (200, 100))
        self.quit_game_image = pygame.image.load(os.path.normpath(quit_game_image_path))
        self.quit_game_image = pygame.transform.scale(self.quit_game_image, (100, 75))
        self.loginImage = pygame.image.load(os.path.normpath(loginImagePath))
        self.loginImage = pygame.transform.scale(self.loginImage, (800, 600))

        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter
        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script


        self.instructor : SaveState = SaveState(
            name="Instructor",
            score=000,
            level=[3,3], #max level so they have access to all
            highScore=0000,
            questionsCompleted=000,
            incorrectAmt=0000,
            correctAmt=000,
            overallGrade=0000,
            loggedIn=True
        )

        self.student : SaveState = None
        self.text_input = text_input.TextInput(placeholder="Username/Password",
                                               fixed_width=400,
                                               border_radius=2,
                                               ui_group=self.ui,
                                               font=pygame.font.Font('freesansbold.ttf', 32))

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

        #music
        from components.media import music, sfx

        self.music = music()
        self.music.menu_music()
        self.sfx = sfx()

    #pulls the player data with the empty player pull function
    def change_state_student(self):
        self.sfx.button_sound()

        from Interface.modules.state import ScoreboardState
        bo = ScoreboardState()
        #if no text then don't let the users enter...
        #do we want an error system here
        if self.text_input.get_text():
            if self.text_input.get_text() == "dev123":
                self.engine.machine.next_state = MenuState(self.engine, self.instructor)
            else:
                Player = bo.getPlayer(playerName=self.text_input.get_text())
                #should be like  self.engine.machine.next_state = MENUSTATE(self.engine, self.instructor)
                #need to add an error message popup
                self.engine.machine.next_state = MenuState(self.engine, Player)

    #loads a instrctor model
    def change_state_instructor(self):
        self.sfx.button_sound()
        if self.text_input.get_text() == "yourMom": #temp password
            self.engine.machine.next_state = instructorState(self.engine)

    def quit_game(self):
       self.sfx.button_sound()

       pygame.quit()

    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.loginImage, (0, 0))
        self.btn_student_login.draw(surface, 125, 450)
        self.btn_teacher_login.draw(surface, 427, 450)
        self.btn_quit_game.draw(surface, 0, 525)
        pygame.draw.rect(surface, "gray31", pygame.Rect(200, 350, 400, 40))
        self.text_input.draw(surface, 200, 350)

        pygame.display.flip()


    def on_event(self, event):
        self.ui.handle_event(event)

        self.text_input._handle_event(event)
        if not self.text_input.active:
            return
        pressed = pygame.key.get_pressed()

        for key in [pygame.K_BACKSPACE, pygame.K_LEFT, pygame.K_RIGHT] + [i for i in range(32, 127)]:
            if not pressed[key] or not self.text_input.should_handle_key(key):
                continue
            self.text_input.handle_key(key)
