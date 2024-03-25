#Jackson
import os
import sys
import random
import pygame


class Asteroid():
    # Class-level attributes
    maxAsteroid : int = 50
    minAsteroid : int = 1
    maxResultAsteroid : int = 100
    numberOfAsteroids : int = 5
    speed : int = 10    # how many pixels the asteroid will move by each loop, not final
    yPos : int = 100      # will not be 100, should be the top of screen
    firstOp : int
    secondOp : int
    correctAnswer : int



    # Constructor method
    def __init__(self, mode) -> None:

        # Generate random operands within specified range
        self.firstOp = random.randint(self.minAsteroid, self.maxAsteroid)
        self.secondOp = random.randint(self.minAsteroid, self.maxAsteroid)

        # Calculate and set the correct answer to the question
        self.qAnswer = self.firstOp + self.secondOp   # correct answer to question, this needs to change to reflect mode
        # set x position from input
        # input will be an int from 1 to 5, the saved value will be multiplied by a constant to get actual position
       
        # Initialize array to store asteroid values
        self.asteroidArr = []


        # Store the mode of the asteroid (1 for addition, 2 for subtraction, 3 for multiplication)
        self.mode = mode

        # generate answer based on mode
        if self.mode == 1:
            # addition
            self.correctAnswer = self.firstOp + self.secondOp
        elif self.mode == 2:
            # subtraction
            self.correctAnswer = self.firstOp - self.secondOp
        else:
            # multiplication
            self.correctAnswer = self.firstOp * self.secondOp     
    
        self.incrementsize = 800 / self.numberOfAsteroids

        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        asteroidImagePath = os.path.join(currentPath, "..", "components", "Images", "asteroid.png")
        self.asteroidImagePath = pygame.image.load(os.path.normpath(asteroidImagePath))
        self.asteroids = []

    def create_asteroids(self, x, y, value, isCorrect):
        # scale it to smaller size and make it quadratic
        surf = pygame.transform.scale(self.asteroidImagePath, (70, 70))
        
        return {
            'surface': surf,
            'position': [x, y],
            'value' : value,
            'speed': self.speed,
            'angle': 0,
            'correct' : isCorrect
        }

    # .generate will create a list of asteriod dictionaries
    # from create_asteriods
    # randomize attributes
    # when asteriods are generated, append to array

    # changes Y axis position by speed amount
    def move_asteroids(self):
        for asteroid in self.asteroidArr:
            asteroid['position'][1] -= self.speed
        
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
       
       print(self.correctAnswer)

       picked = random.randint(1, self.numberOfAsteroids) - 1
       for i in range(0, self.numberOfAsteroids - 1):
            if picked == i:
                self.asteroidArr.append(self.create_asteroids(self.incrementsize * i, 650, self.correctAnswer, True))
            else:
                x = random.randint(self.minAsteroid, self.maxAsteroid)
                # Ensure the incorrect answer is not a duplicate of the correct answer
                while x in self.asteroidArr:
                    x = random.randint(self.minAsteroid, self.maxResultAsteroid)
                self.asteroidArr.append(self.create_asteroids(self.incrementsize * i, 650, x, False))


    def showEquation(self) -> str:
        eq = "%d + %d" % (self.firstOp, self.secondOp)
        return eq
    
    def collision(self) -> None:
        
        pass

        
    
if __name__ == "__main__":
    # Create an instance of the asteroid class
    ass = Asteroid(1)  # mode: 1 (addition) x position: 2
    print(ass.showEquation())
    ass.move_asteroids()
    ass.move_asteroids()

    ass.generateAsteroids()
    print(ass.asteroidArr)
    ass.move_asteroids()
    ass.move_asteroids()
    ass.move_asteroids()
    print(ass.asteroidArr)


    # Generate asteroids with correct and incorrect answers
    # ass.generateAsteroids()
    # Print the array containing asteroid values
    