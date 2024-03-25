import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)  # Moves up to 'interface'
src_dir = os.path.dirname(parent_dir)  # Moves up to 'src'
sys.path.append(src_dir)

from Interface.state_machine import State
from Interface.menu import MenuState

from PygameUIKit import Group, button, text_input
import pygame

#this file is a quick scehem of how a state would look like for login and sign in state!

#this isn't importing properly???? ill figure it out or someone else can i give up
from Interface.modules.state import SaveModel


current_path = os.path.dirname(__file__)
student_login_image_path = os.path.join(current_path, "..", "components", "Images", "student_login.png")
teacher_login_image_path = os.path.join(current_path, "..", "components", "Images", "student_login.png")
quit_game_image_path = os.path.join(current_path, "..", "components", "Images", "student_login.png")
loginImagePath = os.path.join(current_path, "..", "components", "Images", "titlePage.png")

student_login_image = pygame.image.load(os.path.normpath(student_login_image_path))
student_login_image = pygame.transform.scale(student_login_image, (290, 90))
teacher_login_image = pygame.image.load(os.path.normpath(teacher_login_image_path))
teacher_login_image = pygame.transform.scale(teacher_login_image, (290, 90))
quit_game_image = pygame.image.load(os.path.normpath(quit_game_image_path))
quit_game_image = pygame.transform.scale(quit_game_image, (200, 75))
loginImage = pygame.image.load(os.path.normpath(loginImagePath))
loginImage = pygame.transform.scale(loginImage, (800, 600))


class LoginState(State):
    def __init__(self, engine):
        super().__init__(engine)

        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script


        self.instructor : SaveModel = SaveModel(
            name="Instructor",
            score=000,
            level=[3,3,3], #max level so they have access to all
            highScore=0000,
            questionsCompleted=000,
            incorrectAmt=0000,
            correctAmt=000,
            overallGrade=0000,
            loggedIn=True
        )
    
        self.student : SaveModel = None

        self.btn_student_login = button.ButtonPngIcon(student_login_image, self.change_state_student, ui_group=self.ui)
        self.btn_teacher_login = button.ButtonPngIcon(teacher_login_image, self.change_state_instructor, ui_group=self.ui)
        self.btn_quit_game = button.ButtonPngIcon(quit_game_image, self.quit_game, ui_group=self.ui)

    #pulls the player data with the empty player pull function
    def change_state_student(self):
        #should be like  self.engine.machine.next_state = MENUSTATE(self.engine, self.instructor)
        self.engine.machine.next_state = MenuState(self.engine)

    #loads a instrctor model
    def change_state_instructor(self):
        #should be like  self.engine.machine.next_state = MENUSTATE(self.engine, self.instructor)
        self.engine.machine.next_state = MenuState(self.engine)

    def quit_game(self):
       pygame.quit()

    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(loginImage, (0, 0))
        self.btn_student_login.draw(surface, 100, 460)
        self.btn_teacher_login.draw(surface, 425, 460)
        self.btn_quit_game.draw(surface, 300, 500)


        pygame.display.flip()

    def on_event(self, event):
        #theres no keyboard condition or still need to be determined
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         self.engine.machine.next_state = YourStateB(self.engine)
        self.ui.handle_event(event)

