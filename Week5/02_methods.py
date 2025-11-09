"""
Week 5: Instance, Class, and Static Methods Examples
Topics: Different types of methods in classes
"""

class Student:
    """Demonstrating instance, class, and static methods"""

    # Class variable
    total_students = 0
    school_name = "Tech University"

    def __init__(self, name, age, grade):
        # Instance variables
        self.name = name
        self.age = age
        self.grade = grade
        Student.total_students += 1

    # Instance method
    def display_info(self):
        """Instance method - accesses instance variables"""
        return f"{self.name}, Age: {self.age}, Grade: {self.grade}"

    def is_passing(self):
        """Instance method - checks if student is passing"""
        passing_grades = ['A', 'B', 'C']
        return self.grade in passing_grades

    # Class method
    @classmethod
    def get_total_students(cls):
        """Class method - accesses class variables"""
        return f"Total students: {cls.total_students}"

    @classmethod
    def set_school_name(cls, name):
        """Class method - modifies class variable"""
        cls.school_name = name

    # Static method
    @staticmethod
    def is_valid_grade(grade):
        """Static method - doesn't access instance or class variables"""
        valid_grades = ['A', 'B', 'C', 'D', 'F']
        return grade in valid_grades


print("=== Instance Methods ===")
student1 = Student("Alice", 20, "A")
student2 = Student("Bob", 21, "B")

print(student1.display_info())
print(f"Alice passing: {student1.is_passing()}")

print("\n=== Class Methods ===")
print(Student.get_total_students())
Student.set_school_name("Engineering College")
print(f"School: {Student.school_name}")

print("\n=== Static Methods ===")
print(f"Is 'A' valid: {Student.is_valid_grade('A')}")
print(f"Is 'Z' valid: {Student.is_valid_grade('Z')}")

# Another example - Temperature converter
class Temperature:
    """Temperature converter with static methods"""

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15


print("\n=== Temperature Converter ===")
print(f"0°C = {Temperature.celsius_to_fahrenheit(0)}°F")
print(f"100°C = {Temperature.celsius_to_fahrenheit(100)}°F")
print(f"32°F = {Temperature.fahrenheit_to_celsius(32)}°C")
print(f"25°C = {Temperature.celsius_to_kelvin(25)}K")
