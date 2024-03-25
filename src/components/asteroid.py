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
    speed : int = 10    # how many pixels the asteroid will move by each loop, not final
    yPos : int = 100      # will not be 100, should be the top of screen
    firstOp : int
    secondOp : int
    correctAnswer : int


    # Constructor method
    def __init__(self, mode, xPos) -> None:

        # Generate random operands within specified range
        self.firstOp = random.randint(self.minAsteroid, self.maxAsteroid)
        self.secondOp = random.randint(self.minAsteroid, self.maxAsteroid)

        # Calculate and set the correct answer to the question
        self.qAnswer = self.firstOp + self.secondOp   # correct answer to question, this needs to change to reflect mode
        # set x position from input
        # input will be an int from 1 to 5, the saved value will be multiplied by a constant to get actual position
        self.xPos = xPos * 100  # 100 is just a placeholder, will need to confirm

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

    # returns position of asteroid
    def getPosition(self) -> list:
        position = [self.xPos, self.yPos]
        return position
    
    def showEquation(self) -> str:
        eq = "%d + %d" % (self.firstOp, self.secondOp)
        return eq

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

    # .generate will create a list of asteriod dictionaries
    # from create_asteriods
    # randomize attributes
    # when asteriods are generated, append to array
    # 

    # changes Y axis position by speed amount
    def move_asteroids(self):
        self.yPos = self.yPos - self.speed
        


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


   # def destroy() -> None:
        # make asteriod dissapear

    # def isCorrect(self) -> bool:
    #     if self.aAnswer == self.qAnswer:
    #         return True
    #     else:
    #         return False
        
    
if __name__ == "__main__":
    # Create an instance of the asteroid class
    ass = asteroid(1, 2)  # mode: 1 (addition) x position: 2
    print(ass.showEquation())
    print(ass.getPosition())
    ass.move_asteroids()
    ass.move_asteroids()
    print(ass.getPosition())
    # Generate asteroids with correct and incorrect answers
    # ass.generateAsteroids()
    # Print the array containing asteroid values
    print(ass.asteroidArr)