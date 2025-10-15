from figure import Figure
from square import Square

class Rectangle(Figure):
    def __new__(cls,a,b):
        #If both sides are equal, return a Square instead
        if a==b:
            return Square(side=a)
        return object.__new__(Rectangle)
    
    def calculate_area(self):
        """a -> base, b -> height"""
        return self.a * self.b
