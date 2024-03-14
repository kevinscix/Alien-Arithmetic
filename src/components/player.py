#Kevin
from pydantic import BaseModel

class Player(BaseModel):
    # health and points of the player
    health : int
    points : int

    # initialize the player attributes with 100 health and 0 points
    def __init__(self):
        self.health = 100
        self.points = 0

    # decreases the health of the player
    def damage(self):
        self.health -= 0 #placeholder for damage amount

    # returns the health of the player
    def getHealth(self):
        return self.health

    # returns the points of the player
    def addPoints(self, addPoints : int):
        self.points += addPoints

    def setPoints(self, points : int):
       self.points = points
