"""
Week 5 Project: Library Management System - Models
Concepts: Classes, objects, methods, encapsulation
Classes: Book, Member, Library
"""

import json
from datetime import datetime, timedelta


class Book:
    """Represents a book in the library"""

    def __init__(self, isbn, title, author, year):
        """
        Initialize a new book

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

    def __str__(self):
        """String representation of the book"""
        status = "Available" if self.is_available else f"Borrowed (Due: {self.due_date})"
        return f"[{self.isbn}] {self.title} by {self.author} ({self.year}) - {status}"

    def to_dict(self):
        """Convert book to dictionary for JSON serialization"""
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "is_available": self.is_available,
            "borrowed_by": self.borrowed_by,
            "due_date": self.due_date
        }

    @staticmethod
    def from_dict(data):
        """Create a book object from dictionary"""
        book = Book(data["isbn"], data["title"], data["author"], data["year"])
        book.is_available = data.get("is_available", True)
        book.borrowed_by = data.get("borrowed_by")
        book.due_date = data.get("due_date")
        return book


class Member:
    """Represents a library member"""

    def __init__(self, member_id, name, email):
        """
        Initialize a new member

        Args:
            member_id: Unique member ID
            name: Member's full name
            email: Member's email address
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []  # List of ISBNs
        self.join_date = datetime.now().strftime("%Y-%m-%d")

    def borrow_book(self, isbn):
        """
        Add a book to member's borrowed list

        Args:
            isbn: ISBN of the borrowed book

        Returns:
            bool: True if successful, False if already borrowed
        """
        if isbn in self.borrowed_books:
            return False

        self.borrowed_books.append(isbn)
        return True

    def return_book(self, isbn):
        """
        Remove a book from member's borrowed list

        Args:
            isbn: ISBN of the book to return

        Returns:
            bool: True if successful, False if not in borrowed list
        """
        if isbn not in self.borrowed_books:
            return False

        self.borrowed_books.remove(isbn)
        return True

    def __str__(self):
        """String representation of the member"""
        return f"[{self.member_id}] {self.name} ({self.email}) - {len(self.borrowed_books)} books borrowed"

    def to_dict(self):
        """Convert member to dictionary for JSON serialization"""
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "borrowed_books": self.borrowed_books,
            "join_date": self.join_date
        }

    @staticmethod
    def from_dict(data):
        """Create a member object from dictionary"""
        member = Member(data["member_id"], data["name"], data["email"])
        member.borrowed_books = data.get("borrowed_books", [])
        member.join_date = data.get("join_date", datetime.now().strftime("%Y-%m-%d"))
        return member


class Library:
    """Represents the library system"""

    def __init__(self, name):
        """
        Initialize a new library

        Args:
            name: Name of the library
        """
        self.name = name
        self.books = {}  # ISBN -> Book object
        self.members = {}  # member_id -> Member object

    def add_book(self, book):
        """
        Add a book to the library

        Args:
            book: Book object to add

        Returns:
            bool: True if successful, False if ISBN already exists
        """
        if book.isbn in self.books:
            return False

        self.books[book.isbn] = book
        return True

    def remove_book(self, isbn):
        """
        Remove a book from the library

        Args:
            isbn: ISBN of the book to remove

        Returns:
            bool: True if successful, False if not found or borrowed
        """
        if isbn not in self.books:
            return False

        if not self.books[isbn].is_available:
            return False  # Can't remove borrowed books

        del self.books[isbn]
        return True

    def add_member(self, member):
        """
        Add a member to the library

        Args:
            member: Member object to add

        Returns:
            bool: True if successful, False if ID already exists
        """
        if member.member_id in self.members:
            return False

        self.members[member.member_id] = member
        return True

    def remove_member(self, member_id):
        """
        Remove a member from the library

        Args:
            member_id: ID of the member to remove

        Returns:
            bool: True if successful, False if not found or has borrowed books
        """
        if member_id not in self.members:
            return False

        if self.members[member_id].borrowed_books:
            return False  # Can't remove members with borrowed books

        del self.members[member_id]
        return True

    def borrow_book(self, member_id, isbn):
        """
        Process a book borrowing transaction

        Args:
            member_id: ID of the member borrowing
            isbn: ISBN of the book to borrow

        Returns:
            tuple: (success: bool, message: str)
        """
        if member_id not in self.members:
            return False, "Member not found"

        if isbn not in self.books:
            return False, "Book not found"

        book = self.books[isbn]
        member = self.members[member_id]

        if not book.is_available:
            return False, "Book is already borrowed"

        if len(member.borrowed_books) >= 5:
            return False, "Member has reached maximum borrowing limit (5 books)"

        # Process the borrowing
        if book.borrow(member_id) and member.borrow_book(isbn):
            return True, f"Book borrowed successfully. Due date: {book.due_date}"

        return False, "Failed to process borrowing"

    def return_book(self, member_id, isbn):
        """
        Process a book return transaction

        Args:
            member_id: ID of the member returning
            isbn: ISBN of the book to return

        Returns:
            tuple: (success: bool, message: str)
        """
        if member_id not in self.members:
            return False, "Member not found"

        if isbn not in self.books:
            return False, "Book not found"

        book = self.books[isbn]
        member = self.members[member_id]

        if book.borrowed_by != member_id:
            return False, "This book was not borrowed by this member"

        # Process the return
        if book.return_book() and member.return_book(isbn):
            return True, "Book returned successfully"

        return False, "Failed to process return"

    def search_books(self, keyword):
        """
        Search for books by title or author

        Args:
            keyword: Search keyword

        Returns:
            list: List of matching Book objects
        """
        keyword_lower = keyword.lower()
        results = []

        for book in self.books.values():
            if (keyword_lower in book.title.lower() or
                keyword_lower in book.author.lower()):
                results.append(book)

        return results

    def get_available_books(self):
        """Get all available books"""
        return [book for book in self.books.values() if book.is_available]

    def get_borrowed_books(self):
        """Get all borrowed books"""
        return [book for book in self.books.values() if not book.is_available]

    def save_to_file(self, filename="data/library.json"):
        """Save library data to JSON file"""
        data = {
            "name": self.name,
            "books": [book.to_dict() for book in self.books.values()],
            "members": [member.to_dict() for member in self.members.values()]
        }

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_from_file(filename="data/library.json"):
        """Load library data from JSON file"""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)

            library = Library(data["name"])

            for book_data in data.get("books", []):
                book = Book.from_dict(book_data)
                library.books[book.isbn] = book

            for member_data in data.get("members", []):
                member = Member.from_dict(member_data)
                library.members[member.member_id] = member

            return library

        except FileNotFoundError:
            return None
        except Exception as e:
            print(f"Error loading library: {e}")
            return None
