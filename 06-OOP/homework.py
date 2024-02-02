# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of
# tuples and return the slope and distance of the line.

class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1 # Tuple unpacking
        x2,y2 = self.coor2 # Tuple unpacking
        return ((x2-x1)**2 + (y2-y1)**2)**0.5 # Distance formula

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1) # Slope formula

