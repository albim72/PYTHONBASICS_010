from abc import ABC, abstractmethod

class Shape(ABC):
    """Inteface for all geometric shapes"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    """Implementation of the Shape interface"""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(10, 20)
print(rect.area())
print(rect.perimeter())
