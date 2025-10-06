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
