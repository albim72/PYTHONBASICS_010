from dataclasses import dataclass,field

@dataclass
class Employee:
    name: str
    salary: float
    position: str = 'developer'

class EmployeeOld:
    def __init__(self, name, salary, position='developer'):
        self.name = name
        self.salary = salary
        self.position = position


emp1 = Employee('John', 1000)
emp2 = Employee('Jane', 2000)

print(emp1)
print(emp2)

emp1_old = EmployeeOld('John', 1000)
emp2_old = EmployeeOld('Jane', 2000)

print(emp1_old)
print(emp2_old)

print("_"*60)

@dataclass
class Team:
    name: str
    members: list[str] = field(default_factory=list)

    def add_member(self, person: str) -> None :
        self.members.append(person)

team = Team('Engineering')
team.add_member('John')
team.add_member('Jane')
team.add_member('Jeremy')

print(team)
