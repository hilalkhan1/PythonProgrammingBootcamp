"""
Week 7 Project: Report Generation Module
Demonstrates: Generators, yield statement
Functions for generating reports efficiently
"""

from datetime import datetime


def generate_book_catalog(library):
    """
    Generator that yields books one at a time

    Memory-efficient for large catalogs

    Args:
        library: Library object

    Yields:
        tuple: (index, book) for each book
    """
    for index, (isbn, book) in enumerate(library.books.items(), start=1):
        yield index, book


def generate_member_list(library):
    """
    Generator that yields members one at a time

    Args:
        library: Library object

    Yields:
        tuple: (index, member) for each member
    """
    for index, (member_id, member) in enumerate(library.members.items(), start=1):
        yield index, member


def generate_borrowed_books_report(library):
    """
    Generator that yields borrowed books with borrower information

    Args:
        library: Library object

    Yields:
        dict: Information about each borrowed book
    """
    for book in library.books.values():
        if not book.is_available:
            borrower = library.members.get(book.borrowed_by)

            yield {
                "isbn": book.isbn,
                "title": book.title,
                "author": book.author,
                "type": book._type,
                "borrowed_by_id": book.borrowed_by,
                "borrowed_by_name": borrower.name if borrower else "Unknown",
                "borrower_type": borrower._member_type if borrower else "Unknown",
                "due_date": book.due_date,
                "is_overdue": book.due_date < datetime.now().strftime("%Y-%m-%d") if book.due_date else False
            }


def generate_overdue_report(library):
    """
    Generator that yields overdue books with details

    Args:
        library: Library object

    Yields:
        dict: Information about each overdue book
    """
    today = datetime.now().strftime("%Y-%m-%d")

    for book in library.books.values():
        if not book.is_available and book.due_date and book.due_date < today:
            borrower = library.members.get(book.borrowed_by)

            # Calculate days overdue
            from datetime import datetime as dt
            due_date_obj = dt.strptime(book.due_date, "%Y-%m-%d")
            today_obj = dt.now()
            days_overdue = (today_obj - due_date_obj).days

            yield {
                "isbn": book.isbn,
                "title": book.title,
                "borrower_name": borrower.name if borrower else "Unknown",
                "borrower_email": borrower.email if borrower else "Unknown",
                "due_date": book.due_date,
                "days_overdue": days_overdue
            }


def generate_member_activity_report(library):
    """
    Generator that yields member activity information

    Args:
        library: Library object

    Yields:
        dict: Activity information for each member
    """
    for member in library.members.values():
        # Get books currently borrowed
        borrowed_books = []
        for isbn in member._borrowed_books:
            if isbn in library.books:
                borrowed_books.append(library.books[isbn].title)

        yield {
            "member_id": member.member_id,
            "name": member.name,
            "email": member.email,
            "type": member._member_type,
            "books_borrowed": len(member._borrowed_books),
            "max_books": member.max_books,
            "utilization": f"{(len(member._borrowed_books) / member.max_books * 100):.1f}%",
            "borrowed_titles": borrowed_books
        }


def generate_statistics_by_type(library):
    """
    Generator that yields statistics for each book/member type

    Args:
        library: Library object

    Yields:
        dict: Statistics for each type
    """
    # Book type statistics
    book_types = ["Book", "EBook", "PhysicalBook"]

    for book_type in book_types:
        books_of_type = [b for b in library.books.values() if b._type == book_type]
        available = len([b for b in books_of_type if b.is_available])

        yield {
            "category": "Book Type",
            "type": book_type,
            "total": len(books_of_type),
            "available": available,
            "borrowed": len(books_of_type) - available
        }

    # Member type statistics
    member_types = ["Member", "Student", "Teacher"]

    for member_type in member_types:
        members_of_type = [m for m in library.members.values() if m._member_type == member_type]
        active = len([m for m in members_of_type if len(m._borrowed_books) > 0])

        yield {
            "category": "Member Type",
            "type": member_type,
            "total": len(members_of_type),
            "active": active,
            "inactive": len(members_of_type) - active
        }


def generate_paginated_books(library, page_size=10):
    """
    Generator that yields books in pages

    Args:
        library: Library object
        page_size: Number of books per page

    Yields:
        list: Page of books
    """
    books = list(library.books.values())
    total_books = len(books)

    for i in range(0, total_books, page_size):
        page_number = (i // page_size) + 1
        page = books[i:i + page_size]

        yield {
            "page": page_number,
            "total_pages": (total_books + page_size - 1) // page_size,
            "books": page,
            "showing": f"{i + 1}-{min(i + page_size, total_books)} of {total_books}"
        }


def batch_process_books(library, batch_size=50):
    """
    Generator for processing books in batches

    Useful for large datasets

    Args:
        library: Library object
        batch_size: Number of books per batch

    Yields:
        list: Batch of books
    """
    books = list(library.books.values())
    total = len(books)

    for i in range(0, total, batch_size):
        batch = books[i:i + batch_size]
        yield batch


def infinite_id_generator(prefix="ID", start=1000):
    """
    Generator that yields infinite sequence of unique IDs

    Args:
        prefix: ID prefix
        start: Starting number

    Yields:
        str: Unique ID
    """
    current = start
    while True:
        yield f"{prefix}{current:06d}"
        current += 1


def print_full_report(library):
    """
    Print a comprehensive library report using generators

    Args:
        library: Library object
    """
    print("\n" + "=" * 80)
    print(" " * 25 + "LIBRARY COMPREHENSIVE REPORT")
    print("=" * 80)

    # Summary
    print(f"\nLibrary: {library.name}")
    print(f"Total Books: {len(library.books)}")
    print(f"Total Members: {len(library.members)}")

    # Books by type
    print("\n" + "-" * 80)
    print("STATISTICS BY TYPE:")
    print("-" * 80)

    for stat in generate_statistics_by_type(library):
        if stat["category"] == "Book Type":
            print(f"\n{stat['type']}:")
            print(f"  Total: {stat['total']}, Available: {stat['available']}, Borrowed: {stat['borrowed']}")

    # Member activity
    print("\n" + "-" * 80)
    print("MEMBER ACTIVITY:")
    print("-" * 80)

    for activity in generate_member_activity_report(library):
        if activity["books_borrowed"] > 0:
            print(f"\n{activity['name']} ({activity['type']}):")
            print(f"  Books: {activity['books_borrowed']}/{activity['max_books']} ({activity['utilization']})")

    # Overdue books
    overdue_list = list(generate_overdue_report(library))
    if overdue_list:
        print("\n" + "-" * 80)
        print(f"OVERDUE BOOKS ({len(overdue_list)} total):")
        print("-" * 80)

        for overdue in overdue_list:
            print(f"\n{overdue['title']}")
            print(f"  Borrower: {overdue['borrower_name']}")
            print(f"  Days Overdue: {overdue['days_overdue']}")

    print("\n" + "=" * 80)
