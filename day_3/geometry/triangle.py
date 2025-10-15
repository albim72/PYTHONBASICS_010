from figure import Figure

class Triangle(Figure):
    def calculate_area(self):
        """a -> base, b -> height"""
        return (self.a * self.b) / 2
