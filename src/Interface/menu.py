import os
import sys

#change directory
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)  # Moves up to 'interface'
src_dir = os.path.dirname(parent_dir)  # Moves up to 'src'
sys.path.append(src_dir)


#pygame imports
import pygame
from PygameUIKit import Group, button


#state imports
from Interface.state_machine import State
from Interface.modules.state import SaveModel
from Interface.tutorial import TutorialState
from Interface.leaderboard import LeaderboardState
from Interface.game import GameState
currentPath = os.path.dirname(__file__)  

menuImagePath = os.path.join(currentPath, "..", "components", "Images", "menuPage.png")
startImagePath = os.path.join(currentPath, "..", "components", "Images", "startButton.png")
loadImagePath = os.path.join(currentPath, "..", "components", "Images", "loadButton.png")
tutorialImagePath = os.path.join(currentPath, "..", "components", "Images", "tutorialButton.png")
highscoresImagePath = os.path.join(currentPath, "..", "components", "Images", "leaderboardButton.png")
quitImagePath = os.path.join(currentPath, "..", "components", "Images", "exitButton.png")

menuImage = pygame.image.load(os.path.normpath(menuImagePath))
menuImage= pygame.transform.scale(menuImage, (800, 600))
start_image = pygame.image.load(os.path.normpath(startImagePath))
start_image = pygame.transform.scale(start_image, (200, 75))
load_image = pygame.image.load(os.path.normpath(loadImagePath))
load_image = pygame.transform.scale(load_image, (200, 75))
tutorial_image = pygame.image.load(os.path.normpath(tutorialImagePath))
tutorial_image = pygame.transform.scale(tutorial_image, (75, 75))
highscores_image = pygame.image.load(os.path.normpath(highscoresImagePath))
highscores_image = pygame.transform.scale(highscores_image, (200, 75))
quit_image = pygame.image.load(os.path.normpath(quitImagePath))
quit_image = pygame.transform.scale(quit_image, (200, 75))


    
class MenuState(State):
    def __init__(self, engine):
        super().__init__(engine)
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter
        

        self.user : SaveModel = None

        # Start button
        self.btn_start = button.ButtonPngIcon(
            start_image, 
            self.change_state_start, 
            ui_group=self.ui
        )
        self.btn_load = button.ButtonPngIcon(
            load_image, 
            self.change_state_load, 
            ui_group=self.ui
        )
        self.btn_tutorial = button.ButtonPngIcon(
            tutorial_image, 
            self.change_state_tutorial, 
            ui_group=self.ui
        )
        self.btn_highscores = button.ButtonPngIcon(
            highscores_image, 
            self.change_state_highscore, 
            ui_group=self.ui
        )
        self.btn_quit = button.ButtonPngIcon(
            quit_image, 
            self.change_state_exit, 
            ui_group=self.ui
        )



    #IGNORE OUTLEVEL FOR NOW I WILL USE GAME STATE
    #implement game state file
    def change_state_start(self):
        self.engine.machine.next_state = GameState(self.engine)
        
    #call the singin state?
    def change_state_load(self):
        pass

    #call the tutorial state which will be just an image for now?
    def change_state_tutorial(self):
        self.engine.machine.next_state = TutorialState(self.engine)


    #do we jsut want to do a table of the top scores for the first 10?
    def change_state_highscore(self):
        self.engine.machine.next_state = LeaderboardState(self.engine)


    #quit functionality you can implement yourself
    def change_state_exit(self):
        from Interface.login import LoginState
        self.engine.machine.next_state = LoginState(self.engine)
 

    #Notes
        #I got rid of the visibility since its redundant if each state just changes the buttons entirely.
        #so i think this is fine. I wont delete the gameUI yet cause it might be useful for later
    def on_draw(self, surface):
        #change to real background?
        surface.blit(menuImage, (0, 0))

        self.btn_start.draw(surface, 300, 150)
        self.btn_load.draw(surface, 300, 350)
        self.btn_tutorial.draw(surface, 700, 400)
        self.btn_highscores.draw(surface, 550, 550)
        self.btn_quit.draw(surface, 0, 500) 
       
        pygame.display.flip()

    def on_event(self, event):
        #theres no keyboard condition or still need to be determined for menu
        self.ui.handle_event(event)
