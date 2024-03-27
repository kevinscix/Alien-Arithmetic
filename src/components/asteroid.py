#Jackson
import os
import random
import pygame

class Asteroid():
    # Class-level attributes

    # Constructor method
    def __init__(self, mode) -> None:
        self.maxAsteroid : int = 50
        self.minAsteroid : int = 1
        self.maxResultAsteroid : int = 100
        self.numberOfAsteroids : int = 5
        self.speed : float = 1    # how many pixels the asteroid will move by each loop, not final
        self.firstOp : int
        self.secondOp : int
        self.correctAnswer : int
        self.size : float = 1     # placeholder value, this will be the default size before scaling


        # Calculate and set the correct answer to the question
        self.qAnswer = 0
        # set x position from input
        # input will be an int from 1 to 5, the saved value will be multiplied by a constant to get actual position

        # Initialize array to store asteroid values
        self.asteroidArr = []
        self.question_surface = ''

        # Store the mode of the asteroid (1 for addition, 2 for subtraction, 3 for multiplication)
        self.mode = mode
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.incrementsize = 800 / self.numberOfAsteroids

        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        asteroidImagePath = os.path.join(currentPath, "..", "components", "Images", "asteroid.png")
        self.asteroidImagePath = pygame.image.load(os.path.normpath(asteroidImagePath))


    def create_question(self):
         # generate answer based on mode

        self.firstOp = random.randint(self.minAsteroid, self.maxAsteroid)
        self.secondOp = random.randint(self.minAsteroid, self.maxAsteroid)

        # Calculate and set the correct answer to the question
        self.qAnswer = self.firstOp + self.secondOp

        if self.mode == 1:
            # addition
            self.correctAnswer = self.firstOp + self.secondOp
        elif self.mode == 2:
            # subtraction
            self.correctAnswer = self.firstOp - self.secondOp
        else:
            # multiplication
            self.correctAnswer = self.firstOp * self.secondOp

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
            'destoryed' : False
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
                x = random.randint(self.minAsteroid, self.maxAsteroid)
                # Ensure the incorrect answer is not a duplicate of the correct answer
                while x in self.asteroidArr:
                    x = random.randint(self.minAsteroid, self.maxResultAsteroid)
                self.asteroidArr.append(self.create_asteroids(self.incrementsize * i, 0, x, False))

    def showEquation(self) -> str:
        eq = "%d + %d" % (self.firstOp, self.secondOp)
        return eq

    def create_question_surface(self):
        self.question_surface = self.font.render(self.showEquation(), True, (0, 0, 0))

    def size_speed_scale(self, value) -> None:
        size_scalar = value * 0.02 + 1
        speed_scalar = 1 - (size_scalar / 10)

        self.size = self.size * size_scalar
        self.speed = self.speed * speed_scalar



if __name__ == "__main__":
    # Create an instance of the asteroid class
    ass = Asteroid(1)  # mode: 1 (addition) x position: 2
    ass.create_question()
    print("size = ", ass.size)
    print("speed = ", ass.speed)
    ass.size_speed_scale(30)
    print("size = ", ass.size)
    print("speed = ", ass.speed)


    # Generate asteroids with correct and incorrect answers
    # ass.generateAsteroids()
    # Print the array containing asteroid values
