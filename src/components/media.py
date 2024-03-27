import pygame

class music():

    def __init__(self):
        pygame.mixer.init()


    def menu_music(self):
        pygame.mixer.stop()

        # load the menu music and loop it
        pygame.mixer.music.load("../assets/audio/music/menu.wav")
        pygame.mixer.music.play(-1)


    def game_music():
        pygame.mixer.stop()

        # load the menu music and loop it
        pygame.mixer.music.load("../assets/audio/music/Abstraction - Three Red Hearts - Out of Time.wav")
        pygame.mixer.music.play(-1)


class sfx():

    def __init__(self):
        pygame.mixer.init()

    
    def button_sound(self):
        pygame.mixer.music.load("../assets/audio/effects/menu select.wav")
        pygame.mixer.music.play()

    
    def explosion_sound(self):
        pygame.mixer.music.load("../assets/audio/effects/Retro Explosion Short 02.wav")
        pygame.mixer.music.play()

    
    def shoot_sound(self):
        pygame.mixer.music.load("../assets/audio/effects/potential shooting sound 1.wav")
        pygame.mixer()