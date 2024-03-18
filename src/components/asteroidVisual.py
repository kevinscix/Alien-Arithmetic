import asteroid

class asteroidVisual(asteroid): # causes an error with module when asteroid is in the brackets

    speed : int = 10    # how many pixels the asteroid will move by each loop, not final
    size : int
    yPos : int = 100      # will not be 100, should be the top of screen

    # constructor
    def __init__(self, angle, size, xPos) -> None:
        self.angle = angle
        self.size = size
        self.xPos = xPos

    # moves the asteroid down by the speed
    # somewhere there will need to be a loop that calls this until the question is answered
    def move(self) -> None:
        self.yPos = self.yPos - self.speed

    # returns the angle that the asteroid sprite will be displayed at
    # this is so each asteroid will look different
    # there will need to be a random generator for this value where the object is created
    def getAngle(self) -> int:
        return self.angle
    
    # returns size value of asteroid sprite
    def getSize(self) -> int:
        return self.size
    
    # returns the position of the asteroid in the for [x, y]
    def getPos(self) -> list:
        position = [self.xPos, self.yPos]
        return position
    

    



if __name__ == "__main__":
    ass1 = asteroidVisual(90, 50, 3)
    pos = ass1.getPos()
    print(pos)
    ass1.move()
    ass1.move()
    pos2 = ass1.getPos()
    print(pos2)
    print(ass1.getSize())
    print(ass1.getAngle())
