"""
Week 2 Project: Student Grade Manager (Version 2)
Concepts: Lists, dictionaries, tuples, sets, string methods
NEW Features:
- Multiple subjects per student
- Use dictionaries to store student data
- Search students by name
- Track unique subjects with sets
"""

print("=" * 50)
print("   STUDENT GRADE MANAGER - Week 2")
print("=" * 50)
print("Now with multiple subjects support!")
print()

# Store students as a list of dictionaries
students = []

# Track all unique subjects using a set
all_subjects = set()

# Main program loop
while True:
    print("\n" + "=" * 50)
    print("MENU:")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. View All Subjects")
    print("5. Calculate Class Statistics")
    print("6. Find Top Students")
    print("7. Exit")
    print("=" * 50)

    choice = input("\nEnter your choice (1-7): ")

    if choice == '1':
        # Add student with multiple subjects
        print("\n--- Add New Student ---")
        name = input("Enter student name: ").strip()

        if not name:
            print("Error: Name cannot be empty!")
            continue

        # Get number of subjects
        num_subjects_str = input("How many subjects? ")

        if not num_subjects_str.isdigit():
            print("Error: Please enter a valid number!")
            continue

        num_subjects = int(num_subjects_str)

        if num_subjects <= 0:
            print("Error: Must have at least 1 subject!")
            continue

        # Dictionary to store this student's grades
        grades = {}

        # Get grades for each subject
        for i in range(num_subjects):
            subject = input(f"Enter subject {i + 1} name: ").strip().title()

            if not subject:
                print("Error: Subject name cannot be empty!")
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

        # Calculate average
        total = 0
        for grade in grades.values():
            total = total + grade
        average = total / len(grades)

        # Create student dictionary
        student = {
            "name": name,
            "grades": grades,
            "average": round(average, 2)
        }

        students.append(student)
        print(f"\n✓ Student '{name}' added with {len(grades)} subjects!")
        print(f"  Average: {average:.2f}")

    elif choice == '2':
        # View all students
        if not students:
            print("\nNo students in the system!")
            continue

        print("\n" + "=" * 70)
        print("ALL STUDENTS")
        print("=" * 70)

        for i in range(len(students)):
            student = students[i]
            print(f"\n{i + 1}. {student['name']} (Average: {student['average']})")
            print("   Subjects and Grades:")

            # Display each subject and grade
            for subject, grade in student['grades'].items():
                print(f"   - {subject}: {grade:.1f}")

        print("=" * 70)

    elif choice == '3':
        # Search student by name
        search_name = input("\nEnter student name to search: ").strip().lower()

        found = False
        for student in students:
            if search_name in student['name'].lower():
                print("\n--- Student Found ---")
                print(f"Name: {student['name']}")
                print(f"Average: {student['average']}")
                print("Grades:")
                for subject, grade in student['grades'].items():
                    print(f"  - {subject}: {grade:.1f}")
                found = True
                print()

        if not found:
            print("No student found with that name!")

    elif choice == '4':
        # View all unique subjects
        if not all_subjects:
            print("\nNo subjects recorded yet!")
        else:
            print("\n--- All Subjects ---")
            # Convert set to sorted list for display
            subjects_list = list(all_subjects)
            subjects_list.sort()

            for i in range(len(subjects_list)):
                print(f"{i + 1}. {subjects_list[i]}")

    elif choice == '5':
        # Calculate class statistics
        if not students:
            print("\nNo students in the system!")
            continue

        # Collect all averages
        all_averages = []
        for student in students:
            all_averages.append(student['average'])

        # Calculate class average
        total = 0
        for avg in all_averages:
            total = total + avg
        class_average = total / len(all_averages)

        # Find highest and lowest
        highest = all_averages[0]
        lowest = all_averages[0]
        for avg in all_averages:
            if avg > highest:
                highest = avg
            if avg < lowest:
                lowest = avg

        print("\n--- Class Statistics ---")
        print(f"Total Students: {len(students)}")
        print(f"Total Subjects Tracked: {len(all_subjects)}")
        print(f"Class Average: {class_average:.2f}")
        print(f"Highest Average: {highest:.2f}")
        print(f"Lowest Average: {lowest:.2f}")

    elif choice == '6':
        # Find top 3 students
        if not students:
            print("\nNo students in the system!")
            continue

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

        print("\n--- Top Students ---")
        top_count = 3 if len(sorted_students) >= 3 else len(sorted_students)

        for i in range(top_count):
            student = sorted_students[i]
            print(f"{i + 1}. {student['name']}: {student['average']:.2f}")

    elif choice == '7':
        # Exit
        print("\nThank you for using Student Grade Manager!")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 7.")
