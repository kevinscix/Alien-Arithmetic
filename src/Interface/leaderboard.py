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
        scoreboardImagePath = os.path.join(currentPath, "..", "assets", "visuals", "pages - backgrounds", "student leaderboard page.png")
        backButtonPath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "exitButton.png")
        levelSelectButtonPath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "levelSelectButton.png")
        self.font_path = os.path.join(currentPath, "..","assets", "visuals", "fonts", "PressStart2P-Regular.ttf")
        self.scoreboardImage = pygame.image.load(os.path.normpath(scoreboardImagePath))
        self.scoreboardImage = pygame.transform.scale(self.scoreboardImage, (830, 600))
        self.backButtonImage = pygame.image.load(os.path.normpath(backButtonPath))
        self.backButtonImage = pygame.transform.scale(self.backButtonImage, (150, 100))



       # Back button 
        #needs to set up the correct location for and settings 
        self.btn_back = button.ButtonPngIcon(
            self.backButtonImage, 
            self.change_state_menu, 
            ui_group=self.ui
        )


        self.leaderboard_data = []
        self.createBoard()

    def createBoard(self):
        from Interface.modules.state import ScoreboardState, SaveState
        self.scoreboard = ScoreboardState()
        scores : List[SaveState] = self.scoreboard.loadScore()
        self.leaderboard_data = []
        self.leaderboard_data = scores

    def change_state_menu(self):
        from Interface.menu import MenuState
        self.engine.machine.next_state = MenuState(self.engine, self.user)



    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.scoreboardImage, (-15, 0))

        y = 230
        self.font = pygame.font.Font(self.font_path, 25)

        for i, player in enumerate(self.leaderboard_data[:5], start=1):
            # Create text surfaces for the player's name, score, and logged-in status
            name_surface = self.font.render(f"{i}.{player.name}", True, (255, 255, 255))
            score_surface = self.font.render(str(player.score), True, (255, 255, 255))
            
            surface.blit(name_surface, (175, y))
            surface.blit(score_surface, (490, y))
            y += self.font.get_height() + 30

        mainScore_surface = self.font.render(str(self.user.name) + ' score: ' + str(self.user.score), True, "red")
        surface.blit(mainScore_surface, (160, 100))

    

        self.btn_back.draw(surface, 0, 500)

        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Returning to menu screen")
                self.change_state_menu()
        self.ui.handle_event(event)
