"""
Week 2: Dictionaries Examples
Topics: Creating dictionaries, accessing values, methods
"""

# Creating dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics", "Chemistry"]
}

print("=== Creating Dictionaries ===")
print(f"Student: {student}")

# Accessing values
print("\n=== Accessing Values ===")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Grade: {student.get('grade')}")
print(f"GPA (not exists): {student.get('gpa', 'Not found')}")

# Adding and modifying
print("\n=== Adding/Modifying ===")
student["email"] = "alice@example.com"
student["age"] = 21
print(f"Updated student: {student}")

# Dictionary methods
print("\n=== Dictionary Methods ===")

# keys(), values(), items()
print(f"Keys: {student.keys()}")
print(f"Values: {student.values()}")
print(f"Items: {student.items()}")

# Iterating through dictionary
print("\n=== Iteration ===")
for key in student:
    print(f"{key}: {student[key]}")

print("\nUsing items():")
for key, value in student.items():
    print(f"{key} = {value}")

# Dictionary operations
print("\n=== Dictionary Operations ===")

# pop
removed_grade = student.pop("grade")
print(f"Removed grade: {removed_grade}")
print(f"After pop: {student}")

# update
student.update({"grade": "A+", "gpa": 3.9})
print(f"After update: {student}")

# Nested dictionaries
print("\n=== Nested Dictionaries ===")
school = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 21},
    "student3": {"name": "Charlie", "age": 19}
}

print(f"School: {school}")
print(f"Student1 name: {school['student1']['name']}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"\nSquares dictionary: {squares_dict}")
