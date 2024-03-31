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
        parent_path = os.path.dirname(os.path.dirname(__file__))
        
        instructor_image_path = os.path.join(parent_path, "assets", "visuals", "pages - backgrounds", "instructor leaderboard page.png")
        back_button_path = os.path.join(parent_path, "assets", "visuals", "buttons", "text buttons", "logOutButton.png")
        left_button_path = os.path.join(parent_path,"assets", "visuals", "buttons", "text buttons", "left button.png")
        right_button_path = os.path.join(parent_path,"assets", "visuals", "buttons", "text buttons", "right button.png")
        self.font_path = os.path.join(parent_path, "assets", "visuals", "fonts", "PressStart2P-Regular.ttf")

        self.instructor_image = pygame.image.load(os.path.normpath(instructor_image_path))
        self.instructor_image = pygame.transform.scale(self.instructor_image, (840, 600))
        self.back_button_image = pygame.image.load(os.path.normpath(back_button_path))
        self.back_button_image = pygame.transform.scale(self.back_button_image, (150, 100))
        self.left_button_image = pygame.image.load(os.path.normpath(left_button_path))
        self.left_button_image = pygame.transform.scale(self.left_button_image, (75, 100))
        self.right_button_image = pygame.image.load(os.path.normpath(right_button_path))
        self.right_button_image = pygame.transform.scale(self.right_button_image, (75, 100))




       # Back button 
        #needs to set up the correct location for and settings 
        self.btn_back = button.ButtonPngIcon(
            self.back_button_image, 
            self.change_state_menu, 
            ui_group=self.ui
        )
        self.btn_left = button.ButtonPngIcon(
            self.left_button_image, 
            self.change_state_left, 
            ui_group=self.ui
        )
        self.btn_right = button.ButtonPngIcon(
            self.right_button_image, 
            self.change_state_right, 
            ui_group=self.ui
        )
        from components.media import sfx
        self.sfx = sfx()
        self.leaderboard_data = []
        self.createBoard()

    def createBoard(self):
        from Interface.modules.state import ScoreboardState, SaveState
        self.scoreboard = ScoreboardState()
        scores : List[SaveState] = self.scoreboard.loadScore()
        self.leaderboard_data = []
        self.leaderboard_data = scores
        self.start_index = self.currentPage * 5
        self.end_index = self.start_index + 5
        self.displayed_scores = self.leaderboard_data[self.start_index:self.end_index]

    def change_state_menu(self):
        self.sfx.button_sound()
        from Interface.login import LoginState
        self.engine.machine.next_state = LoginState(self.engine)

    def change_state_left(self):
        self.sfx.button_sound()
        if self.currentPage > 0: 
            self.currentPage -= 1

    def change_state_right(self):
        self.sfx.button_sound()
        leaderboard_data = self.createBoard()
        total_pages = (len(self.leaderboard_data) + 4) // 5  
        if self.currentPage + 1 < total_pages:  
            self.currentPage += 1

    def on_draw(self, surface):
        #draws the titleImage on surface
        surface.blit(self.instructor_image, (-25, 0))

        leaderboard_data = self.createBoard()
        y = 200
        self.font = pygame.font.Font(self.font_path, 18)

        #change for loop to have the number 5 and its start be variables passed 
        #to a function that will change its numbers either 
        #+5 or -5 based on left or right button
        try:
           
            
            for i, player in enumerate(self.displayed_scores, start=self.start_index + 1):
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
            if event.key == pygame.K_ESCAPE:
                print("Returning to menu screen")
                self.change_state_menu()
            if event.key == pygame.K_RIGHT:
                self.change_state_right()
            if event.key == pygame.K_LEFT:
                self.change_state_left()
        self.ui.handle_event(event)
