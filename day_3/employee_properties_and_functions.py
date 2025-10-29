"""
employee_properties_and_functions.py

A minimal, well‑commented example for a training session:
- Shows how to use properties for data validation (encapsulation).
- Shows how to implement methods for behavior.
- Includes a simple subclass that overrides a method.
"""

from __future__ import annotations


class Employee:
    """
    Employee represents a single worker with a validated name and salary.

    Key ideas demonstrated:
    - Encapsulation: internal attributes are "private" (_name, _salary).
    - Properties: public, validated access to internal data (name, salary).
    - Behavior: functions (methods) that do actions (work, apply_raise).
    """

    def __init__(self, name: str, salary: float) -> None:
        # --- Initialization block: set validated starting state ---
        # We route through the properties to reuse the same validation logic
        # that will be used for later assignments.
        self._name: str | None = None
        self._salary: float | None = None

        self.name = name      # triggers validation in the setter
        self.salary = salary  # triggers validation in the setter

    # -------------------------------
    # Properties for validated fields
    # -------------------------------

    @property
    def name(self) -> str:
        """Public, validated access to the employee's name."""
        return self._name  # type: ignore[return-value]

    @name.setter
    def name(self, value: str) -> None:
        """
        Validate and set the employee's name.
        Rules:
          - must be a non-empty string after stripping whitespace
        """
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("name cannot be empty")
        self._name = cleaned

    @property
    def salary(self) -> float:
        """Public, validated access to the employee's salary (float)."""
        return self._salary  # type: ignore[return-value]

    @salary.setter
    def salary(self, value: float) -> None:
        """
        Validate and set the employee's salary.
        Rules:
          - must be a number (int or float)
          - must be >= 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("salary must be a number")
        if value < 0:
            raise ValueError("salary cannot be negative")
        self._salary = float(value)

    # --------------------
    # Behavioral functions
    # --------------------

    def work(self) -> None:
        """
        Simulate a simple 'work' action by printing a message.
        (In real apps, this might log an action or update state.)
        """
        print(f"{self.name} is working hard!")

    def apply_raise(self, percent: float) -> None:
        """
        Increase salary by a given percentage.
        Example: percent=10 increases 4000.0 to 4400.0

        Notes:
          - Accepts negative values to represent a pay cut (e.g., -5),
            but disallows a raise that would drop salary below 0.
        """
        if not isinstance(percent, (int, float)):
            raise TypeError("percent must be a number")

        # Calculate the new salary using the percentage delta.
        factor = 1.0 + (percent / 100.0)
        new_salary = self.salary * factor

        if new_salary < 0:
            raise ValueError("resulting salary cannot be negative")
        self.salary = new_salary

    # -------------
    # Nice-to-haves
    # -------------

    def __repr__(self) -> str:  # helpful for debugging / REPL
        return f"Employee(name={self.name!r}, salary={self.salary:.2f})"


class Manager(Employee):
    """
    Manager is a specialized Employee that overrides the work() behavior.
    Demonstrates inheritance and method overriding.
    """

    def work(self) -> None:
        """Managers 'work' by managing the team."""
        print(f"{self.name} is managing the team.")


# ---------------------
# Demo / quick self-test
# ---------------------
if __name__ == "__main__":
    # --- Create an Employee and inspect validated properties ---
    emp = Employee("Alice", 4000)
    print(emp.name)    # -> Alice
    print(emp.salary)  # -> 4000.0

    # --- Call a behavior method ---
    emp.work()         # -> Alice is working hard!

    # --- Apply a raise and verify the result ---
    emp.apply_raise(10)  # +10%
    print(emp.salary)    # -> 4400.0

    # --- Show validation in action (should raise ValueError) ---
    try:
        emp.salary = -2000
    except ValueError as e:
        print(f"Validation works: {e}")

    # --- Demonstrate subclass override ---
    boss = Manager("Bob", 9000)
    boss.work()  # -> Bob is managing the team.
