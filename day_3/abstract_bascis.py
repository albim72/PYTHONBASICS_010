from abc import ABC, abstractmethod

#abstract base class
class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        """Every subclass must define this method."""
        pass


#concrete subclasses
class Student(Person):
    def get_role(self):
        return f"Student: {self.name}"

class Teacher(Person):
    def get_role(self):
        return f"Teacher: {self.name}"

people = [Student("John Brown"), Student("Alice Roberts"), Teacher("Dr Mary Smith")]

for person in people:
    print(person.get_role())
