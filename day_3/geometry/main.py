from triangle import Triangle
from rectangle import Rectangle
from trapezoid import Trapezoid

tr = Triangle(3.6,7.2)
print(f"The area of {tr.__class__.__name__} is {tr.calculate_area():.2f} cm2")

r1 = Rectangle(5.6,8.7)
print(f"The area of {r1.__class__.__name__} is {r1.calculate_area():.2f} cm2")

r2 = Rectangle(4.5,4.5)
print(f"The area of {r2.__class__.__name__} is {r2.calculate_area():.2f} cm2")

tp = Trapezoid(6.8,3.4,5.6)
print(f"The area of {tp.__class__.__name__} is {tp.calculate_area():.2f} cm2")

