"""
Week 3 Project: Student Grade Manager (Version 3)
Concepts: Functions, modules, imports, code organization
NEW Features:
- Modular code structure with separate modules
- Reusable functions
- Clean separation of concerns
- Subject-wise statistics
"""

# Import our custom modules
from display import show_menu, display_all_students, display_statistics, display_top_students, display_subjects, display_student
from student_operations import add_student, search_student, get_top_students
from calculations import calculate_class_statistics, find_subject_average


def main():
    """Main program function"""
    print("=" * 50)
    print("   STUDENT GRADE MANAGER - Week 3")
    print("=" * 50)
    print("Now with modular code structure!")
    print()

    # Store students as a list of dictionaries
    students = []

    # Track all unique subjects using a set
    all_subjects = set()

    # Main program loop
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            # Add student
            success, message = add_student(students, all_subjects)
            print(f"\n{'✓' if success else '✗'} {message}")

        elif choice == '2':
            # View all students
            display_all_students(students)

        elif choice == '3':
            # Search student
            search_name = input("\nEnter student name to search: ").strip()
            found_students = search_student(students, search_name)

            if found_students:
                print(f"\nFound {len(found_students)} student(s):")
                for student in found_students:
                    display_student(student)
            else:
                print("No student found with that name!")

        elif choice == '4':
            # View all unique subjects
            display_subjects(all_subjects)

        elif choice == '5':
            # Calculate class statistics
            if not students:
                print("\nNo students in the system!")
                continue

            stats = calculate_class_statistics(students)
            display_statistics(stats, len(all_subjects))

        elif choice == '6':
            # Find top students
            if not students:
                print("\nNo students in the system!")
                continue

            top_students = get_top_students(students, count=3)
            display_top_students(top_students)

        elif choice == '7':
            # Subject statistics
            if not all_subjects:
                print("\nNo subjects recorded yet!")
                continue

            print("\n--- Subject Statistics ---")
            subjects_list = sorted(list(all_subjects))

            for subject in subjects_list:
                average, count = find_subject_average(students, subject)
                print(f"{subject}:")
                print(f"  Students taking this subject: {count}")
                print(f"  Average grade: {average:.2f}")

        elif choice == '8':
            # Exit
            print("\nThank you for using Student Grade Manager!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 8.")


# This is the entry point - only run main() if this file is executed directly
if __name__ == "__main__":
    main()
