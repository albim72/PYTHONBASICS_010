from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, a, b=None):
        self.a = a
        if b:
            self.b = b
        self.message()

    @abstractmethod
    def calculate_area(self):
        """Each subclass must implement its own area calculation."""
        pass


    def message(self):
        print("This is new object of Figure class")
