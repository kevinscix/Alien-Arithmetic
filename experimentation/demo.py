import os
import random

import pygame
from pygame import Color

from PygameUIKit import Group
from PygameUIKit import text_input, button, slider

#
#
# This is a file to showcase every EasyObject
#
#

RED = (255, 0, 0)
BTN_GREEN = (0, 169, 0)
BTN_BLUE = (83, 131, 232)

cwd = os.path.dirname(__file__)



class Demo:
    def __init__(self):
        self.done = False
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()

        self.easy_objects = Group()
        self.text_input = text_input.TextInput(placeholder="This is a placeholder text", fixed_width=200, border_radius=2, ui_group=self.easy_objects,
                                               font=def_font)


        self.slider = slider.Slider(0, 100, 1, show_value=True, ui_group=self.easy_objects, font=def_font)
        self.slider.connect(self.change_values)

        
       
        self.dancing = False

    def run(self):
        while not self.done:
            dt = self.clock.tick(60) / 1000
            self.events()
            self.update(dt)
            self.draw(self.screen)

    def events(self):
        events = pygame.event.get()
        for event in events:
            self.easy_objects.handle_event(event)
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"position: {event.pos}")

        self.text_input.handle_events(events)

    def update(self, dt):
        self.easy_objects.update(dt)
        if self.dancing:
            self.change_values()

    def draw(self, win):
        W, H = self.screen.get_size()
        win.fill(Color(224, 224, 224))
        self.text_input.draw(win, W // 2 - self.text_input.rect.w // 2, H - 200)
        self.slider.draw(win, 100, 400, 300, 5)
        pygame.display.flip()

    def change_values(self):
        i = random.randint(0, len(self.chart.values) - 1)
        new_value = random.randint(0, 100)
        self.chart.change_value(i, new_value)

    def toggle_dance(self):
        self.dancing = not self.dancing


def do_nothing():
    pass


if __name__ == '__main__':
    pygame.init()
    def_font = pygame.font.SysFont("Arial", 20)

    Demo().run()
    pygame.quit()