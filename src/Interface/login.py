from state_machine import State, YourStateA, YourStateB, DisplayEngine
from PygameUIKit import Group, button
import pygame
import os


#this file is a quick scehem of how a state would look like for login and sign in state!

#this isn't importing properly???? ill figure it out or someone else can i give up
from modules.state import SaveModel

class LoginState(State):
    def __init__(self, engine):
        super().__init__(engine)
        self.background = 'white'
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter
        
        
        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        mainTitleImagePath = os.path.join(currentPath, "..", "src", "components", "Images", "titlePage.png")
        # Normalize the path to remove any '..'
        self.mainTitleImage = pygame.image.load(os.path.normpath(mainTitleImagePath))
    
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
        self.engine.machine.next_state = YourStateA(self.engine)

    #loads a instrctor model
    def change_state_instructor(self):
        #should be like  self.engine.machine.next_state = MENUSTATE(self.engine, self.instructor)

        self.engine.machine.next_state = YourStateB(self.engine)

    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.mainTitleImage, (0, 0))
        self.btn_start.draw(surface, *self.btn_start.surface.get_rect(center=(surface.get_height() // 2, surface.get_height()  // 2 - 50)).topleft)
        self.btn_quit.draw(surface, *self.btn_quit.surface.get_rect(center=(surface.get_width()  // 2, surface.get_height() // 2 + 50)).topleft)

        pygame.display.flip()

    def on_event(self, event):
        #theres no keyboard condition or still need to be determined
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         self.engine.machine.next_state = YourStateB(self.engine)
        self.ui.handle_event(event)


#make a state to search for a name?
class SignInState(State):
    pass 


if __name__ == "__main__":
    def main():
        pygame.init()
        engine = DisplayEngine('Example State machine', 60, 800, 600)
        engine.run(YourStateA(engine))
    pygame.quit()

    main()