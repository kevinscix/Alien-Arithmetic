from Interface.state_machine import DisplayEngine
import pygame
from Interface.login import LoginState

import os
import sys

current_dir = os.path.dirname(__file__)
sys.path.append(current_dir)

def main():
    pygame.init()
    engine = DisplayEngine('Alien Arithmetic', 60, 800, 600)
    engine.run(LoginState(engine))
pygame.quit()

print(current_dir)
main()