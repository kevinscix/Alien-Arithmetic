import pygame
from PygameUIKit import Group, button

W = 1280
H = 720
class GameGUI:
    def __init__(self, window, start_callback, quit_callback):
        self.window = window
        self.start_callback = start_callback
        self.quit_callback = quit_callback
        self.ui = Group()
        
        self.btn_start = button.ButtonText("Start", self.start, rect_color=(85, 145, 92), fixed_width=200, border_radius=10, text_align="center", ui_group=self.ui)

        self.btn_quit = button.ButtonText("Quit", self.quit, rect_color=(181, 71, 71), fixed_width=180, border_radius=10, text_align="center", ui_group=self.ui)

    def handle_events(self, events):
        for event in events:
            self.ui.handle_event(event)

    def draw(self):
        self.window.fill((0, 0, 0))
        self.btn_start.draw(self.window, *self.btn_start.surface.get_rect(center=(W // 2, H // 2 - 50)).topleft)
        self.btn_quit.draw(self.window, *self.btn_quit.surface.get_rect(center=(W // 2, H // 2 + 50)).topleft)

    def start(self):
        self.start_callback()

    def quit(self):
        self.quit_callback()