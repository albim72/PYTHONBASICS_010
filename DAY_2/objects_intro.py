#definition of the simplest class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(Car)


car1 = Car("BMW", "550i")
print(car1.brand)
print(car1.model)

car2 = Car("Mercedes", "B-Class")
print(car2.brand)
print(car2.model)

print("_"*60)
#method inside a class
class Rectangle:
    _color = "red"
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    #getter function
    def color(self):
        return self._color

    #setter function
    def change_color(self, new_color):
        self._color = new_color

r1 = Rectangle(10, 20)
print(r1.area())
print(r1.color())
r1.change_color("blue")
print(r1.color())

print("_"*60)

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "?????"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        return "Meow!"

dog1 = Dog("Ludvik","English Bulldog")
print(f"the dog sound is {dog1.sound()}")

cat = Cat("Ator","Black")
print(f"the cat sound is {cat.sound()}")

dog2 = Dog("Rocky","Belgian Sheepdog")
print(f"the dog sound is {dog2.sound()}")
