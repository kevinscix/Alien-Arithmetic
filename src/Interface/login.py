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
        menuImagePath = os.path.join(currentPath, "..", "components", "Images", "titlePage.png")
        # Normalize the path to remove any '..'
        self.mainTitleImage = pygame.image.load(os.path.normpath(menuImagePath))
        self.mainTitleImage= pygame.transform.scale(self.mainTitleImage, (800, 600))

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

    #pulls the player data with the empty player pull function
    def change_state_student(self):
        #should be like  self.engine.machine.next_state = MENUSTATE(self.engine, self.instructor)
        self.engine.machine.next_state = SignInState(self.engine)

    #loads a instrctor model
    def change_state_instructor(self):
        #should be like  self.engine.machine.next_state = MENUSTATE(self.engine, self.instructor)

        self.engine.machine.next_state = MenuState(self.engine)

    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.mainTitleImage, (0, 0))
        self.btn_studentLogin.draw(surface, *self.btn_studentLogin.surface.get_rect(center=(surface.get_height() // 2, surface.get_height()  // 2 - 50)).topleft)
        self.btn_teacherLogin.draw(surface, *self.btn_teacherLogin.surface.get_rect(center=(surface.get_width()  // 2, surface.get_height() // 2 + 50)).topleft)

        pygame.display.flip()

    def on_event(self, event):
        #theres no keyboard condition or still need to be determined
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         self.engine.machine.next_state = YourStateB(self.engine)
        self.ui.handle_event(event)



#make a state to search for a name?
class SignInState(State):
    def __init__(self, engine):
        super().__init__(engine)
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        signinImagePath = os.path.join(currentPath, "..", "components", "Images", "loadScreen.png")
        # Normalize the path to remove any '..'
        self.signinImagePath = pygame.image.load(os.path.normpath(signinImagePath))
        self.signinImagePath= pygame.transform.scale(self.signinImagePath, (800, 600))
        
        # new game
        self.btn_new_game = button.ButtonText(
            "NEW GAME", 
            self.new_game_state,
            fixed_width=200,  
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )

        # load game
        self.btn_pre_game = button.ButtonText(
            "LOAD GAME", 
            self.load_game_state, 
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
       
        # load game
        self.btn_leaderboard = button.ButtonText(
            "Leader Board", 
            self.change_state_leaderboard, 
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )

        #exit button
        self.btn_exit = button.ButtonText(
            "EXIT", 
            self.change_state_exit, 
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )

        self.load_text_input = text_input.TextInput(
            text="",
            font=pygame.font.Font(pygame.font.get_default_font(), 30),
            fixed_width=200, 
            border_radius=10,
            placeholder="",
            ui_group=self.ui
        )
    
    def new_game_state(self):
        print("loaded new game")

    def load_game_state(self):
        print("loaded previous game")

    def change_state_leaderboard(self):
        pass

    def change_state_exit(self):
        self.engine.machine.next_state = MenuState(self.engine)
    
    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.signinImagePath, (0, 0))
        self.btn_new_game.draw(surface, *self.btn_new_game.surface.get_rect(center=(surface.get_width()  // 2, surface.get_height() // 2 + 50)).topleft)
        self.btn_pre_game.draw(surface, *self.btn_pre_game.surface.get_rect(center=(surface.get_height() // 2, surface.get_height()  // 2 - 50)).topleft)
        self.btn_leaderboard.draw(surface, *self.btn_leaderboard.surface.get_rect(center=(surface.get_height() // 2, surface.get_height()  // 2 - 100)).topleft)
        self.btn_exit.draw(surface, *self.btn_exit.surface.get_rect(center=(surface.get_height() // 2, surface.get_height()  // 2 + 100)).topleft)
        self.load_text_input.draw(surface, *self.btn_exit.surface.get_rect(center=(surface.get_height() // 2, surface.get_height()  // 2 + 200)).topleft)
        pygame.display.flip()

    def on_event(self, event):
        #theres no keyboard condition or still need to be determined
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         self.engine.machine.next_state = YourStateB(self.engine)
        self.ui.handle_event(event)

