
import os
import random

import pygame
from pygame import Color

from PygameUIKit import Group
from PygameUIKit import text_input, button, slider

#
class Demo:
    def __init__(self):
        self.done = False
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.easy_objects = Group()
        self.text_input = text_input.TextInput(placeholder="", fixed_width=200, border_radius=2, ui_group=self.easy_objects,
                                               font=pygame.font.Font('freesansbold.ttf', 32))

    def run(self):
        while not self.done:
            self.events()
            self.draw()

    def on_events_button(self, events):
        self.text_input.handle_events(events)
       
    def draw(self):
        self.text_input.draw(self.screen, 200, 200)

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    def_font = pygame.font.SysFont("Arial", 20)

    Demo().run()
    pygame.quit()