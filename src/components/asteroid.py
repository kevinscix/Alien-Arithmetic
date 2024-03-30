#Jackson
import os
import random
import pygame
import unittest

pygame.font.init()

class Asteroid():
    # Class-level attributes

    # Constructor method
    def __init__(self, mode, level) -> None:
        self.maxAsteroid : int = 10
        self.minAsteroid : int = 1
        self.maxResultAsteroid : int = self.maxAsteroid * self.maxAsteroid

        if level == 1:
            self.numberOfAsteroids = 3
        elif level == 2:
            self.numberOfAsteroids = 4
        elif level == 3:
            self.numberOfAsteroids = 5
        else:
            self.numberOfAsteroids = 5
        self.speed : float = 1    # how many pixels the asteroid will move by each loop, not final
        self.firstOp : int
        self.secondOp : int
        self.correctAnswer : int
        self.size : float = 1     # placeholder value, this will be the default size before scaling
        self.mode = mode
        self.level = level
        # Calculate and set the correct answer to the question
        self.qAnswer = 0
        # set x position from input
        # input will be an int from 1 to 5, the saved value will be multiplied by a constant to get actual position

        # Initialize array to store asteroid values
        self.asteroidArr = []
        self.question_surface = ''


        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.incrementsize = 800 / self.numberOfAsteroids

        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        asteroidImagePath = os.path.join(currentPath, "..", "assets", "visuals", "level builder", "asteroid.png")
        self.asteroidImagePath = pygame.image.load(os.path.normpath(asteroidImagePath))


    def create_question(self):
         # generate answer based on mode

        self.firstOp = random.randint(self.minAsteroid, self.maxAsteroid)
        self.secondOp = random.randint(self.minAsteroid, self.maxAsteroid)

        # Calculate and set the correct answer to the question
        self.qAnswer = self.firstOp + self.secondOp
        print("creating question for", self.mode)
        if self.mode == "plus":
            # addition
            self.correctAnswer = self.firstOp + self.secondOp
        elif self.mode == "minus":
            # subtraction
            self.correctAnswer = self.firstOp - self.secondOp
        elif self.mode == "multiply":
            # multiplication
            self.correctAnswer = self.firstOp * self.secondOp
        else:
            # sometimes this value is reached?
            self.correctAnswer = 999

    def create_asteroids(self, x, y, value, isCorrect):
        # scale it to smaller size and make it quadratic
        surf = pygame.transform.scale(self.asteroidImagePath, (70, 70))
        number_surface = self.font.render((str(value)), True, (0, 0, 0))

        return {
            'surface': surf,
            'number_surface': number_surface,
            'position': [x, y],
            'value' : value,
            'speed': self.speed,
            'angle': 0,
            'correct' : isCorrect,
            'destroyed' : False
        }

    # .generate will create a list of asteriod dictionaries
    # from create_asteriods
    # randomize attributes
    # when asteriods are generated, append to array

    # changes Y axis position by speed amount
    def move_asteroids(self):
        for asteroid in self.asteroidArr:
            asteroid['position'][1] += self.speed

    def collide_barrer(self):
        pass

    # Method to generate asteroids with correct and incorrect answers
    def generateAsteroids(self):

        #generate the first correct answer
        #[answer]
        #generate the rest of the incorrect answers
        # for loop -1 the number of asteroids
        # rnd int if not answer and not in asteroid
        # store value in the array
        # for loop that creates an incorrect answer for each asteroid

        self.create_question()
        self.create_question_surface()

        picked = random.randint(0 , self.numberOfAsteroids - 1)
        print(picked)
        print(self.correctAnswer)
        for i in range(0, self.numberOfAsteroids):
            if picked == i:
                self.asteroidArr.append(self.create_asteroids(self.incrementsize * i, 0, self.correctAnswer, True))
            else:
                if self.mode == "plus":
                    # 1 - max + max is the upper limit
                    x = random.randint(self.minAsteroid, self.maxAsteroid + self.maxAsteroid)
                    # addition
                elif self.mode == "minus":
                    # 1 - max and max - 1, range for minus
                    x = random.randint(-self.maxAsteroid, self.maxAsteroid)

                elif self.mode == "multiply":
                    # 1 - max * max.
                    x = random.randint(self.minAsteroid, self.maxResultAsteroid)

                # Ensure the incorrect answer is not a duplicate of the correct answer
                while x in self.asteroidArr:
                    x = random.randint(self.minAsteroid, self.maxResultAsteroid)
                self.asteroidArr.append(self.create_asteroids(self.incrementsize * i, 0, x, False))

    def showEquation(self) -> str:
        eq = ""
        if self.mode == "plus":
            eq = "%d + %d" % (self.firstOp, self.secondOp)
        elif self.mode == "minus":
            eq = "%d - %d" % (self.firstOp, self.secondOp)
        elif self.mode == "multiply":
            eq = "%d x %d" % (self.firstOp, self.secondOp)

        return eq

    def create_question_surface(self):
        self.question_surface = self.font.render(self.showEquation(), True, (0, 0, 0))

    def size_speed_scale(self, value) -> None:
        size_scalar = value * 0.02 + 1
        speed_scalar = 1 - (size_scalar / 10)

        self.size = self.size * size_scalar
        self.speed = self.speed * speed_scalar



if __name__ == "__main__":
    # # Create an instance of the asteroid class
    # ass = Asteroid(1)  # mode: 1 (addition) x position: 2
    # ass.create_question()
    # print("size = ", ass.size)
    # print("speed = ", ass.speed)
    # ass.size_speed_scale(30)
    # print("size = ", ass.size)
    # print("speed = ", ass.speed)


    # Generate asteroids with correct and incorrect answers
    # ass.generateAsteroids()
    # Print the array containing asteroid values


    ass = Asteroid(1, 1)
    ass.create_question()
    ass.generateAsteroids()

    for i in range(5):
         print(ass.asteroidArr[i])

    for i in range(5):
         print(ass.asteroidArr[i]["position"])


    ass.move_asteroids()
    ass.move_asteroids()

    for i in range(5):
         print(ass.asteroidArr[i]["position"])

    # print("should be false", ass.asteroidArr[0]["destroyed"])


    class test_asteroid(unittest.TestCase):

        def setUp(self):
            self.asteroid = Asteroid(1)
            self.asteroid.create_question()
            self.asteroid.generateAsteroids()

        def test_move(self):
            for i in range(5):
                self.asteroid.move_asteroids()
            self.assertEqual(self.asteroid.asteroidArr[0]["position"][1], 5, "position is wrong")

        def test_collide(self):
            for i in range (5):
                self.assertEqual(self.asteroid.asteroidArr[i]["destroyed"], True, "not destroyed")


    unittest.main()
