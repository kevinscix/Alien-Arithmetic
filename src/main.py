from Interface.state_machine import DisplayEngine
from Interface.login import LoginState
import pygame
import os
import sys
# Setup the environment by appending the current directory to the system path.
current_dir = os.path.dirname(__file__)
sys.path.append(current_dir)

def main():
    """
    The main function that initializes the pygame environment, sets up the game engine, and starts the game loop.

    This function creates an instance of the DisplayEngine, sets the initial state to LoginState, and runs the game loop
    until the game is exited. Pygame is initialized at the beginning and quit at the end to ensure proper resource management.
    """
    pygame.init()# Initialize all imported pygame modules
    # Create a DisplayEngine object with the specified title, frame rate, and window size
    engine = DisplayEngine('Alien Arithmetic', 60, 800, 600)
    # Start the game loop with the initial state set to LoginState
    engine.run(LoginState(engine))
pygame.quit()

main()


