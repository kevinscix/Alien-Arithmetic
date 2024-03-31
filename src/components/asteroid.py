import os
import random
import pygame
import unittest

pygame.font.init()

class Asteroid():

    # Constructor method
    def __init__(self, mode, level) -> None:
        """
        Initializes Asteroid object.
        Args:
            mode (str): Game mode ('plus', 'minus', 'multiply').
            level (int): Game level.
        """
        self.max_asteroid : int = 10
        self.min_asteroid : int = 1
        self.max_result_asteroid : int = self.max_asteroid * self.max_asteroid

        #offset is used to center the asteroid to center
        if level == 1:
            self.number_of_asteroids = 3
            self.offset = 70
        elif level == 2:
            self.number_of_asteroids = 4
            self.offset = 55
        elif level == 3:
            self.number_of_asteroids = 5
            self.offset = 35
        else:
            self.number_of_asteroids = 5


        self.speed : float = 1    # how many pixels the asteroid will move by each loop, not final
        self.first_op : int
        self.second_op : int
        self.second_answer : int
        self.size : float = 1
        self.mode = mode
        self.level = level

        # Initialize array to store asteroid values
        self.asteroid_arr = []
        self.question_surface = ''

        self.font_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "visuals", "fonts", "PressStart2P-Regular.ttf")

        self.font = pygame.font.Font(self.font_path, 24)
        self.incrementsize = 800 / self.number_of_asteroids

        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        asteroidImagePath = os.path.join(currentPath, "..", "assets", "visuals", "level builder", "asteroid.png")
        self.asteroidImagePath = pygame.image.load(os.path.normpath(asteroidImagePath))


    def create_question(self):
        """
        Generates a random arithmetic question.
        """
        self.first_op = random.randint(self.min_asteroid, self.max_asteroid)
        self.second_op = random.randint(self.min_asteroid, self.max_asteroid)

        # Calculate and set the correct answer to the question
        print("creating question for", self.mode)
        if self.mode == "plus":
            # addition
            self.second_answer = self.first_op + self.second_op
        elif self.mode == "minus":
            # subtraction
            self.second_answer = self.first_op - self.second_op
        elif self.mode == "multiply":
            # multiplication
            self.second_answer = self.first_op * self.second_op
        else:
            self.second_answer = 999

    def create_asteroids(self, x, y, value, isCorrect):
        """
        Creates an asteroid.
        Args:
            x (int): X-coordinate of the asteroid.
            y (int): Y-coordinate of the asteroid.
            value (int): Value displayed on the asteroid.
            isCorrect (bool): Indicates whether the asteroid represents the correct answer.
        Returns:
            dict: Dictionary representing the asteroid.
        """
        # scale it to smaller size and make it quadratic
        surf = pygame.transform.scale(self.asteroidImagePath, (70, 70))
        number_surface = self.font.render((str(value)), True, (0, 0, 0))

        return {
            'surface': surf,
            'number_surface': number_surface,
            'position': [x + self.offset, y],
            'value' : value,
            'speed': self.speed,
            'angle': 0,
            'correct' : isCorrect,
            'destroyed' : False
        }

    # changes Y axis position by speed amount
    def move_asteroids(self):
        """
        Moves all asteroids downward by the current speed.
        """
        for asteroid in self.asteroid_arr:
            asteroid['position'][1] += self.speed

    def generateAsteroids(self):
        """
        Generates asteroids with correct and incorrect answers.
        """
        self.create_question()
        self.create_question_surface()

        picked = random.randint(0 , self.number_of_asteroids - 1)
        print(picked)
        print(self.second_answer)
        values = []

        #must append here else it will allow the generated value before be the correct answers
        values.append(self.second_answer)
        for i in range(0, self.number_of_asteroids):
            if picked == i:
                self.asteroid_arr.append(self.create_asteroids(self.incrementsize * i, 0, self.second_answer, True))
            else:
                x = 0
                if self.mode == "plus":
                    # 1 - max + max is the upper limit
                    x = random.randint(self.min_asteroid, self.max_asteroid + self.max_asteroid)
                    while x in values:
                        print(x, " |+| ", values)
                        x = random.randint(self.min_asteroid, self.max_asteroid + self.max_asteroid)
                    # addition
                elif self.mode == "minus":
                    # 1 - max and max - 1, range for minus
                    x = random.randint(-self.max_asteroid, self.max_asteroid)
                    while x in values:
                        x = random.randint(-self.max_asteroid, self.max_asteroid)

                elif self.mode == "multiply":
                    # 1 - max * max.
                    x = random.randint(self.min_asteroid, self.max_result_asteroid)
                    while x in values:
                        x = random.randint(self.min_asteroid, self.max_result_asteroid)

                # Ensure the incorrect answer is not a duplicate of the correct answer
                
                values.append(x)
                print(x, " -> " ,values)
                self.asteroid_arr.append(self.create_asteroids(self.incrementsize * i, 0, x, False))

    def showEquation(self) -> str:
        """
        Returns:
            str: Equation string.
        """
        eq = "none"
        if self.mode == "plus":
            eq = "%d+%d=" % (self.first_op, self.second_op)
        elif self.mode == "minus":
            eq = "%d-%d=" % (self.first_op, self.second_op)
        elif self.mode == "multiply":
            eq = "%dx%d=" % (self.first_op, self.second_op)

        return eq

    def create_question_surface(self):
        """
        Creates the surface for displaying the equation.
        """
        self.question_surface = self.font.render(self.showEquation(), True, (0, 0, 0))

    def size_speed_scale(self, value) -> None:
        """
        Scales the size and speed of the asteroid.
        Args:
            value (float): Value used for scaling.
        """
        size_scalar = value * 0.02 + 1
        speed_scalar = 1 - (size_scalar / 10)
        self.size = self.size * size_scalar
        self.speed = self.speed * speed_scalar



if __name__ == "__main__":

    # manual testing
    ass = Asteroid("multiply", 1)
    ass.create_question()
    ass.generateAsteroids()


    for i in range(2):
         print(ass.asteroid_arr[i])

    for i in range(2):
         print(ass.asteroid_arr[i]["position"])
    
    print("mode:", ass.mode)
    print("equation:", ass.showEquation())


    # automated testing
    class test_asteroid(unittest.TestCase):

        def setUp(self):
            self.asteroid = Asteroid(1, 1)
            self.asteroid.create_question()
            self.asteroid.generateAsteroids()

        def test_move(self):
            for i in range(5):
                self.asteroid.move_asteroids()
            self.assertEqual(self.asteroid.asteroid_arr[0]["position"][1], 5, "position is wrong")


    unittest.main()
