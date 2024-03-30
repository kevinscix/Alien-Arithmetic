import pygame
import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)  # Moves up to 'interface'
src_dir = os.path.dirname(parent_dir)  # Moves up to 'src'
sys.path.append(src_dir)

class music():

    def __init__(self):
        pygame.mixer.init()
        self.menu_music_path = os.path.join(parent_dir, "assets", "audio", "music", "menu.wav")
        self.game_music_path = os.path.join(parent_dir, "assets", "audio", "music", "Abstraction - Three Red Hearts - Out of Time.wav")
        pygame.mixer.music.set_volume(0.2)

    def menu_music(self):
        pygame.mixer.stop()
        # load the menu music and loop it
        pygame.mixer.music.load(self.menu_music_path)
        pygame.mixer.music.play(-1)


    def game_music(self):
        pygame.mixer.stop()

        # load the menu music and loop it
        pygame.mixer.music.load(self.game_music_path)
        pygame.mixer.music.play(-1)


class sfx():

    def __init__(self):
        pygame.mixer.init()
        self.button_sounds = os.path.join(parent_dir, "assets", "audio", "effects", "menu select.wav")
        self.explosion_sounds = os.path.join(parent_dir, "assets", "audio", "effects", "Retro Explosion Short 02.wav")
        self.shooting_sounds = os.path.join(parent_dir, "assets", "audio", "effects", "potential shooting sound 1.wav")
        self.sounds = {
            'bullet' : pygame.mixer.Sound(self.shooting_sounds),
            'explosion' : pygame.mixer.SoundType(self.explosion_sounds),
            'button' : pygame.mixer.SoundType(self.button_sounds)
        }

    def button_sound(self):
        self.sounds['button'].set_volume(0.2)
        self.sounds['button'].play()


    def explosion_sound(self):
        self.sounds['button'].set_volume(0.3)
        self.sounds['explosion'].play()


    def shoot_sound(self):
        self.sounds['bullet'].play()
