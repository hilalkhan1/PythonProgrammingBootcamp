"""
Week 6 Project: Book Class Hierarchy
Demonstrates: Inheritance, Polymorphism
Classes: Book (base), EBook, PhysicalBook
"""

from datetime import datetime, timedelta


class Book:
    """Base class representing a book in the library"""

    def __init__(self, isbn, title, author, year):
        """
        Initialize a book

        Args:
            isbn: International Standard Book Number
            title: Book title
            author: Author name
            year: Publication year
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
        self.borrowed_by = None
        self.due_date = None
        self._type = "Book"  # Protected attribute

    def borrow(self, member_id, days=14):
        """
        Mark book as borrowed

        Args:
            member_id: ID of the member borrowing the book
            days: Number of days for the loan period

        Returns:
            bool: True if successful, False if already borrowed
        """
        if not self.is_available:
            return False

        self.is_available = False
        self.borrowed_by = member_id
        self.due_date = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
        return True

    def return_book(self):
        """
        Mark book as returned

        Returns:
            bool: True if successful, False if not borrowed
        """
        if self.is_available:
            return False

        self.is_available = True
        self.borrowed_by = None
        self.due_date = None
        return True

    def get_info(self):
        """Get book information - polymorphic method"""
        status = "Available" if self.is_available else f"Borrowed (Due: {self.due_date})"
        return f"[{self.isbn}] {self.title} by {self.author} ({self.year}) - {status}"

    def __str__(self):
        """String representation of the book"""
        return f"[{self._type}] {self.get_info()}"

    def to_dict(self):
        """Convert book to dictionary for JSON serialization"""
        return {
            "type": self._type,
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "is_available": self.is_available,
            "borrowed_by": self.borrowed_by,
            "due_date": self.due_date
        }


class EBook(Book):
    """Electronic book with file size and format"""

    def __init__(self, isbn, title, author, year, file_size_mb, file_format):
        """
        Initialize an e-book

        Args:
            isbn: International Standard Book Number
            title: Book title
            author: Author name
            year: Publication year
            file_size_mb: File size in megabytes
            file_format: File format (PDF, EPUB, MOBI, etc.)
        """
        super().__init__(isbn, title, author, year)
        self.file_size_mb = file_size_mb
        self.file_format = file_format.upper()
        self._type = "EBook"

    def borrow(self, member_id, days=30):
        """
        EBooks can be borrowed for longer periods (30 days default)
        Overrides parent method
        """
        return super().borrow(member_id, days)

    def get_info(self):
        """Get ebook-specific information - polymorphic override"""
        base_info = super().get_info()
        return f"{base_info} | {self.file_format} ({self.file_size_mb}MB)"

    def download_link(self):
        """Generate download link (simulated)"""
        return f"https://library.example.com/download/{self.isbn}.{self.file_format.lower()}"

    def to_dict(self):
        """Convert ebook to dictionary"""
        data = super().to_dict()
        data.update({
            "file_size_mb": self.file_size_mb,
            "file_format": self.file_format
        })
        return data


class PhysicalBook(Book):
    """Physical book with shelf location and condition"""

    def __init__(self, isbn, title, author, year, shelf_location, condition="Good"):
        """
        Initialize a physical book

        Args:
            isbn: International Standard Book Number
            title: Book title
            author: Author name
            year: Publication year
            shelf_location: Physical location in library (e.g., "A3-15")
            condition: Book condition (New, Good, Fair, Poor)
        """
        super().__init__(isbn, title, author, year)
        self.shelf_location = shelf_location
        self.condition = condition
        self._type = "PhysicalBook"

    def borrow(self, member_id, days=14):
        """
        Physical books have standard 14-day borrowing period
        Overrides parent method
        """
        return super().borrow(member_id, days)

    def get_info(self):
        """Get physical book-specific information - polymorphic override"""
        base_info = super().get_info()
        return f"{base_info} | Shelf: {self.shelf_location} | Condition: {self.condition}"

    def update_condition(self, new_condition):
        """
        Update book condition

        Args:
            new_condition: New condition (New, Good, Fair, Poor)

        Returns:
            bool: True if successful
        """
        valid_conditions = ["New", "Good", "Fair", "Poor"]
        if new_condition in valid_conditions:
            self.condition = new_condition
            return True
        return False

    def to_dict(self):
        """Convert physical book to dictionary"""
        data = super().to_dict()
        data.update({
            "shelf_location": self.shelf_location,
            "condition": self.condition
        })
        return data


def create_book_from_dict(data):
    """
    Factory function to create appropriate book type from dictionary

    Args:
        data: Dictionary containing book data

    Returns:
        Book object (Book, EBook, or PhysicalBook)
    """
    book_type = data.get("type", "Book")

    if book_type == "EBook":
        book = EBook(
            data["isbn"],
            data["title"],
            data["author"],
            data["year"],
            data.get("file_size_mb", 0),
            data.get("file_format", "PDF")
        )
    elif book_type == "PhysicalBook":
        book = PhysicalBook(
            data["isbn"],
            data["title"],
            data["author"],
            data["year"],
            data.get("shelf_location", "Unknown"),
            data.get("condition", "Good")
        )
    else:
        book = Book(data["isbn"], data["title"], data["author"], data["year"])

    # Restore borrowing state
    book.is_available = data.get("is_available", True)
    book.borrowed_by = data.get("borrowed_by")
    book.due_date = data.get("due_date")

    return book
