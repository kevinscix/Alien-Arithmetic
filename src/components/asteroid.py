#Jackson

import random

class asteroid():
    maxAsteroid : int 
    minAsteroid : int
    numberOfAsteroids : int


    def __init__(self, firstOp, secondOp, aAnswer) -> None:
        self.firstOp = random.randint(self.minAsteroid, self.maxAsteroid)
        self.secondOp = random.randint(self.minAsteroid, self.maxAsteroid)
        self.qAnswer = firstOp + secondOp   # correct answer to question
        self.xPosition = 0
        self.yPosition = 0
       # self.aAnswer = random.randint(self.minAsteroid, self.maxAsteroid)        # answer that the asteroid will display
        self.asteroidArr = []

    # def createOp1() -> None:
    #     self.firstOp = random.randint(0, 9) # figure out range

    # def createOp2() -> None:
    #     self.secondOp = random.randint(0, 9)

    def createAnswer(self) -> int:
        qAnswer = self.firstOp + self.secondOp
        return qAnswer


    def generateAsteroids(self):
        
        #generate the first correct answer
        #[answer]
        #generate the rest of the incorrect answers
        # for loop -1 the number of asteroids 
        # rnd int if not answer and not in asteroid 
        # store value in the array

        # for loop that creates an incorrect answer for each asteroid
        for i in range(0, self.numberOfAsteroids - 1):
            x = random.randint(self.minAsteroid, self.maxAsteroid)
            while x == self.qAnswer:
                x = random.randint(self.minAsteroid, self.maxAsteroid)
            self.asteroidArr[i] = random.randint(self.minAsteroid, self.maxAsteroid)




    # def move() -> None:
    #     yPosition = yPosition - 5 # figure out how fast to move down

   # def destroy() -> None:
        # make asteriod dissapear

    def isCorrect(self) -> bool:
        if self.aAnswer == self.qAnswer:
            return True
        else:
            return False