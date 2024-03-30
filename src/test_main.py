from Interface.state_machine import DisplayEngine
import pygame
from Interface.login import LoginState

def main():
    pygame.init()
    engine = DisplayEngine('Alien Arithmetic', 60, 800, 600)
    engine.run(LoginState(engine))
    pygame.quit()

main()  