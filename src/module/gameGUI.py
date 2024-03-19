import pygame
from PygameUIKit import Group, button

class GameGUI:
    def __init__(self, window, start_callback, quit_callback, load_callback, tutorial_callback, highscores_callback, studentLogin_callback, teacherLogin_callback):
        self.window = window
        self.start_callback = start_callback
        self.load_callback = load_callback
        self.tutorial_callback = tutorial_callback
        self.highscores_callback = highscores_callback
        self.quit_callback = quit_callback
        self.studentLogin_callback = studentLogin_callback
        self.teacherLogin_callback = teacherLogin_callback
        self.ui = Group()
        
       # Student Login button
        self.btn_studentLogin = button.ButtonText(
            "Student Login", 
            studentLogin_callback, 
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
        # Teacher Login button
        self.btn_teacherLogin = button.ButtonText(
            "Teacher login", 
            teacherLogin_callback, 
            fixed_width=200,  
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )

       # Start button
        self.btn_start = button.ButtonText(
            "Start", 
            start_callback, 
            rect_color=(85, 145, 92),  # Green color
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
        # Load Game button
        self.btn_load = button.ButtonText(
            "Load Game", 
            load_callback, 
            rect_color=(85, 92, 145),  # Blue color
            fixed_width=220,  # Slightly wider
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
        # Tutorial button
        self.btn_tutorial = button.ButtonText(
            "Tutorial", 
            tutorial_callback, 
            # rect_color=(145, 92, 85),  # Orange color
            fixed_width=200, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
        # Highscores button
        self.btn_highscores = button.ButtonText(
            "Highscores", 
            highscores_callback, 
            rect_color=(92, 145, 85),  # Different shade of green
            fixed_width=220,  # Slightly wider
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )
        
        # Quit button
        self.btn_quit = button.ButtonText(
            "Quit", 
            quit_callback, 
            rect_color=(181, 71, 71),  # Red color
            fixed_width=180, 
            border_radius=10, 
            text_align="center", 
            ui_group=self.ui
        )


    def handle_events(self, events):
        for event in events:
            self.ui.handle_event(event)

    def draw(self):
        button_spacing = 60
        start_y = self.window.get_height() // 2 - (button_spacing * 2)  # Start drawing from this y-coordinate

        # Student login button
        self.btn_studentLogin.draw(self.window, *self.btn_studentLogin.surface.get_rect(center = (self.window.get_width() // 2 - 150, self.window.get_height() - 150)).topleft)

        # Teacher Login button
        self.btn_teacherLogin.draw(self.window, *self.btn_teacherLogin.surface.get_rect(center = (self.window.get_width() // 2 + 150, self.window.get_height() - 150)).topleft)


        # # Start button
        # self.btn_start.draw(self.window, *self.btn_start.surface.get_rect(center=(self.window.get_width() // 2, start_y)).topleft)

        # # Load Game button
        # self.btn_load.draw(self.window, *self.btn_load.surface.get_rect(center=(self.window.get_width() // 2, start_y + button_spacing)).topleft)

        # # Tutorial button
        # self.btn_tutorial.draw(self.window, *self.btn_tutorial.surface.get_rect(center=(self.window.get_width() // 2, start_y + button_spacing * 2)).topleft)

        # # Highscores button
        # self.btn_highscores.draw(self.window, *self.btn_highscores.surface.get_rect(center=(self.window.get_width() // 2, start_y + button_spacing * 3)).topleft)

        # # Quit button
        # self.btn_quit.draw(self.window, *self.btn_quit.surface.get_rect(center=(self.window.get_width() // 2, start_y + button_spacing * 4)).topleft)
        
    def start(self):
        self.start_callback()
        
    def load(self):
        self.load_callback()

    def tutorial(self):
        self.tutorial_callback()

    def highscores(self):
        self.highscores_callback()

    def quit(self):
        self.quit_callback()

    def studentLogin(self):
        self.studentLogin_callback()

    def teacherLogin(self):
        self.teacherLogin_callback()