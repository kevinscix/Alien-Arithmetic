import os
import sys
import pygame
#change directory
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  
sys.path.append(src_dir)
from Interface.state_machine import State
from Interface.modules.state import SaveState
from Interface.game import GameState
from PygameUIKit import Group, button

parent_dir = os.path.dirname(os.path.dirname(__file__))  
quitImagePath = os.path.join(parent_dir, "assets", "visuals", "buttons", "text buttons", "exitButton.png")
quit_image = pygame.image.load(os.path.normpath(quitImagePath))
quit_image = pygame.transform.scale(quit_image, (150, 105))

class OuterLevelState(State):
    def __init__(self, engine, user):
        super().__init__(engine)
        #UI
        self.ui = Group()  
        self.user : SaveState = user

        #make this into a utils function?
        level_image_path = os.path.join(parent_dir, "assets", "visuals", "pages - backgrounds", "asteroid page.png")
        self.level_select = pygame.image.load(os.path.normpath(level_image_path))
        self.level_select= pygame.transform.scale(self.level_select, (800, 600))
        x_asteroid_path = os.path.join(parent_dir, "assets", "visuals", "stage-level select", "xAsteroid.png")
        self.x_asteroid = pygame.image.load(os.path.normpath(x_asteroid_path))
        self.x_asteroid= pygame.transform.scale(self.x_asteroid, (125, 125))
        plus_asteroid_path = os.path.join(parent_dir,"assets", "visuals", "stage-level select", "plusAsteroid.png")
        self.plus_asteroid = pygame.image.load(os.path.normpath(plus_asteroid_path))
        self.plus_asteroid= pygame.transform.scale(self.plus_asteroid, (125, 125))
        minus_asteroid_path = os.path.join(parent_dir,"assets", "visuals", "stage-level select", "minusAsteroid.png")
        self.minus_asteroid = pygame.image.load(os.path.normpath(minus_asteroid_path))
        self.minus_asteroid= pygame.transform.scale(self.minus_asteroid, (125, 125))

        self.modes = {
            "plus" : 1,
            "minus" : 2,
            "multiply" : 3
        }

       # Student Login button
        self.btn_level_plus = button.ButtonPngIcon(
            self.plus_asteroid,
            lambda: self.start_inner_state("plus"),
            ui_group=self.ui
        )

        self.btn_level_minus = button.ButtonPngIcon(
            self.minus_asteroid,
            lambda: self.start_inner_state("minus"),
            ui_group=self.ui
        )

        self.btn_level_x = button.ButtonPngIcon(
            self.x_asteroid,
            lambda: self.start_inner_state("multiply"),
            ui_group=self.ui
        )

        self.btn_quit = button.ButtonPngIcon(
            quit_image,
            self.change_state_exit,
            ui_group=self.ui
        )
        from components.media import music, sfx
        self.music = music()
        self.music.menu_music()
        self.sfx = sfx()


        #determine max level
        self.max_level = self.user.level[0]
        if self.max_level == 1:
            self.btn_level_minus.hover_color = "red"
            self.btn_level_x.hover_color = "red"
        elif self.max_level == 2:
            self.btn_level_x.hover_color = "red"




    def start_inner_state(self, mode):
        self.sfx.button_sound()
        if  self.modes[mode] <= self.max_level:
            self.engine.machine.next_state = InnerLevelState(self.engine, mode, self.user)


    def change_state_exit(self):
        self.sfx.button_sound()
        from Interface.menu import MenuState
        self.engine.machine.next_state = MenuState(self.engine, self.user)

    def on_draw(self, surface):
        surface.blit(self.level_select , (0, 0))

        self.btn_level_plus.draw(surface, 260, 30)
        self.btn_level_minus.draw(surface, 415, 225)
        self.btn_level_x.draw(surface, 260, 435)
        self.btn_quit.draw(surface, 5, 485)


        #add the buttons we need should be 3 for the diff levels
        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Returning to menu screen")
                self.change_state_exit()
        self.ui.handle_event(event)

      

class InnerLevelState(State):
    def __init__(self, engine, mode, user):
        super().__init__(engine)

        self.mode = mode
        self.user :SaveState = user
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter
        #make this into a utils function?

        levelSelectPath = os.path.join(currentPath, "..", "assets", "visuals", "pages - backgrounds", "planet page.png")
        self.level_select = pygame.image.load(os.path.normpath(levelSelectPath))
        self.level_select= pygame.transform.scale(self.level_select, (800, 600))
        levelOnePath = os.path.join(currentPath, "..", "assets", "visuals", "stage-level select", "levelOne.png")
        self.levelOne = pygame.image.load(os.path.normpath(levelOnePath))
        self.levelOne= pygame.transform.scale(self.levelOne, (150, 125))
        levelTwoPath = os.path.join(currentPath, "..","assets", "visuals", "stage-level select", "levelTwo.png")
        self.levelTwo = pygame.image.load(os.path.normpath(levelTwoPath))
        self.levelTwo = pygame.transform.scale(self.levelTwo, (150, 125))
        levelThreePath = os.path.join(currentPath, "..","assets", "visuals", "stage-level select", "levelThree.png")
        self.levelThree = pygame.image.load(os.path.normpath(levelThreePath))
        self.levelThree = pygame.transform.scale(self.levelThree, (150, 125))


       # Student Login button
        self.btn_level_one = button.ButtonPngIcon(
            self.levelOne,
            lambda: self.start_game_state(1),
            ui_group=self.ui
        )

        self.btn_level_two = button.ButtonPngIcon(
            self.levelTwo,
            lambda: self.start_game_state(2),
            ui_group=self.ui
        )

        self.btn_level_three = button.ButtonPngIcon(
            self.levelThree,
            lambda: self.start_game_state(3),
            ui_group=self.ui
        )

        self.btn_quit = button.ButtonPngIcon(
            quit_image,
            self.change_state_exit,
            ui_group=self.ui
        )
        from components.media import sfx
        self.sfx = sfx()

        self.max_level = self.user.level[1]
        if self.max_level == 1:
            self.btn_level_two.hover_color = "red"
            self.btn_level_three.hover_color = "red"
        elif self.max_level == 2:
            self.btn_level_three.hover_color = "red"


        #and so on, must wait to understand how this work before we continue

    def start_game_state(self, level):
        self.sfx.button_sound()
        #if level is up to the required maxLevel then we can change the state else return locked
        if level <= self.max_level:
            self.engine.machine.next_state = GameState(self.engine, self.user, self.mode, level)

        #return a error message function to write ont he screen the error...

    def change_state_exit(self):
        self.sfx.button_sound()
        self.engine.machine.next_state = OuterLevelState(self.engine, self.user)

    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.level_select , (0, 0))
        self.btn_level_one.draw(surface, 245, 35)
        self.btn_level_two.draw(surface, 405, 238)
        self.btn_level_three.draw(surface, 255, 445)
        self.btn_quit.draw(surface, 5, 485)


        #add the buttons we need should be 3 for the diff levels
        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Returning to menu screen")
                self.change_state_exit()
        self.ui.handle_event(event)


