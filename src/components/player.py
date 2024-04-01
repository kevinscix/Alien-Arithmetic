import unittest
from typing import Optional

class Player():
    """
    Represents the player in Alien Arithmetic
    """

    # health and points of the player
    health : Optional[int] = None
    points : Optional[int] = None
    speed : Optional[int] = None


    def __init__(self):
        """
        Initializes player with default attributes.
        """
        self.totalHealth = 3
        self.health = 3
        self.points = 0
        self.speed = 300
        self.ready = True

    def healthScale(self) -> int:
        """
        Calculates the health scale of the player.
        Returns:
            float: The health scale, a value between 0 and 1.
        """
        return self.health / self.totalHealth

    def damage(self):
        """
        Decreases the player's health by one.
        """
        self.health -= 1

    def resetHealth(self):
        """
        Resets the player's health to its maximum value.
        """
        self.health = 3

    def getHealth(self) -> int:
        """
        Returns:
            int: The current health of the player.
        """
        return self.health

    def addPoints(self) -> None:
        """
        Adds points to the player's score.
        Args:
            addPoints (int): The number of points to add.
        """
        self.points += 10

    def removePoints(self):
        """
        Remove points to the player's score.
        Args:
            removePoints (int): The number of points to add.
        """
        self.points -= 10
        if self.points < 0:
            self.points = 0


    def setPoints(self, points : int) -> None:
       """
        Sets the player's score to a specific value.
        Args:
            points (int): The new score for the player.
        """
       self.points = points

    def getSpeed(self) -> int:
        """
        Returns:
            int: The speed of the player.
        """
        return self.speed

#unit testing

class TestPlayer(unittest.TestCase):
    """
    Test cases for the Player class.
    """

    def setUp(self):
        """
        Sets up the test fixture.
        """
        self.player = Player()

    def test_initial_attributes(self):
        """
        Test the initial attributes of a new player.
        """
        self.assertEqual(self.player.totalHealth, 3, "Initial total health should be 3")
        self.assertEqual(self.player.health, 3, "Initial health should be 3")
        self.assertEqual(self.player.points, 0, "Initial points should be 0")
        self.assertEqual(self.player.speed, 300, "Initial speed should be 300")
        self.assertTrue(self.player.ready, "Player should be initially ready")

    def test_health_scale(self):
        """
        Test the health scale method.
        """
        self.player.health = 1
        self.assertEqual(self.player.healthScale(), 1 / 3, "Health scale calculation is incorrect")

    def test_modify_attributes(self):
        """
        Test modifying player's health, points, and speed.
        """
        self.player.health = 2
        self.player.points = 100
        self.player.speed = 200
        self.assertEqual(self.player.health, 2, "Health should be updated to 2")
        self.assertEqual(self.player.points, 100, "Points should be updated to 100")
        self.assertEqual(self.player.speed, 200, "Speed should be updated to 200")

if __name__ == "__main__":
    unittest.main()