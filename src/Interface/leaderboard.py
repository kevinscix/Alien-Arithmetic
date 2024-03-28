from Interface.state_machine import State, DisplayEngine
from PygameUIKit import Group, button
import pygame
from typing import List
import os

#comments
# do we need any interactions from this state


class LeaderboardState(State):
    def __init__(self, engine, user):
        super().__init__(engine)

        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        self.user = user
        currentPath = os.path.dirname(__file__)  
        scoreboardImagePath = os.path.join(currentPath, "..", "components", "Images", "scoreboardScreen.png")
        backButtonPath = os.path.join(currentPath, "..", "components", "Images", "logOutButton.png")
        levelSelectButtonPath = os.path.join(currentPath, "..", "components", "Images", "levelSelectButton.png")
        self.scoreboardImage = pygame.image.load(os.path.normpath(scoreboardImagePath))
        self.scoreboardImage = pygame.transform.scale(self.scoreboardImage, (800, 600))
        self.backButtonImage = pygame.image.load(os.path.normpath(backButtonPath))
        self.backButtonImage = pygame.transform.scale(self.backButtonImage, (150, 100))
        self.levelSelectImage = pygame.image.load(os.path.normpath(levelSelectButtonPath))
        self.levelSelectImage = pygame.transform.scale(self.levelSelectImage, (245, 100))


        # pull loaded data from scoreboard class .load function
        # return a array of player class, these are player models that are validated
        # can pull individual player data from this 
        # create a subfunction separate the data by rows of player name, score and have they logged on
        # then draw this in the def 0n_draw function

       # Back button 
        #needs to set up the correct location for and settings 
        self.btn_back = button.ButtonPngIcon(
            self.backButtonImage, 
            self.change_state_menu, 
            ui_group=self.ui
        )
        self.btn_level_select = button.ButtonPngIcon(
            self.levelSelectImage, 
            self.change_state_select, 
            ui_group=self.ui
        )
    
    def createBoard(self):
        from Interface.modules.state import ScoreboardState, SaveState
        self.scoreboard = ScoreboardState()
        scores : List[SaveState] = self.scoreboard.loadScore()
        sorted_scores = sorted(scores, key=lambda s: s.score, reverse=True)

        return sorted_scores

    def change_state_menu(self):
        from Interface.menu import MenuState
        self.engine.machine.next_state = MenuState(self.engine, self.user)
    
    def change_state_select(self):
        from Interface.level import OutterLevelState
        self.engine.machine.next_state = OutterLevelState(self.engine)


    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.scoreboardImage, (0, 0))

        leaderboard_data = self.createBoard()
        y = 205
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        for i, player in enumerate(leaderboard_data[:5], start=1):
            # Create text surfaces for the player's name, score, and logged-in status
            name_surface = self.font.render(f"{i}.{player.name}", True, (255, 255, 255))
            score_surface = self.font.render(str(player.score), True, (255, 255, 255))
            logged_in_surface = self.font.render('Yes' if player.loggedIn else 'No', True, (255, 255, 255))
            
            surface.blit(name_surface, (110, y))
            surface.blit(score_surface, (320, y))
            surface.blit(logged_in_surface, (550, y))
            y += self.font.get_height() + 25

    

        self.btn_level_select.draw(surface, 275, 500)
        self.btn_back.draw(surface, 0, 500)

        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Returning to menu screen")
                self.go_back_menu()
        self.ui.handle_event(event)
