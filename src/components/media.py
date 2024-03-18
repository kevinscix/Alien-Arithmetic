import pygame
class Media:
    def __init__(self, imagePath):
        self.backgroundImage = pygame.image.load(imagePath)

    def drawBackground(self, screen):
        screen.blit(self.backgroundImage, (0, 0))