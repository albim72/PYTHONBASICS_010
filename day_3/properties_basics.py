class Car:
    def __init__(self,brand,speed=0):
        self._brand = brand #internal attribute (protected by convention)
        self._speed = speed #internal attribute (protected by convention)

    #classic getter and setter for brand
    def get_brand(self):
        return self._brand

    def set_brand(self,new_brand):
        if not new_brand:
            raise ValueError("Brand cannot be empty")
        self._brand = new_brand

    #modern property for speed
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self,value):
        if value < 0:
            raise ValueError("Speed cannot be negative")
        if value > 300:
            raise ValueError("Speed cannot be greater than 300")
        self._speed = value

    @property
    def status(self):
        """Read-only property thats returns the status of the car."""
        if self._speed == 0:
            return f"{self._brand} is parked"
        elif self._speed < 300:
            return f"{self._brand} is moving at {self._speed} km/h"
        else:
            return f"{self._brand} is over speeding at {self._speed} km/h!"

try:
    car = Car("Tesla")

    #using classic getter/setter
    print(car.get_brand())
    car.set_brand("BMW")
    print(car.get_brand())

    #-- using properties for speed ---
    car.speed = 100
    print(car.speed)
    print(car.status)

    car.speed = 340
    print(car.status)

    car.speed = -20

except ValueError as e:
    print(e)



