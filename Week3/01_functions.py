"""
Week 3: Functions Examples
Topics: Defining functions, parameters, return values
"""

# Simple function
def greet():
    """Function with no parameters"""
    print("Hello, World!")

print("=== Simple Function ===")
greet()

# Function with parameters
def greet_person(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

print("\n=== Function with Parameters ===")
greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def add_numbers(a, b):
    """Function with multiple parameters"""
    return a + b

print("\n=== Function with Return Value ===")
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Default parameters
def power(base, exponent=2):
    """Function with default parameter"""
    return base ** exponent

print("\n=== Default Parameters ===")
print(f"2^2 = {power(2)}")
print(f"2^3 = {power(2, 3)}")

# Keyword arguments
def student_info(name, age, grade):
    """Function demonstrating keyword arguments"""
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

print("\n=== Keyword Arguments ===")
student_info(name="Alice", age=20, grade="A")
student_info(grade="B", name="Bob", age=21)  # Order doesn't matter

# *args - variable positional arguments
def sum_all(*numbers):
    """Function with variable positional arguments"""
    return sum(numbers)

print("\n=== *args ===")
print(f"Sum of 1,2,3: {sum_all(1, 2, 3)}")
print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - variable keyword arguments
def print_info(**info):
    """Function with variable keyword arguments"""
    for key, value in info.items():
        print(f"{key}: {value}")

print("\n=== **kwargs ===")
print_info(name="Alice", age=25, city="New York")

# Docstrings
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length: The length of the rectangle
        width: The width of the rectangle

    Returns:
        The area of the rectangle
    """
    return length * width

print("\n=== Docstrings ===")
print(f"Area: {calculate_area(5, 3)}")
print(f"Docstring: {calculate_area.__doc__}")
