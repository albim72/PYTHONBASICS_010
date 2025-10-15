from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.message()
        
    @abstractmethod
    def calculate_area(self):
        """Each figure has its own area calculation method."""
        pass
    
    def message(self):
        print("This is new object of Figure class")
