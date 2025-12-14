"""
Week 7 Project: Library Management System (Version 3)
Concepts: Lambda, map/filter/reduce, Generators, Decorators
NEW Features:
- Analytics module with lambda, map, filter, reduce
- Custom decorators for logging and validation
- Report generation with generators
- Advanced data processing and statistics
"""

from books import Book, EBook, PhysicalBook
from members import Member, StudentMember, TeacherMember
from library import Library
from analytics import (get_popular_authors, filter_books_by_year, get_available_ebooks,
                       calculate_total_file_size, get_borrowing_statistics,
                       calculate_library_value, group_books_by_type)
from reports import (generate_book_catalog, generate_overdue_report,
                     generate_member_activity_report, print_full_report,
                     generate_paginated_books)
from decorators import log_transaction, timer


def show_menu():
    """Display main menu"""
    print("\n" + "=" * 60)
    print("LIBRARY MENU:")
    print("1. Add Book (Physical/EBook)")
    print("2. Add Member (Regular/Student/Teacher)")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Books")
    print("6. View All Books (Paginated)")
    print("7. View All Members")
    print("8. Analytics - Popular Authors")
    print("9. Analytics - Borrowing Statistics")
    print("10. Analytics - Library Value")
    print("11. Analytics - Books by Year Range")
    print("12. Reports - Overdue Books")
    print("13. Reports - Member Activity")
    print("14. Reports - Full Report")
    print("15. Save & Exit")
    print("=" * 60)


@timer
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
            shelf = input("Enter shelf location: ").strip()
            condition = input("Enter condition (New/Good/Fair/Poor): ").strip() or "Good"
            book = PhysicalBook(isbn, title, author, year, shelf, condition)
        elif book_type == '2':
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
    """Add a new member"""
    print("\n--- Add New Member ---")
    print("1. Regular Member")
    print("2. Student Member")
    print("3. Teacher Member")

    member_type = input("Enter choice (1-3): ").strip()
    member_id = input("Enter member ID: ").strip()
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()

    if member_type == '1':
        member = Member(member_id, name, email)
    elif member_type == '2':
        student_id = input("Enter student ID: ").strip()
        major = input("Enter major: ").strip()
        member = StudentMember(member_id, name, email, student_id, major)
    elif member_type == '3':
        faculty_id = input("Enter faculty ID: ").strip()
        department = input("Enter department: ").strip()
        member = TeacherMember(member_id, name, email, faculty_id, department)
    else:
        print("✗ Invalid member type!")
        return

    success, message = library.add_member(member)
    print(f"{'✓' if success else '✗'} {message}")


def show_popular_authors(library):
    """Display popular authors using analytics"""
    print("\n--- Popular Authors ---")

    top_n = input("How many top authors to show? (default: 5): ").strip()
    top_n = int(top_n) if top_n.isdigit() else 5

    authors = get_popular_authors(library, top_n)

    if authors:
        print(f"\nTop {len(authors)} Authors:")
        for rank, (author, count) in enumerate(authors, start=1):
            print(f"{rank}. {author}: {count} book(s)")
    else:
        print("No books in library!")


def show_borrowing_stats(library):
    """Display borrowing statistics using analytics"""
    print("\n--- Borrowing Statistics ---")

    stats = get_borrowing_statistics(library)

    print(f"Total Members: {stats['total_members']}")
    print(f"Members with Books: {stats['members_with_books']}")
    print(f"Total Books Borrowed: {stats['total_books_borrowed']}")
    print(f"Average per Member: {stats['average_per_member']:.2f}")

    # Group books by type
    grouped = group_books_by_type(library)
    print("\nBooks by Type:")
    for book_type, books in grouped.items():
        available = len(list(filter(lambda b: b.is_available, books)))
        print(f"  {book_type}: {len(books)} total ({available} available)")


def show_library_value(library):
    """Display estimated library value"""
    print("\n--- Library Value Estimate ---")

    value = calculate_library_value(library)
    print(f"Estimated Total Value: ${value:,.2f}")

    # Show breakdown
    grouped = group_books_by_type(library)
    print("\nBreakdown:")
    for book_type, books in grouped.items():
        if book_type == "PhysicalBook":
            type_value = len(books) * 25
        elif book_type == "EBook":
            type_value = len(books) * 15
        else:
            type_value = 0
        print(f"  {book_type}: {len(books)} books × ${25 if book_type == 'PhysicalBook' else 15} = ${type_value:,.2f}")

    # EBook storage
    total_size = calculate_total_file_size(library)
    print(f"\nTotal EBook Storage: {total_size:.2f} MB")


def filter_by_year_range(library):
    """Filter and display books by year range"""
    print("\n--- Filter Books by Year ---")

    try:
        start_year = int(input("Enter start year: ").strip())
        end_year = int(input("Enter end year: ").strip())

        books = filter_books_by_year(library, start_year, end_year)

        print(f"\nFound {len(books)} book(s) published between {start_year} and {end_year}:")
        for book in books:
            print(f"  [{book.year}] {book.title} by {book.author}")

    except ValueError:
        print("✗ Invalid year entered!")


def show_overdue_report(library):
    """Display overdue books report using generator"""
    print("\n" + "=" * 80)
    print("OVERDUE BOOKS REPORT")
    print("=" * 80)

    overdue_count = 0
    for overdue in generate_overdue_report(library):
        overdue_count += 1
        print(f"\n{overdue_count}. {overdue['title']}")
        print(f"   Borrower: {overdue['borrower_name']} ({overdue['borrower_email']})")
        print(f"   Due Date: {overdue['due_date']}")
        print(f"   Days Overdue: {overdue['days_overdue']}")

    if overdue_count == 0:
        print("\n✓ No overdue books!")

    print("=" * 80)


def show_member_activity(library):
    """Display member activity report using generator"""
    print("\n" + "=" * 80)
    print("MEMBER ACTIVITY REPORT")
    print("=" * 80)

    for activity in generate_member_activity_report(library):
        print(f"\n{activity['name']} ({activity['type']}) - ID: {activity['member_id']}")
        print(f"  Books Borrowed: {activity['books_borrowed']}/{activity['max_books']} ({activity['utilization']})")

        if activity['borrowed_titles']:
            print(f"  Currently Reading:")
            for title in activity['borrowed_titles']:
                print(f"    - {title}")

    print("=" * 80)


def view_books_paginated(library):
    """View books with pagination using generator"""
    if not library.books:
        print("\nNo books in library!")
        return

    page_size = 10

    for page_data in generate_paginated_books(library, page_size):
        print(f"\n{'='*80}")
        print(f"PAGE {page_data['page']} of {page_data['total_pages']} - Showing {page_data['showing']}")
        print("=" * 80)

        for book in page_data['books']:
            print(f"  {book}")

        if page_data['page'] < page_data['total_pages']:
            choice = input("\nPress Enter for next page, 'q' to quit: ").strip().lower()
            if choice == 'q':
                break
        else:
            print("\n[End of catalog]")


def main():
    """Main program function"""
    print("=" * 60)
    print("   LIBRARY MANAGEMENT SYSTEM - Week 7")
    print("=" * 60)
    print("Advanced Features with Functional Programming!")
    print()

    # Load library
    library = Library.load_from_file()

    if library:
        print(f"✓ Loaded library: {library.name}")
        print(f"  Books: {len(library.books)}, Members: {len(library.members)}")
    else:
        name = input("Enter library name: ").strip() or "My Library"
        library = Library(name)
        print(f"✓ Created new library: {library.name}")

    # Main loop
    while True:
        show_menu()
        choice = input("\nEnter choice (1-15): ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            add_member(library)
        elif choice == '3':
            member_id = input("\nEnter member ID: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            success, message = library.borrow_book(member_id, isbn)
            print(f"{'✓' if success else '✗'} {message}")
        elif choice == '4':
            member_id = input("\nEnter member ID: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            success, message = library.return_book(member_id, isbn)
            print(f"{'✓' if success else '✗'} {message}")
        elif choice == '5':
            keyword = input("\nEnter search keyword: ").strip()
            results = library.search_books(keyword)
            if results:
                print(f"\nFound {len(results)} book(s):")
                for book in results:
                    print(f"  {book}")
            else:
                print("No books found!")
        elif choice == '6':
            view_books_paginated(library)
        elif choice == '7':
            if library.members:
                print(f"\n{'='*80}\nALL MEMBERS\n{'='*80}")
                for member in library.members.values():
                    print(f"  {member}")
                print("=" * 80)
            else:
                print("\nNo members!")
        elif choice == '8':
            show_popular_authors(library)
        elif choice == '9':
            show_borrowing_stats(library)
        elif choice == '10':
            show_library_value(library)
        elif choice == '11':
            filter_by_year_range(library)
        elif choice == '12':
            show_overdue_report(library)
        elif choice == '13':
            show_member_activity(library)
        elif choice == '14':
            print_full_report(library)
        elif choice == '15':
            print("\nSaving library data...")
            try:
                library.save_to_file()
                print("✓ Data saved!")
                print("\nThank you for using the Library Management System!")
                print("Goodbye!")
                break
            except Exception as e:
                print(f"✗ Error: {e}")
                if input("Exit anyway? (y/n): ").lower() == 'y':
                    break
        else:
            print("\n✗ Invalid choice!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")
    except Exception as e:
        print(f"\n\nFatal error: {str(e)}")
