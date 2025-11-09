"""
Week 5: Association (Has-A Relationship) Examples
Topics: Composition and object relationships
"""

# Simple association - Student and Course
class Course:
    """Represents a course"""

    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

    def __str__(self):
        return f"{self.course_name} ({self.course_code})"


class Student:
    """Student with enrolled courses"""

    def __init__(self, name):
        self.name = name
        self.courses = []  # Association - Student has many Courses

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")

    def list_courses(self):
        if not self.courses:
            return f"{self.name} is not enrolled in any courses"

        courses_str = ", ".join(str(course) for course in self.courses)
        return f"{self.name}'s courses: {courses_str}"


print("=== Student-Course Association ===")
student = Student("Alice")
math = Course("Mathematics", "MATH101")
physics = Course("Physics", "PHYS101")

student.enroll(math)
student.enroll(physics)
print(student.list_courses())

# Author-Book association
class Author:
    """Represents an author"""

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name} ({self.country})"


class Book:
    """Book associated with an Author"""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author  # Association - Book has an Author
        self.pages = pages

    def info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"


print("\n=== Author-Book Association ===")
author = Author("J.K. Rowling", "UK")
book = Book("Harry Potter", author, 500)
print(book.info())

# University-Department-Professor (multi-level association)
class Professor:
    """Represents a professor"""

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"Prof. {self.name} ({self.subject})"


class Department:
    """Department with professors"""

    def __init__(self, name):
        self.name = name
        self.professors = []

    def add_professor(self, professor):
        self.professors.append(professor)

    def list_professors(self):
        return [str(prof) for prof in self.professors]


class University:
    """University with departments"""

    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def display_structure(self):
        print(f"\n{self.name}")
        for dept in self.departments:
            print(f"  Department: {dept.name}")
            for prof in dept.professors:
                print(f"    - {prof}")


print("\n=== University Structure ===")
uni = University("Tech University")

cs_dept = Department("Computer Science")
cs_dept.add_professor(Professor("Alice Smith", "AI"))
cs_dept.add_professor(Professor("Bob Johnson", "Networks"))

math_dept = Department("Mathematics")
math_dept.add_professor(Professor("Charlie Brown", "Calculus"))

uni.add_department(cs_dept)
uni.add_department(math_dept)

uni.display_structure()
