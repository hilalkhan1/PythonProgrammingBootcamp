"""
Week 3 Project: Student Operations Module
Contains functions for adding, searching, and managing students
"""


def add_student(students, all_subjects):
    """
    Add a new student with multiple subjects

    Args:
        students: List of student dictionaries
        all_subjects: Set of all subjects

    Returns:
        tuple: (success: bool, message: str)
    """
    print("\n--- Add New Student ---")
    name = input("Enter student name: ").strip()

    if not name:
        return False, "Error: Name cannot be empty!"

    # Get number of subjects
    num_subjects_str = input("How many subjects? ")

    if not num_subjects_str.isdigit():
        return False, "Error: Please enter a valid number!"

    num_subjects = int(num_subjects_str)

    if num_subjects <= 0:
        return False, "Error: Must have at least 1 subject!"

    # Dictionary to store this student's grades
    grades = {}

    # Get grades for each subject
    for i in range(num_subjects):
        subject = input(f"Enter subject {i + 1} name: ").strip().title()

        if not subject:
            print("Error: Subject name cannot be empty! Skipping...")
            continue

        # Get grade with validation
        valid_grade = False
        while not valid_grade:
            grade_str = input(f"Enter grade for {subject} (0-100): ")

            if grade_str.replace('.', '', 1).isdigit():
                grade = float(grade_str)
                if 0 <= grade <= 100:
                    grades[subject] = grade
                    all_subjects.add(subject)  # Add to set of all subjects
                    valid_grade = True
                else:
                    print("Grade must be between 0 and 100!")
            else:
                print("Please enter a valid number!")

    # Calculate average using helper function
    from calculations import calculate_average
    average = calculate_average(list(grades.values()))

    # Create student dictionary
    student = {
        "name": name,
        "grades": grades,
        "average": round(average, 2)
    }

    students.append(student)
    return True, f"Student '{name}' added with {len(grades)} subjects! Average: {average:.2f}"


def search_student(students, search_name):
    """
    Search for students by name

    Args:
        students: List of student dictionaries
        search_name: Name to search for

    Returns:
        list: List of matching students
    """
    found_students = []
    search_lower = search_name.lower()

    for student in students:
        if search_lower in student['name'].lower():
            found_students.append(student)

    return found_students


def get_top_students(students, count=3):
    """
    Get top students sorted by average grade

    Args:
        students: List of student dictionaries
        count: Number of top students to return

    Returns:
        list: Sorted list of top students
    """
    # Sort students by average (bubble sort - descending)
    sorted_students = students.copy()

    n = len(sorted_students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_students[j]['average'] < sorted_students[j + 1]['average']:
                # Swap
                temp = sorted_students[j]
                sorted_students[j] = sorted_students[j + 1]
                sorted_students[j + 1] = temp

    # Return top 'count' students
    top_count = count if len(sorted_students) >= count else len(sorted_students)
    return sorted_students[:top_count]
