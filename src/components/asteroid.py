#Jackson

import random

class asteroid():
    maxAsteroid : int = 50
    minAsteroid : int = 20
    numberOfAsteroids : int = 15


    def __init__(self, firstOp, secondOp, mode) -> None:
        self.firstOp = random.randint(self.minAsteroid, self.maxAsteroid)
        self.secondOp = random.randint(self.minAsteroid, self.maxAsteroid)
        self.qAnswer = firstOp + secondOp   # correct answer to question, this needs to change to reflect mode
        self.xPosition = 0
        self.yPosition = 0
       # self.aAnswer = random.randint(self.minAsteroid, self.maxAsteroid)        # answer that the asteroid will display
        self.asteroidArr = []
        self.mode = mode        # 1 for addition, 2 for subtraction, 3 for multiplication

    # def createOp1() -> None:
    #     self.firstOp = random.randint(0, 9) # figure out range

    # def createOp2() -> None:
    #     self.secondOp = random.randint(0, 9)

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
    ass = asteroid(3, 5, 1)
    ass.generateAsteroids()
    print(ass.asteroidArr)