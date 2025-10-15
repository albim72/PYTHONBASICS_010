"""
Optional Challenge – Classes, Inheritance, File Handling, and Error Management
"""


# Base class: Person
class Person:
    def __init__(self, name, age):
        # Validate that age is numeric
        if not isinstance(age, (int, float)):
            raise ValueError("Age must be a numeric value.")
        self.name = name
        self.age = age

    def info(self):
        """Return a formatted description of the person."""
        return f"Name: {self.name}, Age: {self.age}"


# Subclass: Student (inherits from Person)
class Student(Person):
    def __init__(self, name, age, grade):
        # Initialize the base class first
        super().__init__(name, age)

        # Validate grade
        if not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a numeric value.")
        self.grade = grade

    def info(self):
        """Override the info() method to include the grade."""
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


# Function for saving students to a file
def save_to_file(students, filename="students.txt"):
    """Save all students to a text file, handling possible file errors."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for student in students:
                file.write(f"{student.name} | {student.age} | {student.grade}\n")
        print(f"Successfully saved {len(students)} students to '{filename}'.")

    except IOError:
        print("Error: Could not write to file. Check file permissions or disk space.")

    finally:
        print("End of program – file operation completed.")


# Main execution
if __name__ == "__main__":
    try:
        # Create a few students
        students = [
            Student("Alice", 20, 4.5),
            Student("Bob", 22, 3.8),
            Student("Charlie", 19, 4.9)
        ]

        # Display info for each student
        for s in students:
            print(s.info())

        # Save data to file
        save_to_file(students)

    except ValueError as e:
        print(f"Data error: {e}")
