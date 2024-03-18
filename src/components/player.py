#Kevin
from pydantic import BaseModel
from typing import Optional

class Player(BaseModel):
    # health and points of the player
    health : Optional[int] = None
    points : Optional[int] = None
    speed : Optional[int] = None

    # initialize the player attributes with 100 health and 0 points
    def __init__(self):
        self.health = 3
        self.points = 0
        self.speed = 300

    # decreases the health of the player
    def damage(self) -> None:
        self.health -= 0 #placeholder for damage amount

    def damage(self):
        self.health -= 1

    # returns the health of the player
    def getHealth(self) -> int:
        return self.health

    # returns the points of the player
    def addPoints(self, addPoints : int) -> None:
        self.points += addPoints

    def setPoints(self, points : int) -> None:
       self.points = points

    def getSpeed(self) -> int:
        return self.speed

    #for later implementation to save player specific information
    def save(self) -> None:
        pass

        # missile methods

    # ready is the status of the missile (cooldown system)
    
    # the user's input will trigger this method
    # it will check the ready variable
    # if ready, it will fire a missile
    # missile will despawn once it is 100px off the screen
    def trajectory(self):
        if self.ready == True:
            self.ready = False
            Projectile.trajectory(self)
        else:
            # if missile isn't ready, nothing happens :)
            pass
