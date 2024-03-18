import asteroid

class asteroidVisual(asteroid):

    speed : int = 10    # how many pixels the asteroid will move by each loop, not final
    size : int
    yPos : int = 100      # will not be 100, should be the top of screen

    def __init__(self, angle, size, xPos) -> None:
        self.angle = angle
        self.size = size
        self.xPos = xPos

    def move(speed) -> None:
        yPos = yPos - speed

    def getAngle(self) -> int:
        return self.angle
    
    def getSize(self) -> int:
        return self.size
    
    def getPos(self, yPos) -> list:
        position = [self.xPos, yPos]
        return position
    

    



if __name__ == "__main__":
    ass1 = asteroidVisual(90, 50, 3)
   # ass1.move
   # ass1.move
    pos = ass1.getPos
    print(pos[0])
