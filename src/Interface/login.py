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

class LoginState(State):
    def __init__(self, engine):
        super().__init__(engine)

        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        loginImagePath = os.path.join(currentPath, "..", "components", "Images", "titlePage.png")
        # Normalize the path to remove any '..'
        self.loginImagePath = pygame.image.load(os.path.normpath(loginImagePath))
        self.loginImagePath= pygame.transform.scale(self.loginImagePath, (800, 600))

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

       # Student Login button
        self.btn_studentLogin = button.ButtonText(
            "Student Login", 
            self.change_state_student, 
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
        # Teacher Login button
        self.btn_teacherLogin = button.ButtonText(
            "Teacher login", 
            self.change_state_instructor, 
            fixed_width=200,  
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )

        # Quit game
        self.btn_teacherLogin = button.ButtonText(
            "Quit Game", 
            self.change_state_instructor, 
            fixed_width=200,  
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )

    #pulls the player data with the empty player pull function
    def change_state_student(self):
        #should be like  self.engine.machine.next_state = MENUSTATE(self.engine, self.instructor)
        self.engine.machine.next_state = MenuState(self.engine)

    #loads a instrctor model
    def change_state_instructor(self):
        #should be like  self.engine.machine.next_state = MENUSTATE(self.engine, self.instructor)

        self.engine.machine.next_state = MenuState(self.engine)

    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.loginImagePath, (0, 0))
        self.btn_studentLogin.draw(surface, *self.btn_studentLogin.surface.get_rect(center=(surface.get_height() // 2, surface.get_height()  // 2 - 50)).topleft)
        self.btn_teacherLogin.draw(surface, *self.btn_teacherLogin.surface.get_rect(center=(surface.get_width()  // 2, surface.get_height() // 2 + 50)).topleft)

        pygame.display.flip()

    def on_event(self, event):
        #theres no keyboard condition or still need to be determined
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         self.engine.machine.next_state = YourStateB(self.engine)
        self.ui.handle_event(event)

