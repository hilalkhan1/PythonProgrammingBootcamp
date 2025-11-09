"""
Week 1 Project: Student Grade Tracker (Version 1)
Concepts: Variables, operators, conditionals, loops, basic input/output
"""

print("=" * 50)
print("   STUDENT GRADE TRACKER - Week 1")
print("=" * 50)
print("Welcome! Track up to 5 students and their grades.")
print()

# Individual variables for each student (no lists!)
student1_name = ""
student1_grade = 0.0
student1_exists = False

student2_name = ""
student2_grade = 0.0
student2_exists = False

student3_name = ""
student3_grade = 0.0
student3_exists = False

student4_name = ""
student4_grade = 0.0
student4_exists = False

student5_name = ""
student5_grade = 0.0
student5_exists = False

# Track how many students we have
student_count = 0

# Main program loop
while True:
    print("\n" + "=" * 50)
    print("MENU:")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Count Students")
    print("4. Calculate Average Grade")
    print("5. Exit")
    print("=" * 50)

    choice = input("\nEnter your choice (1-5): ")

    if choice == '1':
        # Add student
        print("\n--- Add New Student ---")

        if student_count >= 5:
            print("Error: Maximum 5 students reached!")
        else:
            name = input("Enter student name: ")

            # Simple validation for name
            if name == "":
                print("Error: Name cannot be empty!")
            else:
                # Get grade with basic validation
                grade_input = input("Enter grade (0-100): ")

                # Check if grade is a valid number
                if grade_input.replace('.', '', 1).isdigit():
                    grade = float(grade_input)

                    if grade >= 0 and grade <= 100:
                        # Find first empty slot and add student
                        if not student1_exists:
                            student1_name = name
                            student1_grade = grade
                            student1_exists = True
                            student_count = student_count + 1
                            print(f"\n✓ Student '{name}' added with grade {grade}")
                        elif not student2_exists:
                            student2_name = name
                            student2_grade = grade
                            student2_exists = True
                            student_count = student_count + 1
                            print(f"\n✓ Student '{name}' added with grade {grade}")
                        elif not student3_exists:
                            student3_name = name
                            student3_grade = grade
                            student3_exists = True
                            student_count = student_count + 1
                            print(f"\n✓ Student '{name}' added with grade {grade}")
                        elif not student4_exists:
                            student4_name = name
                            student4_grade = grade
                            student4_exists = True
                            student_count = student_count + 1
                            print(f"\n✓ Student '{name}' added with grade {grade}")
                        elif not student5_exists:
                            student5_name = name
                            student5_grade = grade
                            student5_exists = True
                            student_count = student_count + 1
                            print(f"\n✓ Student '{name}' added with grade {grade}")
                    else:
                        print("Error: Grade must be between 0 and 100!")
                else:
                    print("Error: Please enter a valid number!")

    elif choice == '2':
        # View all students
        print("\n" + "=" * 50)
        print("ALL STUDENTS")
        print("=" * 50)

        if student_count == 0:
            print("No students in the system yet!")
        else:
            print(f"{'Name':<20} {'Grade':<10}")
            print("-" * 30)

            # Display each student if they exist
            if student1_exists:
                print(f"{student1_name:<20} {student1_grade:<10.1f}")
            if student2_exists:
                print(f"{student2_name:<20} {student2_grade:<10.1f}")
            if student3_exists:
                print(f"{student3_name:<20} {student3_grade:<10.1f}")
            if student4_exists:
                print(f"{student4_name:<20} {student4_grade:<10.1f}")
            if student5_exists:
                print(f"{student5_name:<20} {student5_grade:<10.1f}")

        print("=" * 50)

    elif choice == '3':
        # Count students
        print(f"\nTotal students: {student_count}")

    elif choice == '4':
        # Calculate average grade
        if student_count == 0:
            print("\nNo students to calculate average!")
        else:
            # Calculate sum manually
            total = 0.0
            highest = 0.0
            lowest = 100.0

            if student1_exists:
                total = total + student1_grade
                if student1_grade > highest:
                    highest = student1_grade
                if student1_grade < lowest:
                    lowest = student1_grade

            if student2_exists:
                total = total + student2_grade
                if student2_grade > highest:
                    highest = student2_grade
                if student2_grade < lowest:
                    lowest = student2_grade

            if student3_exists:
                total = total + student3_grade
                if student3_grade > highest:
                    highest = student3_grade
                if student3_grade < lowest:
                    lowest = student3_grade

            if student4_exists:
                total = total + student4_grade
                if student4_grade > highest:
                    highest = student4_grade
                if student4_grade < lowest:
                    lowest = student4_grade

            if student5_exists:
                total = total + student5_grade
                if student5_grade > highest:
                    highest = student5_grade
                if student5_grade < lowest:
                    lowest = student5_grade

            # Calculate average
            average = total / student_count
            print(f"\nClass Average: {average:.2f}")
            print(f"Highest Grade: {highest:.2f}")
            print(f"Lowest Grade: {lowest:.2f}")

    elif choice == '5':
        # Exit
        print("\nThank you for using Student Grade Tracker!")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 5.")
