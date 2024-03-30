from Interface.state_machine import State, DisplayEngine
from PygameUIKit import Group, button
import pygame
from typing import List
import os

#comments
# do we need any interactions from this state


class instructorState(State):
    def __init__(self, engine):
        super().__init__(engine)

        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        currentPath = os.path.dirname(__file__)  
        instructorImagePath = os.path.join(currentPath, "..", "assets", "visuals", "pages - backgrounds", "instructor leaderboard page.png")
        backButtonPath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "logOutButton.png")
        self.instructorImage = pygame.image.load(os.path.normpath(instructorImagePath))
        self.instructorImage = pygame.transform.scale(self.instructorImage, (830, 600))
        self.backButtonImage = pygame.image.load(os.path.normpath(backButtonPath))
        self.backButtonImage = pygame.transform.scale(self.backButtonImage, (150, 100))



       # Back button 
        #needs to set up the correct location for and settings 
        self.btn_back = button.ButtonPngIcon(
            self.backButtonImage, 
            self.change_state_menu, 
            ui_group=self.ui
        )
        # self.btn_left = button.ButtonPngIcon(
        #     self.leftButtonImage, 
        #     self.change_state_right, 
        #     ui_group=self.ui
        # )
        # self.btn_right = button.ButtonPngIcon(
        #     self.rightButtonImage, 
        #     self.change_state_right, 
        #     ui_group=self.ui
        # )
    
    def createBoard(self):
        from Interface.modules.state import ScoreboardState, SaveState
        self.scoreboard = ScoreboardState()
        scores : List[SaveState] = self.scoreboard.loadScore()
        sorted_scores = sorted(scores, key=lambda s: s.score, reverse=True)

        return sorted_scores

    def change_state_menu(self):
        from Interface.login import LoginState
        self.engine.machine.next_state = LoginState(self.engine)

    def change_state_left(self):
        pass
    def change_state_right(self):
        pass

    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.instructorImage, (-15, 0))

        leaderboard_data = self.createBoard()
        y = 228
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        #change for loop to have the number 5 and its start be variables passed 
        #to a function that will change its numbers either 
        #+5 or -5 based on left or right button
        for i, player in enumerate(leaderboard_data[:5], start=1):
            # Create text surfaces for the player's name, score, and logged-in status
            name_surface = self.font.render(f"{i}.{player.name}", True, (255, 255, 255))
            score_surface = self.font.render(str(player.score), True, (255, 255, 255))
            
            surface.blit(name_surface, (175, y))
            surface.blit(score_surface, (490, y))
            y += self.font.get_height() + 20


    

        self.btn_back.draw(surface, 0, 500)

        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Returning to menu screen")
                self.go_back_menu()
        self.ui.handle_event(event)
