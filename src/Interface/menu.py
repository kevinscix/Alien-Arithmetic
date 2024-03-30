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
from Interface.modules.state import SaveState
from Interface.tutorial import TutorialState
from Interface.leaderboard import LeaderboardState
from Interface.game import GameState
from Interface.level import OuterLevelState
currentPath = os.path.dirname(__file__)





class MenuState(State):
    def __init__(self, engine, user):
        super().__init__(engine)
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter
        self.user : SaveState = user

        self.menuImagePath = os.path.join(currentPath, "..", "components", "Images", "menuPage.png")
        startImagePath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "startButton.png")
        loadImagePath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "loadButton.png")
        tutorialImagePath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "tutorialButton.png")
        highscoresImagePath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "leaderboardButton.png")
        quitImagePath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "exitButton.png")

        self.menuImage = pygame.image.load(os.path.normpath(self.menuImagePath))
        self.menuImage= pygame.transform.scale(self.menuImage, (800, 600))
        self.start_image = pygame.image.load(os.path.normpath(startImagePath))
        self.start_image = pygame.transform.scale(self.start_image, (225, 100))
        self.load_image = pygame.image.load(os.path.normpath(loadImagePath))
        self.load_image = pygame.transform.scale(self.load_image, (225, 100))
        self.tutorial_image = pygame.image.load(os.path.normpath(tutorialImagePath))
        self.tutorial_image = pygame.transform.scale(self.tutorial_image, (75, 100))
        self.highscores_image = pygame.image.load(os.path.normpath(highscoresImagePath))
        self.highscores_image = pygame.transform.scale(self.highscores_image, (240, 100))
        self.quit_image = pygame.image.load(os.path.normpath(quitImagePath))
        self.quit_image = pygame.transform.scale(self.quit_image, (150, 105))


        # Start button
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

        from components.media import sfx
        self.sfx = sfx()

    #IGNORE OUTLEVEL FOR NOW I WILL USE GAME STATE
    #implement game state file
    def change_state_start(self):
        self.sfx.button_sound()
        #give a clear file
        self.engine.machine.next_state = OuterLevelState(self.engine, self.user)

    #call the singin state?
    def change_state_load(self):
        self.sfx.button_sound()
        #contiue with current user
        self.engine.machine.next_state = OuterLevelState(self.engine, self.user)


    #call the tutorial state which will be just an image for now?
    def change_state_tutorial(self):
        self.sfx.button_sound()
        self.engine.machine.next_state = TutorialState(self.engine, self.user)


    #do we jsut want to do a table of the top scores for the first 10?
    def change_state_highscore(self):
        self.sfx.button_sound()
        self.engine.machine.next_state = LeaderboardState(self.engine, self.user)


    #quit functionality you can implement yourself
    def change_state_exit(self):
        self.sfx.button_sound(  )
        from Interface.login import LoginState
        self.engine.machine.next_state = LoginState(self.engine)


    #Notes
        #I got rid of the visibility since its redundant if each state just changes the buttons entirely.
        #so i think this is fine. I wont delete the gameUI yet cause it might be useful for later
    def on_draw(self, surface):
        #change to real background?
        surface.blit(self.menuImage, (0, 0))

        self.btn_start.draw(surface, 290, 180)
        self.btn_load.draw(surface, 290, 325)
        self.btn_tutorial.draw(surface, 710, 373)
        self.btn_highscores.draw(surface, 550, 487)
        self.btn_quit.draw(surface, 5, 485)

        pygame.display.flip()

    def on_event(self, event):
        #theres no keyboard condition or still need to be determined for menu
        self.ui.handle_event(event)





