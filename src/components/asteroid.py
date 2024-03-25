#Jackson
import os
import sys
import random
import pygame


class asteroid():
    # Class-level attributes
    maxAsteroid : int = 50
    minAsteroid : int = 20
    numberOfAsteroids : int = 15


    # Constructor method
    def __init__(self, firstOp, secondOp, mode) -> None:

        # Generate random operands within specified range
        self.firstOp = random.randint(self.minAsteroid, self.maxAsteroid)
        self.secondOp = random.randint(self.minAsteroid, self.maxAsteroid)

        # Calculate and set the correct answer to the question
        self.qAnswer = firstOp + secondOp   # correct answer to question, this needs to change to reflect mode

        # Initialize position
        self.xPosition = 0
        self.yPosition = 0

        # Initialize array to store asteroid values
       # self.aAnswer = random.randint(self.minAsteroid, self.maxAsteroid)        # answer that the asteroid will display
        self.asteroidArr = []

        # Store the mode of the asteroid (1 for addition, 2 for subtraction, 3 for multiplication)
        self.mode = mode     

    # def createOp1() -> None:
    #     self.firstOp = random.randint(0, 9) # figure out range

    # def createOp2() -> None:
    #     self.secondOp = random.randint(0, 9)

    # Method to create correct answer based on the mode
    def createAnswer(self) -> int:
        if self.mode == 1:
            # addition
            qAnswer = self.firstOp + self.secondOp
        elif self.mode == 2:
            # subtraction
            qAnswer = self.firstOp - self.secondOp
        else:
            # multiplication
            qAnswer = self.firstOp * self.secondOp
        return qAnswer


    def create_asteroids(self, ships):
        # choose one of the ships as target for fire
        fire_target = random.choice(ships)
    
        # load image of ship
        surf = pygame.image.load(os.path.join(RES_FOLDER, 'aliens.png'))
        
        # scale it to smaller size and make it quadratic
        surf = pygame.transform.scale(surf, (70, 70))
        return {
            'surface': surf.convert_alpha(),
            'position': [randrange(892), -64],
            'speed': 4,
            'fire_target': fire_target,
            'angle': 0,
            'ticks_to_laser': 25
        }

    def move_asteroids(self):
        pass


    # Method to generate asteroids with correct and incorrect answers
    def generateAsteroids(self):
        
        #generate the first correct answer
        #[answer]
        #generate the rest of the incorrect answers
        # for loop -1 the number of asteroids 
        # rnd int if not answer and not in asteroid 
        # store value in the array
        correctAnswer = self.createAnswer()
        print(correctAnswer)
        self.asteroidArr.append(correctAnswer)
        # for loop that creates an incorrect answer for each asteroid
        for i in range(0, self.numberOfAsteroids - 1):
            x = random.randint(self.minAsteroid, self.maxAsteroid)
            # Ensure the incorrect answer is not a duplicate of the correct answer
            while x in self.asteroidArr:
                x = random.randint(self.minAsteroid, self.maxAsteroid)
            self.asteroidArr.append(x)


    # def move() -> None:
    #     yPosition = yPosition - 5 # figure out how fast to move down

   # def destroy() -> None:
        # make asteriod dissapear

    # def isCorrect(self) -> bool:
    #     if self.aAnswer == self.qAnswer:
    #         return True
    #     else:
    #         return False
        
    
if __name__ == "__main__":
    # Create an instance of the asteroid class
    ass = asteroid(3, 5, 1)  # Example operands: 3, 5; Mode: Addition (1)
    # Generate asteroids with correct and incorrect answers
    ass.generateAsteroids()
    # Print the array containing asteroid values
    print(ass.asteroidArr)