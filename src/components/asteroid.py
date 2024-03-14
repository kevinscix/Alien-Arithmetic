#Jackson

import random

class asteroid():

    def __init__(self, firstOp, secondOp, aAnswer) -> None:
        self.firstOp = random.randint(0, 9)
        self.secondOp = random.randint(0, 9)
        self.qAnswer = firstOp + secondOp   # correct answer to question
        self.xPosition = 0
        self.yPosition = 0
        self.aAnswer = random.randint(0, 9)        # answer that the asteroid will display


    # def createOp1() -> None:
    #     self.firstOp = random.randint(0, 9) # figure out range

    # def createOp2() -> None:
    #     self.secondOp = random.randint(0, 9)

    def createAnswer(self) -> None:
        qAnswer = self.firstOp + self.secondOp

    def move() -> None:
        yPosition = yPosition - 5 # figure out how fast to move down

   # def destroy() -> None:
        # make asteriod dissapear

    def isCorrect(self) -> bool:
        if self.aAnswer == self.qAnswer:
            return True
        else:
            return False