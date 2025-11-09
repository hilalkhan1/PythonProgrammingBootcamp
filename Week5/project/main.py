"""
Week 5 Project: Library Management System (Version 1)
Concepts: Classes, objects, methods, encapsulation
NEW: Complete OOP design with Book, Member, and Library classes
"""

import os
from models import Book, Member, Library


def show_menu():
    """Display main menu"""
    print("\n" + "=" * 60)
    print("LIBRARY MENU:")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Books")
    print("6. View All Books")
    print("7. View All Members")
    print("8. View Available Books")
    print("9. View Borrowed Books")
    print("10. Save & Exit")
    print("=" * 60)


def add_book(library):
    """Add a new book to the library"""
    print("\n--- Add New Book ---")
    isbn = input("Enter ISBN: ").strip()
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()

    year_str = input("Enter publication year: ").strip()

    try:
        year = int(year_str)
        book = Book(isbn, title, author, year)

        if library.add_book(book):
            print(f"✓ Book '{title}' added successfully!")
        else:
            print(f"✗ Book with ISBN {isbn} already exists!")

    except ValueError:
        print("✗ Invalid year entered!")


def add_member(library):
    """Add a new member to the library"""
    print("\n--- Add New Member ---")
    member_id = input("Enter member ID: ").strip()
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()

    member = Member(member_id, name, email)

    if library.add_member(member):
        print(f"✓ Member '{name}' added successfully!")
    else:
        print(f"✗ Member with ID {member_id} already exists!")


def borrow_book(library):
    """Process a book borrowing"""
    print("\n--- Borrow Book ---")
    member_id = input("Enter member ID: ").strip()
    isbn = input("Enter book ISBN: ").strip()

    success, message = library.borrow_book(member_id, isbn)

    if success:
        print(f"✓ {message}")
    else:
        print(f"✗ {message}")


def return_book(library):
    """Process a book return"""
    print("\n--- Return Book ---")
    member_id = input("Enter member ID: ").strip()
    isbn = input("Enter book ISBN: ").strip()

    success, message = library.return_book(member_id, isbn)

    if success:
        print(f"✓ {message}")
    else:
        print(f"✗ {message}")


def search_books(library):
    """Search for books"""
    keyword = input("\nEnter search keyword (title or author): ").strip()

    results = library.search_books(keyword)

    if results:
        print(f"\nFound {len(results)} book(s):")
        for book in results:
            print(f"  {book}")
    else:
        print("No books found matching your search.")


def view_all_books(library):
    """Display all books"""
    if not library.books:
        print("\nNo books in the library!")
        return

    print("\n" + "=" * 80)
    print(f"ALL BOOKS ({len(library.books)} total)")
    print("=" * 80)

    for book in library.books.values():
        print(f"  {book}")

    print("=" * 80)


def view_all_members(library):
    """Display all members"""
    if not library.members:
        print("\nNo members in the library!")
        return

    print("\n" + "=" * 80)
    print(f"ALL MEMBERS ({len(library.members)} total)")
    print("=" * 80)

    for member in library.members.values():
        print(f"  {member}")

    print("=" * 80)


def view_available_books(library):
    """Display available books"""
    available = library.get_available_books()

    if not available:
        print("\nNo books available for borrowing!")
        return

    print("\n" + "=" * 80)
    print(f"AVAILABLE BOOKS ({len(available)} books)")
    print("=" * 80)

    for book in available:
        print(f"  {book}")

    print("=" * 80)


def view_borrowed_books(library):
    """Display borrowed books"""
    borrowed = library.get_borrowed_books()

    if not borrowed:
        print("\nNo books currently borrowed!")
        return

    print("\n" + "=" * 80)
    print(f"BORROWED BOOKS ({len(borrowed)} books)")
    print("=" * 80)

    for book in borrowed:
        print(f"  {book}")

    print("=" * 80)


def main():
    """Main program function"""
    print("=" * 60)
    print("   LIBRARY MANAGEMENT SYSTEM - Week 5")
    print("=" * 60)
    print("Object-Oriented Programming with Classes!")
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
        choice = input("\nEnter your choice (1-10): ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            add_member(library)
        elif choice == '3':
            borrow_book(library)
        elif choice == '4':
            return_book(library)
        elif choice == '5':
            search_books(library)
        elif choice == '6':
            view_all_books(library)
        elif choice == '7':
            view_all_members(library)
        elif choice == '8':
            view_available_books(library)
        elif choice == '9':
            view_borrowed_books(library)
        elif choice == '10':
            # Save and exit
            print("\nSaving library data...")
            try:
                os.makedirs("data", exist_ok=True)
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
            print("\n✗ Invalid choice! Please enter a number between 1 and 10.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n\nFatal error: {str(e)}")
        print("Program terminated unexpectedly.")
