"""
test_employee_properties_and_functions.py

A minimal test suite for employee_properties_and_functions.py
Intended for educational / live coding use during the Python training.
"""

import pytest
from employee_properties_and_functions import Employee, Manager


def test_employee_creation_and_properties():
    """Ensure an Employee can be created and its properties validated."""
    emp = Employee("Alice", 4000)
    assert emp.name == "Alice"
    assert emp.salary == 4000.0

    # Test that invalid name raises an error
    with pytest.raises(ValueError):
        emp.name = "   "  # empty after strip

    # Test that invalid salary raises an error
    with pytest.raises(ValueError):
        emp.salary = -10


def test_apply_raise_increases_salary():
    """Check that apply_raise correctly increases salary by a percentage."""
    emp = Employee("Bob", 5000)
    emp.apply_raise(10)  # +10%
    assert pytest.approx(emp.salary, rel=1e-3) == 5500.0


def test_manager_inherits_and_overrides_work(capsys):
    """Managers should override the work() method."""
    boss = Manager("Carol", 8000)
    boss.work()
    captured = capsys.readouterr()
    assert "managing the team" in captured.out


if __name__ == "__main__":
    # Run tests manually without pytest runner (for demo purposes)
    print("Running quick self-test...")
    test_employee_creation_and_properties()
    test_apply_raise_increases_salary()
    print("All manual tests passed!")
