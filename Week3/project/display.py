"""
Week 3 Project: Display Module
Contains functions for displaying information to the user
"""


def show_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("MENU:")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. View All Subjects")
    print("5. Calculate Class Statistics")
    print("6. Find Top Students")
    print("7. Subject Statistics")
    print("8. Exit")
    print("=" * 50)


def display_student(student, show_number=None):
    """
    Display a single student's information

    Args:
        student: Student dictionary
        show_number: Optional number to display before name
    """
    prefix = f"{show_number}. " if show_number else ""
    print(f"\n{prefix}{student['name']} (Average: {student['average']:.2f})")
    print("   Subjects and Grades:")

    for subject, grade in student['grades'].items():
        print(f"   - {subject}: {grade:.1f}")


def display_all_students(students):
    """
    Display all students in the system

    Args:
        students: List of student dictionaries
    """
    if not students:
        print("\nNo students in the system!")
        return

    print("\n" + "=" * 70)
    print("ALL STUDENTS")
    print("=" * 70)

    for i, student in enumerate(students, start=1):
        display_student(student, show_number=i)

    print("=" * 70)


def display_statistics(stats, subject_count):
    """
    Display class statistics

    Args:
        stats: Dictionary containing statistics
        subject_count: Number of unique subjects
    """
    print("\n--- Class Statistics ---")
    print(f"Total Students: {stats['count']}")
    print(f"Total Subjects Tracked: {subject_count}")
    print(f"Class Average: {stats['average']:.2f}")
    print(f"Highest Average: {stats['highest']:.2f}")
    print(f"Lowest Average: {stats['lowest']:.2f}")


def display_top_students(top_students):
    """
    Display top performing students

    Args:
        top_students: List of student dictionaries sorted by average
    """
    print("\n--- Top Students ---")
    for i, student in enumerate(top_students, start=1):
        print(f"{i}. {student['name']}: {student['average']:.2f}")


def display_subjects(subjects):
    """
    Display all unique subjects

    Args:
        subjects: Set of subject names
    """
    if not subjects:
        print("\nNo subjects recorded yet!")
        return

    print("\n--- All Subjects ---")
    subjects_list = sorted(list(subjects))

    for i, subject in enumerate(subjects_list, start=1):
        print(f"{i}. {subject}")
