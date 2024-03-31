import unittest
from typing import Optional

class Player():
    # health and points of the player
    health : Optional[int] = None
    points : Optional[int] = None
    speed : Optional[int] = None

    # initialize the player attributes with 100 health and 0 points
    def __init__(self):
        self.totalHealth = 3
        self.health = 3
        self.points = 0
        self.speed = 300
        self.ready = True

    def healthScale(self) -> int:
        return self.health / self.totalHealth
    #decrease by onne, player should have a set
    def damage(self):
        self.health -= 1

    def resetHealth(self):
        self.health = 3
    # returns the health of the player
    def getHealth(self) -> int:
        return self.health

    # returns the points of the player
    def addPoints(self) -> None:
        self.points += 10

    def removePoints(self):
        self.points -= 10
    def setPoints(self, points : int) -> None:
       self.points = points

    def getSpeed(self) -> int:
        return self.speed

    #for later implementation to save player specific information
    def save(self) -> None:
        pass

#unit testing

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_initial_attributes(self):
        # Test that a new player has the correct initial attributes
        self.assertEqual(self.player.totalHealth, 3, "Initial total health should be 3")
        self.assertEqual(self.player.health, 3, "Initial health should be 3")
        self.assertEqual(self.player.points, 0, "Initial points should be 0")
        self.assertEqual(self.player.speed, 300, "Initial speed should be 300")
        self.assertTrue(self.player.ready, "Player should be initially ready")

    def test_health_scale(self):
        # Test the health scale method
        self.player.health = 1
        self.assertEqual(self.player.healthScale(), 1 / 3, "Health scale calculation is incorrect")

    def test_modify_attributes(self):
        # Test modifying player's health, points, and speed
        self.player.health = 2
        self.player.points = 100
        self.player.speed = 200
        self.assertEqual(self.player.health, 2, "Health should be updated to 2")
        self.assertEqual(self.player.points, 100, "Points should be updated to 100")
        self.assertEqual(self.player.speed, 200, "Speed should be updated to 200")

if __name__ == "__main__":
    unittest.main()