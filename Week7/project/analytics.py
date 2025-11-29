"""
Week 7 Project: Library Analytics Module
Demonstrates: Lambda functions, map, filter, reduce
Functions for analyzing library data
"""

from functools import reduce
from datetime import datetime


def get_popular_authors(library, top_n=5):
    """
    Get most popular authors by number of books

    Uses map, filter, reduce, and lambda

    Args:
        library: Library object
        top_n: Number of top authors to return

    Returns:
        list: List of tuples (author, count)
    """
    # Get all authors
    authors = list(map(lambda book: book.author, library.books.values()))

    # Count occurrences
    author_counts = {}
    for author in authors:
        author_counts[author] = author_counts.get(author, 0) + 1

    # Sort by count using lambda
    sorted_authors = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_authors[:top_n]


def filter_books_by_year(library, start_year, end_year):
    """
    Filter books published within a year range

    Uses filter and lambda

    Args:
        library: Library object
        start_year: Start year (inclusive)
        end_year: End year (inclusive)

    Returns:
        list: Filtered list of books
    """
    return list(filter(
        lambda book: start_year <= book.year <= end_year,
        library.books.values()
    ))


def get_available_ebooks(library):
    """
    Get all available ebooks

    Uses filter and lambda

    Args:
        library: Library object

    Returns:
        list: List of available ebooks
    """
    return list(filter(
        lambda book: book._type == "EBook" and book.is_available,
        library.books.values()
    ))


def calculate_total_file_size(library):
    """
    Calculate total file size of all ebooks

    Uses filter, map, and reduce

    Args:
        library: Library object

    Returns:
        float: Total file size in MB
    """
    # Get all ebooks
    ebooks = filter(lambda book: book._type == "EBook", library.books.values())

    # Extract file sizes
    file_sizes = map(lambda ebook: ebook.file_size_mb, ebooks)

    # Sum using reduce
    total = reduce(lambda acc, size: acc + size, file_sizes, 0)

    return total


def get_members_with_max_books(library):
    """
    Get members who have borrowed the maximum number of books they can

    Uses filter and lambda

    Args:
        library: Library object

    Returns:
        list: List of members at their borrowing limit
    """
    return list(filter(
        lambda member: len(member._borrowed_books) >= member.max_books,
        library.members.values()
    ))


def get_borrowing_statistics(library):
    """
    Calculate borrowing statistics across all members

    Uses map, filter, reduce

    Args:
        library: Library object

    Returns:
        dict: Statistics about borrowing
    """
    # Get number of books borrowed by each member
    borrowed_counts = list(map(
        lambda member: len(member._borrowed_books),
        library.members.values()
    ))

    if not borrowed_counts:
        return {
            "total_members": 0,
            "members_with_books": 0,
            "total_books_borrowed": 0,
            "average_per_member": 0
        }

    # Members who have borrowed at least one book
    members_with_books = len(list(filter(lambda count: count > 0, borrowed_counts)))

    # Total books borrowed
    total_borrowed = reduce(lambda acc, count: acc + count, borrowed_counts, 0)

    # Average books per member
    average = total_borrowed / len(borrowed_counts) if borrowed_counts else 0

    return {
        "total_members": len(library.members),
        "members_with_books": members_with_books,
        "total_books_borrowed": total_borrowed,
        "average_per_member": round(average, 2)
    }


def sort_books_by_title(books):
    """
    Sort books alphabetically by title

    Uses sorted and lambda

    Args:
        books: List of book objects

    Returns:
        list: Sorted list of books
    """
    return sorted(books, key=lambda book: book.title.lower())


def sort_books_by_availability(books):
    """
    Sort books by availability (available first)

    Uses sorted and lambda

    Args:
        books: List of book objects

    Returns:
        list: Sorted list of books
    """
    return sorted(books, key=lambda book: not book.is_available)


def group_books_by_type(library):
    """
    Group books by their type

    Uses filter and lambda

    Args:
        library: Library object

    Returns:
        dict: Dictionary with book types as keys and lists of books as values
    """
    types = ["Book", "EBook", "PhysicalBook"]

    grouped = {}
    for book_type in types:
        grouped[book_type] = list(filter(
            lambda book: book._type == book_type,
            library.books.values()
        ))

    return grouped


def find_overdue_by_member_type(library, member_type):
    """
    Find overdue books borrowed by a specific member type

    Uses filter, map, and lambda

    Args:
        library: Library object
        member_type: Type of member ("Student", "Teacher", etc.)

    Returns:
        list: List of overdue books borrowed by specified member type
    """
    today = datetime.now().strftime("%Y-%m-%d")

    # Get members of specified type
    target_members = filter(
        lambda member: member._member_type == member_type,
        library.members.values()
    )

    # Get their member IDs
    member_ids = set(map(lambda member: member.member_id, target_members))

    # Filter overdue books borrowed by these members
    overdue = list(filter(
        lambda book: (not book.is_available and
                     book.due_date and
                     book.due_date < today and
                     book.borrowed_by in member_ids),
        library.books.values()
    ))

    return overdue


def calculate_library_value(library, price_per_physical=25, price_per_ebook=15):
    """
    Calculate estimated total value of library collection

    Uses map, filter, reduce, and lambda

    Args:
        library: Library object
        price_per_physical: Estimated price per physical book
        price_per_ebook: Estimated price per ebook

    Returns:
        float: Total estimated value
    """
    # Physical books value
    physical_books = filter(
        lambda book: book._type == "PhysicalBook",
        library.books.values()
    )
    physical_value = reduce(
        lambda acc, _: acc + price_per_physical,
        physical_books,
        0
    )

    # Ebooks value
    ebooks = filter(
        lambda book: book._type == "EBook",
        library.books.values()
    )
    ebook_value = reduce(
        lambda acc, _: acc + price_per_ebook,
        ebooks,
        0
    )

    return physical_value + ebook_value
