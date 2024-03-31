import asteroid

class asteroidVisual(asteroid): # causes an error with module when asteroid is in the brackets

    speed : int = 10    # how many pixels the asteroid will move by each loop, not final
    size : int
    yPos : int = 100      # will not be 100, should be the top of screen

    
    def __init__(self, angle, size, xPos) -> None:
        """
        Initializes a new asteroidVisual object.

        Args:
            angle (int): Angle at which the asteroid sprite will be displayed.
            size (int): Size of the asteroid sprite.
            xPos (int): X-coordinate of the asteroid's position.
        """
        self.angle = angle
        self.size = size
        self.xPos = xPos

   
    def move(self) -> None:
        """
        Moves the asteroid downwards by its speed.
        """
        self.yPos = self.yPos - self.speed

    def getAngle(self) -> int:
        """
        Returns:
            int: Angle of the asteroid sprite.
        """
        return self.angle
    
    def getSize(self) -> int:
        return self.size
    
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
