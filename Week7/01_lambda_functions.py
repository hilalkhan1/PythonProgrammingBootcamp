"""
Week 7: Lambda Functions Examples
Topics: Anonymous functions, lambda with built-in functions
"""

# Simple lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments
add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")

# Lambda with sorting
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students.sort(key=lambda x: x[1], reverse=True)
print(f"Sorted by grade: {students}")

# Lambda with filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Lambda with map
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squares: {squared}")
