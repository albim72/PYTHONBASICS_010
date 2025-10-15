import math
from figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        # Call the parent constructor with only one parameter
        super().__init__(radius)

    def calculate_area(self):
        # Formula: π × r²
        return math.pi * self.a ** 2
