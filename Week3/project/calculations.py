"""
Week 3 Project: Calculations Module
Contains mathematical and statistical functions
"""


def calculate_average(grades):
    """
    Calculate average of a list of grades

    Args:
        grades: List of numeric grades

    Returns:
        float: Average grade, or 0 if list is empty
    """
    if not grades:
        return 0.0

    total = sum(grades)
    return total / len(grades)


def calculate_class_statistics(students):
    """
    Calculate overall class statistics

    Args:
        students: List of student dictionaries

    Returns:
        dict: Statistics including average, highest, lowest
    """
    if not students:
        return {
            "count": 0,
            "average": 0.0,
            "highest": 0.0,
            "lowest": 0.0
        }

    # Collect all averages
    all_averages = [student['average'] for student in students]

    stats = {
        "count": len(students),
        "average": calculate_average(all_averages),
        "highest": max(all_averages),
        "lowest": min(all_averages)
    }

    return stats


def find_subject_average(students, subject_name):
    """
    Calculate average grade for a specific subject across all students

    Args:
        students: List of student dictionaries
        subject_name: Name of the subject

    Returns:
        tuple: (average: float, count: int) - average and number of students taking the subject
    """
    subject_grades = []

    for student in students:
        if subject_name in student['grades']:
            subject_grades.append(student['grades'][subject_name])

    if not subject_grades:
        return 0.0, 0

    return calculate_average(subject_grades), len(subject_grades)
