"""
Week 6 Project: Library Management System (Version 2)
Concepts: Inheritance, Polymorphism, Encapsulation, Abstraction
NEW Features:
- Book hierarchy: Book, EBook, PhysicalBook
- Member hierarchy: Member, StudentMember, TeacherMember
- Different borrowing limits and loan periods based on type
- Properties and encapsulation with getters/setters
"""

from books import Book, EBook, PhysicalBook
from members import Member, StudentMember, TeacherMember
from library import Library


def show_menu():
    """Display main menu"""
    print("\n" + "=" * 60)
    print("LIBRARY MENU:")
    print("1. Add Book (Physical/EBook)")
    print("2. Add Member (Regular/Student/Teacher)")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Books")
    print("6. View All Books")
    print("7. View All Members")
    print("8. View Books by Type")
    print("9. View Members by Type")
    print("10. View Member's Borrowed Books")
    print("11. View Overdue Books")
    print("12. Save & Exit")
    print("=" * 60)


def add_book(library):
    """Add a new book to the library"""
    print("\n--- Add New Book ---")
    print("Select book type:")
    print("1. Physical Book")
    print("2. EBook")

    book_type = input("Enter choice (1-2): ").strip()

    isbn = input("Enter ISBN: ").strip()
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()

    try:
        year = int(input("Enter publication year: ").strip())

        if book_type == '1':
            # Physical book
            shelf = input("Enter shelf location (e.g., A3-15): ").strip()
            print("Condition options: New, Good, Fair, Poor")
            condition = input("Enter condition (default: Good): ").strip() or "Good"

            book = PhysicalBook(isbn, title, author, year, shelf, condition)

        elif book_type == '2':
            # EBook
            file_size = float(input("Enter file size (MB): ").strip())
            file_format = input("Enter file format (PDF/EPUB/MOBI): ").strip()

            book = EBook(isbn, title, author, year, file_size, file_format)

        else:
            print("✗ Invalid book type!")
            return

        success, message = library.add_book(book)
        print(f"{'✓' if success else '✗'} {message}")

    except ValueError as e:
        print(f"✗ Invalid input: {e}")


def add_member(library):
    """Add a new member to the library"""
    print("\n--- Add New Member ---")
    print("Select member type:")
    print("1. Regular Member")
    print("2. Student Member")
    print("3. Teacher Member")

    member_type = input("Enter choice (1-3): ").strip()

    member_id = input("Enter member ID: ").strip()
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()

    if member_type == '1':
        # Regular member
        member = Member(member_id, name, email)

    elif member_type == '2':
        # Student member
        student_id = input("Enter student ID: ").strip()
        major = input("Enter major: ").strip()
        member = StudentMember(member_id, name, email, student_id, major)

    elif member_type == '3':
        # Teacher member
        faculty_id = input("Enter faculty ID: ").strip()
        department = input("Enter department: ").strip()
        member = TeacherMember(member_id, name, email, faculty_id, department)

    else:
        print("✗ Invalid member type!")
        return

    success, message = library.add_member(member)
    print(f"{'✓' if success else '✗'} {message}")
    if success:
        print(f"  Max books: {member.max_books}")


def view_books_by_type(library):
    """View books filtered by type"""
    print("\n--- View Books by Type ---")
    print("1. Physical Books")
    print("2. EBooks")
    print("3. All Books")

    choice = input("Enter choice (1-3): ").strip()

    if choice == '1':
        books = library.get_books_by_type("PhysicalBook")
        print(f"\n{'='*80}\nPHYSICAL BOOKS ({len(books)} total)\n{'='*80}")
    elif choice == '2':
        books = library.get_books_by_type("EBook")
        print(f"\n{'='*80}\nEBOOKS ({len(books)} total)\n{'='*80}")
    elif choice == '3':
        books = list(library.books.values())
        print(f"\n{'='*80}\nALL BOOKS ({len(books)} total)\n{'='*80}")
    else:
        print("✗ Invalid choice!")
        return

    if not books:
        print("No books found!")
    else:
        for book in books:
            print(f"  {book}")

    print("=" * 80)


def view_members_by_type(library):
    """View members filtered by type"""
    print("\n--- View Members by Type ---")
    print("1. Regular Members")
    print("2. Student Members")
    print("3. Teacher Members")
    print("4. All Members")

    choice = input("Enter choice (1-4): ").strip()

    if choice == '1':
        members = library.get_members_by_type("Member")
        print(f"\n{'='*80}\nREGULAR MEMBERS ({len(members)} total)\n{'='*80}")
    elif choice == '2':
        members = library.get_members_by_type("Student")
        print(f"\n{'='*80}\nSTUDENT MEMBERS ({len(members)} total)\n{'='*80}")
    elif choice == '3':
        members = library.get_members_by_type("Teacher")
        print(f"\n{'='*80}\nTEACHER MEMBERS ({len(members)} total)\n{'='*80}")
    elif choice == '4':
        members = list(library.members.values())
        print(f"\n{'='*80}\nALL MEMBERS ({len(members)} total)\n{'='*80}")
    else:
        print("✗ Invalid choice!")
        return

    if not members:
        print("No members found!")
    else:
        for member in members:
            print(f"  {member}")

    print("=" * 80)


def view_member_books(library):
    """View books borrowed by a specific member"""
    member_id = input("\nEnter member ID: ").strip()

    if member_id not in library.members:
        print("✗ Member not found!")
        return

    member = library.members[member_id]
    borrowed_books = library.get_member_borrowed_books(member_id)

    print(f"\n{'='*80}")
    print(f"BOOKS BORROWED BY: {member.name}")
    print(f"{'='*80}")

    if not borrowed_books:
        print("No books currently borrowed!")
    else:
        for book in borrowed_books:
            print(f"  {book}")
        print(f"\nTotal: {len(borrowed_books)}/{member.max_books} books")

    print("=" * 80)


def view_overdue_books(library):
    """View all overdue books"""
    overdue = library.get_overdue_books()

    print(f"\n{'='*80}\nOVERDUE BOOKS ({len(overdue)} total)\n{'='*80}")

    if not overdue:
        print("No overdue books!")
    else:
        for book in overdue:
            borrower = library.members.get(book.borrowed_by)
            borrower_name = borrower.name if borrower else "Unknown"
            print(f"  {book}")
            print(f"    Borrowed by: {borrower_name} ({book.borrowed_by})")

    print("=" * 80)


def main():
    """Main program function"""
    print("=" * 60)
    print("   LIBRARY MANAGEMENT SYSTEM - Week 6")
    print("=" * 60)
    print("Advanced OOP with Inheritance and Polymorphism!")
    print()

    # Load existing library or create new one
    library = Library.load_from_file()

    if library:
        print(f"✓ Loaded existing library: {library.name}")
        print(f"  Books: {len(library.books)}, Members: {len(library.members)}")
    else:
        name = input("Enter library name: ").strip() or "My Library"
        library = Library(name)
        print(f"✓ Created new library: {library.name}")

    # Main program loop
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-12): ").strip()

        if choice == '1':
            add_book(library)

        elif choice == '2':
            add_member(library)

        elif choice == '3':
            # Borrow book
            member_id = input("\nEnter member ID: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            success, message = library.borrow_book(member_id, isbn)
            print(f"{'✓' if success else '✗'} {message}")

        elif choice == '4':
            # Return book
            member_id = input("\nEnter member ID: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            success, message = library.return_book(member_id, isbn)
            print(f"{'✓' if success else '✗'} {message}")

        elif choice == '5':
            # Search books
            keyword = input("\nEnter search keyword: ").strip()
            results = library.search_books(keyword)
            if results:
                print(f"\nFound {len(results)} book(s):")
                for book in results:
                    print(f"  {book}")
            else:
                print("No books found!")

        elif choice == '6':
            # View all books
            if not library.books:
                print("\nNo books in the library!")
            else:
                print(f"\n{'='*80}\nALL BOOKS ({len(library.books)} total)\n{'='*80}")
                for book in library.books.values():
                    print(f"  {book}")
                print("=" * 80)

        elif choice == '7':
            # View all members
            if not library.members:
                print("\nNo members in the library!")
            else:
                print(f"\n{'='*80}\nALL MEMBERS ({len(library.members)} total)\n{'='*80}")
                for member in library.members.values():
                    print(f"  {member}")
                print("=" * 80)

        elif choice == '8':
            view_books_by_type(library)

        elif choice == '9':
            view_members_by_type(library)

        elif choice == '10':
            view_member_books(library)

        elif choice == '11':
            view_overdue_books(library)

        elif choice == '12':
            # Save and exit
            print("\nSaving library data...")
            try:
                library.save_to_file()
                print("✓ Library data saved successfully!")
                print("\nThank you for using the Library Management System!")
                print("Goodbye!")
                break
            except Exception as e:
                print(f"✗ Error saving data: {e}")
                confirm = input("Exit anyway? (y/n): ").lower()
                if confirm == 'y':
                    break

        else:
            print("\n✗ Invalid choice! Please enter a number between 1 and 12.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n\nFatal error: {str(e)}")
        print("Program terminated unexpectedly.")
