from figure import Figure

class Trapezoid(Figure):
    def __init__(self,a,b,h):
        super().__init__(a,b)
        self.h = h

    def calculate_area(self):
        return (self.a + self.b) * self.h / 2
