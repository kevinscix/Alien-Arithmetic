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
        self.currentPage = 0  

        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter    
        parentPath = os.path.dirname(os.path.dirname(__file__))
        instructorImagePath = os.path.join(parentPath, "assets", "visuals", "pages - backgrounds", "instructor leaderboard page.png")
        backButtonPath = os.path.join(parentPath, "assets", "visuals", "buttons", "text buttons", "logOutButton.png")
        leftButtonPath = os.path.join(parentPath,"assets", "visuals", "buttons", "text buttons", "left button.png")
        rightButtonPath = os.path.join(parentPath,"assets", "visuals", "buttons", "text buttons", "right button.png")
        self.font_path = os.path.join(parentPath, "assets", "visuals", "fonts", "PressStart2P-Regular.ttf")

        self.instructorImage = pygame.image.load(os.path.normpath(instructorImagePath))
        self.instructorImage = pygame.transform.scale(self.instructorImage, (840, 600))
        self.backButtonImage = pygame.image.load(os.path.normpath(backButtonPath))
        self.backButtonImage = pygame.transform.scale(self.backButtonImage, (150, 100))
        self.leftButtonImage = pygame.image.load(os.path.normpath(leftButtonPath))
        self.leftButtonImage = pygame.transform.scale(self.leftButtonImage, (75, 100))
        self.rightButtonImage = pygame.image.load(os.path.normpath(rightButtonPath))
        self.rightButtonImage = pygame.transform.scale(self.rightButtonImage, (75, 100))





       # Back button 
        #needs to set up the correct location for and settings 
        self.btn_back = button.ButtonPngIcon(
            self.backButtonImage, 
            self.change_state_menu, 
            ui_group=self.ui
        )
        self.btn_left = button.ButtonPngIcon(
            self.leftButtonImage, 
            self.change_state_left, 
            ui_group=self.ui
        )
        self.btn_right = button.ButtonPngIcon(
            self.rightButtonImage, 
            self.change_state_right, 
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
        from Interface.login import LoginState
        self.engine.machine.next_state = LoginState(self.engine)

    def change_state_left(self):
        if self.currentPage > 0: 
            self.currentPage -= 1
    def change_state_right(self):
        leaderboard_data = self.createBoard()
        total_pages = (len(self.leaderboard_data) + 4) // 5  
        if self.currentPage + 1 < total_pages:  
            self.currentPage += 1

    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.instructorImage, (-25, 0))

        leaderboard_data = self.createBoard()
        y = 200
        self.font = pygame.font.Font(self.font_path, 18)

        #change for loop to have the number 5 and its start be variables passed 
        #to a function that will change its numbers either 
        #+5 or -5 based on left or right button
        try:
            start_index = self.currentPage * 5
            end_index = start_index + 5
            displayed_scores = self.leaderboard_data[start_index:end_index]
            
            for i, player in enumerate(displayed_scores, start=start_index + 1):
                name_surface = self.font.render(f"{player.name}", True, (255, 255, 255))
                level_surface = self.font.render(f"{player.level}", True, (255, 255, 255))
                completed_surface = self.font.render(f"{player.questionsCompleted}", True, (255, 255, 255))
                correct_surface = self.font.render(f"{player.correctAmt}", True, (255, 255, 255))
                score_surface = self.font.render(str(player.score), True, (255, 255, 255))
                surface.blit(name_surface, (85, y))
                surface.blit(level_surface, (220, y))
                surface.blit(completed_surface, (500, y))
                surface.blit(correct_surface, (370, y))
                surface.blit(score_surface, (590, y))
                y += self.font.get_height() + 40
        except:
            pass


    
        self.btn_left.draw(surface, -3, 250)
        self.btn_right.draw(surface, 728, 250)

        self.btn_back.draw(surface, 0, 500)

        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.change_state_menu:
                print("Returning to menu screen")
                self.change_state_menu()
        self.ui.handle_event(event)
