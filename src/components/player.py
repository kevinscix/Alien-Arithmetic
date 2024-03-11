#Kevin
import pygame

class Player:
    health : int
    points : int

    def __init__(self):
        self.health = 100
        self.points = 0

    def damage(self):
        self.health -= 0 #placeholder for damage amount

    def getHealth(self):
        return self.health

    def addPoints(self, addPoints : int):
        self.points += addPoints

    def setPoints(self, points : int):
       self.points = points

    def move(self):
        pass