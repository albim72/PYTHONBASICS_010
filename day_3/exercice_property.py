from __future__ import annotations
from typing import List


class Employee:
    """
    A simple Employee model that demonstrates:
      - properties (encapsulation + validation)
      - functions (behaviors/actions)
      - a read-only computed property
    """

    def __init__(self, name: str, salary: float) -> None:
        self._name = name
        self._salary = salary  # monthly salary in currency units

    # ---------- Properties ----------
    @property
    def name(self) -> str:
        """Public, safe access to the employee's name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Validate before updating the name."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()

    @property
    def salary(self) -> float:
        """Public, safe access to the monthly salary."""
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """Validate before updating the salary."""
        if not isinstance(value, (int, float)):
            raise ValueError("Salary must be numeric.")
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = float(value)

    @property
    def annual_salary(self) -> float:
        """Read-only: computed on the fly from monthly salary."""
        return self._salary * 12

    # ---------- Functions (behaviors) ----------
    def work(self) -> None:
        """An action that represents behavior, not data."""
        print(f"{self._name} is working hard!")

    def apply_raise(self, percent: float) -> None:
        """
        Increase salary by a given percentage.
        Valid range is 0% to 50% to avoid unrealistic jumps.
        """
        if not isinstance(percent, (int, float)):
            raise ValueError("Percent must be numeric.")
        if not (0 <= percent <= 50):
            raise ValueError("Raise percent must be between 0 and 50.")
        self._salary *= (1 + percent / 100.0)

    # ---------- Utility ----------
    def __repr__(self) -> str:
        return f"Employee(name='{self._name}', salary={self._salary:.2f})"


class Manager(Employee):
    """
    A Manager is an Employee with a different 'work' behavior
    and a simple notion of team size.
    """

    def __init__(self, name: str, salary: float, team: List[Employee] | None = None) -> None:
        super().__init__(name, salary)
        self._team: List[Employee] = team or []

    @property
    def team_size(self) -> int:
        """Read-only: current number of direct reports."""
        return len(self._team)

    def add_report(self, emp: Employee) -> None:
        if not isinstance(emp, Employee):
            raise TypeError("Only Employee instances can be added to a team.")
        self._team.append(emp)

    def work(self) -> None:
        """Override: different behavior for managers."""
        print(f"{self.name} is managing a team of {self.team_size} people.")


class Department:
    """
    A small aggregator to show properties on collections.
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self._employees: List[Employee] = []

    def add_employee(self, emp: Employee) -> None:
        if not isinstance(emp, Employee):
            raise TypeError("Department accepts only Employee instances.")
        self._employees.append(emp)

    @property
    def headcount(self) -> int:
        return len(self._employees)

    @property
    def average_salary(self) -> float:
        """Read-only: 0.0 for empty dept, otherwise arithmetic mean."""
        if not self._employees:
            return 0.0
        return sum(e.salary for e in self._employees) / len(self._employees)

    def __repr__(self) -> str:
        return f"Department(name='{self.name}', headcount={self.headcount}, avg_salary={self.average_salary:.2f})"


# ----------------- Demo / Quick Test -----------------
if __name__ == "__main__":
    # Create employees
    alice = Employee("Alice", 4000)
    bob = Employee("Bob", 5200)

    # Behaviors (functions)
    alice.work()
    bob.apply_raise(10)
    bob.work()

    # Properties (safe data access)
    print("Alice monthly:", alice.salary, " | annual:", alice.annual_salary)
    print("Bob monthly:", bob.salary, " | annual:", bob.annual_salary)

    # Manager with reports
    mgr = Manager("Chloe", 8000)
    mgr.add_report(alice)
    mgr.add_report(bob)
    mgr.work()

    # Department aggregation
    dev = Department("Engineering")
    for person in (alice, bob, mgr):
        dev.add_employee(person)
    print(dev)  # Department summary

    # A couple of validations (uncomment to test failures)
    # alice.salary = -100     # -> ValueError
    # mgr.apply_raise(80)     # -> ValueError
    # dev.add_employee("Joe") # -> TypeError
