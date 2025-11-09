"""
Week 4 Project: Student Grade Manager (Version 4)
Concepts: Error handling, file I/O, JSON, data persistence
NEW Features:
- Save student data to JSON file
- Load student data on startup
- Auto-save after each operation
- Error handling for file operations
- Input validation with try/except
"""

# Import our custom modules
from display import show_menu, display_all_students, display_statistics, display_top_students, display_subjects, display_student
from student_operations import add_student, search_student, get_top_students
from calculations import calculate_class_statistics, find_subject_average
from file_handler import save_students, load_students, create_backup


def main():
    """Main program function"""
    print("=" * 50)
    print("   STUDENT GRADE MANAGER - Week 4")
    print("=" * 50)
    print("Now with data persistence!")
    print()

    # Load existing data
    print("Loading existing data...")
    students, all_subjects, load_message = load_students()
    print(load_message)
    print()

    # Main program loop
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            # Add student
            success, message = add_student(students, all_subjects)
            print(f"\n{'✓' if success else '✗'} {message}")

            # Auto-save after adding
            if success:
                save_success, save_msg = save_students(students)
                if save_success:
                    print("✓ Data saved automatically")
                else:
                    print(f"⚠ Warning: {save_msg}")

        elif choice == '2':
            # View all students
            display_all_students(students)

        elif choice == '3':
            # Search student
            try:
                search_name = input("\nEnter student name to search: ").strip()

                if not search_name:
                    print("Error: Search name cannot be empty!")
                    continue

                found_students = search_student(students, search_name)

                if found_students:
                    print(f"\nFound {len(found_students)} student(s):")
                    for student in found_students:
                        display_student(student)
                else:
                    print("No student found with that name!")

            except KeyboardInterrupt:
                print("\nSearch cancelled.")
            except Exception as e:
                print(f"Error during search: {str(e)}")

        elif choice == '4':
            # View all unique subjects
            display_subjects(all_subjects)

        elif choice == '5':
            # Calculate class statistics
            if not students:
                print("\nNo students in the system!")
                continue

            try:
                stats = calculate_class_statistics(students)
                display_statistics(stats, len(all_subjects))
            except Exception as e:
                print(f"Error calculating statistics: {str(e)}")

        elif choice == '6':
            # Find top students
            if not students:
                print("\nNo students in the system!")
                continue

            try:
                # Get number of top students to display
                count_input = input("How many top students to display? (default: 3): ").strip()

                if count_input and count_input.isdigit():
                    count = int(count_input)
                else:
                    count = 3

                top_students = get_top_students(students, count=count)
                display_top_students(top_students)

            except ValueError:
                print("Error: Invalid number entered. Using default (3).")
                top_students = get_top_students(students, count=3)
                display_top_students(top_students)
            except Exception as e:
                print(f"Error finding top students: {str(e)}")

        elif choice == '7':
            # Subject statistics
            if not all_subjects:
                print("\nNo subjects recorded yet!")
                continue

            try:
                print("\n--- Subject Statistics ---")
                subjects_list = sorted(list(all_subjects))

                for subject in subjects_list:
                    average, count = find_subject_average(students, subject)
                    print(f"{subject}:")
                    print(f"  Students taking this subject: {count}")
                    print(f"  Average grade: {average:.2f}")

            except Exception as e:
                print(f"Error calculating subject statistics: {str(e)}")

        elif choice == '8':
            # Exit
            print("\nSaving data before exit...")

            # Create backup before final save
            backup_success, backup_msg = create_backup()
            if backup_success:
                print(f"✓ {backup_msg}")

            # Final save
            save_success, save_msg = save_students(students)

            if save_success:
                print(f"✓ {save_msg}")
                print("\nThank you for using Student Grade Manager!")
                print("Goodbye!")
                break
            else:
                print(f"⚠ Warning: {save_msg}")
                confirm = input("Exit anyway? (y/n): ").lower()
                if confirm == 'y':
                    print("\nGoodbye!")
                    break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 8.")


# This is the entry point - only run main() if this file is executed directly
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n\nFatal error: {str(e)}")
        print("Program terminated unexpectedly.")
