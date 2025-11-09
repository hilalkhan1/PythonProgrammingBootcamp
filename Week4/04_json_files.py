"""
Week 4: JSON File Operations Examples
Topics: Reading and writing JSON files
"""

import json

# Writing JSON file
print("=== Writing JSON File ===")

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics", "Chemistry"],
    "scores": {
        "Math": 95,
        "Physics": 92,
        "Chemistry": 88
    }
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully!")

# Reading JSON file
print("\n=== Reading JSON File ===")
with open("student.json", "r") as file:
    loaded_student = json.load(file)
    print(json.dumps(loaded_student, indent=2))

# Accessing JSON data
print("\n=== Accessing JSON Data ===")
print(f"Name: {loaded_student['name']}")
print(f"Age: {loaded_student['age']}")
print(f"Courses: {', '.join(loaded_student['courses'])}")
print(f"Math score: {loaded_student['scores']['Math']}")

# Writing list of dictionaries
print("\n=== Writing Multiple Records ===")

students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

# Reading list of dictionaries
print("\nReading multiple students:")
with open("students.json", "r") as file:
    all_students = json.load(file)
    for student in all_students:
        print(f"  {student['name']}: Age {student['age']}, Grade {student['grade']}")

# JSON to string and back
print("\n=== JSON Strings ===")

data = {"name": "Python", "version": 3.9, "features": ["simple", "powerful"]}

# Convert to JSON string
json_string = json.dumps(data, indent=2)
print("JSON string:")
print(json_string)

# Convert back to Python object
parsed_data = json.loads(json_string)
print(f"\nParsed data: {parsed_data}")

# Complex JSON structure
print("\n=== Complex JSON Structure ===")

school = {
    "name": "Tech University",
    "location": "New York",
    "departments": [
        {
            "name": "Computer Science",
            "students": [
                {"name": "Alice", "gpa": 3.8},
                {"name": "Bob", "gpa": 3.6}
            ]
        },
        {
            "name": "Mathematics",
            "students": [
                {"name": "Charlie", "gpa": 3.9},
                {"name": "David", "gpa": 3.7}
            ]
        }
    ]
}

with open("school.json", "w") as file:
    json.dump(school, file, indent=4)

print("Complex JSON structure created!")

# Reading and processing
with open("school.json", "r") as file:
    school_data = json.load(file)
    print(f"\nSchool: {school_data['name']}")
    for dept in school_data['departments']:
        print(f"\nDepartment: {dept['name']}")
        for student in dept['students']:
            print(f"  - {student['name']}: GPA {student['gpa']}")

# Updating JSON file
print("\n=== Updating JSON File ===")


def add_student_to_json(filename, new_student):
    """Add a new student to JSON file"""
    # Read existing data
    with open(filename, "r") as file:
        students = json.load(file)

    # Add new student
    students.append(new_student)

    # Write back
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)


add_student_to_json("students.json", {"name": "Eve", "age": 22, "grade": "A"})
print("Student added to JSON file!")

# Cleanup
import os
os.remove("student.json")
os.remove("students.json")
os.remove("school.json")
print("\nCleanup: JSON files removed")
