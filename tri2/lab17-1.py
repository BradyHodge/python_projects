# ----------------------
# Made by Brady Hodge
# Status: Omitted
# lab 17-1; 1/1
# ----------------------

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distanceFromPoint(self, initX, initY):
        return (self.x - initX) + (self.y - initY)



p = Point(7, 6)
print(p.distanceFromOrigin())
print(p.distanceFromPoint(4, 8))
