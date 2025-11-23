"""
Week 6 Project: Enhanced Library Class
Works with book and member hierarchies
"""

import json
import os
from books import create_book_from_dict
from members import create_member_from_dict, TeacherMember


class Library:
    """Enhanced library system supporting different book and member types"""

    def __init__(self, name):
        """
        Initialize a library

        Args:
            name: Name of the library
        """
        self.name = name
        self.books = {}  # ISBN -> Book object (Book, EBook, or PhysicalBook)
        self.members = {}  # member_id -> Member object (Member, Student, or Teacher)

    def add_book(self, book):
        """Add a book to the library"""
        if book.isbn in self.books:
            return False, f"Book with ISBN {book.isbn} already exists"

        self.books[book.isbn] = book
        return True, f"Book '{book.title}' added successfully"

    def remove_book(self, isbn):
        """Remove a book from the library"""
        if isbn not in self.books:
            return False, "Book not found"

        if not self.books[isbn].is_available:
            return False, "Cannot remove borrowed book"

        del self.books[isbn]
        return True, "Book removed successfully"

    def add_member(self, member):
        """Add a member to the library"""
        if member.member_id in self.members:
            return False, f"Member with ID {member.member_id} already exists"

        self.members[member.member_id] = member
        return True, f"Member '{member.name}' added successfully"

    def remove_member(self, member_id):
        """Remove a member from the library"""
        if member_id not in self.members:
            return False, "Member not found"

        if self.members[member_id].borrowed_books:
            return False, "Cannot remove member with borrowed books"

        del self.members[member_id]
        return True, "Member removed successfully"

    def borrow_book(self, member_id, isbn):
        """
        Process a book borrowing transaction
        Uses polymorphism - different member types have different limits
        """
        if member_id not in self.members:
            return False, "Member not found"

        if isbn not in self.books:
            return False, "Book not found"

        book = self.books[isbn]
        member = self.members[member_id]

        if not book.is_available:
            return False, "Book is already borrowed"

        # Check if member can borrow (polymorphic - different limits for different member types)
        can_borrow, message = member.borrow_book(isbn)
        if not can_borrow:
            return False, message

        # Get loan period based on member type and book type
        days = 14  # Default

        # Teachers get extended loan periods
        if isinstance(member, TeacherMember):
            days = member.get_loan_period()

        # Process the borrowing
        if book.borrow(member_id, days):
            return True, f"Book borrowed successfully. Due date: {book.due_date}"

        # Rollback if book borrowing failed
        member.return_book(isbn)
        return False, "Failed to process borrowing"

    def return_book(self, member_id, isbn):
        """Process a book return transaction"""
        if member_id not in self.members:
            return False, "Member not found"

        if isbn not in self.books:
            return False, "Book not found"

        book = self.books[isbn]
        member = self.members[member_id]

        if book.borrowed_by != member_id:
            return False, "This book was not borrowed by this member"

        # Process the return
        return_success, return_msg = member.return_book(isbn)

        if return_success and book.return_book():
            return True, "Book returned successfully"

        return False, "Failed to process return"

    def search_books(self, keyword):
        """Search for books by title or author"""
        keyword_lower = keyword.lower()
        results = []

        for book in self.books.values():
            if (keyword_lower in book.title.lower() or
                keyword_lower in book.author.lower()):
                results.append(book)

        return results

    def get_books_by_type(self, book_type):
        """
        Get all books of a specific type

        Args:
            book_type: Type name ("EBook", "PhysicalBook", or "Book")

        Returns:
            list: List of books of the specified type
        """
        return [book for book in self.books.values() if book._type == book_type]

    def get_members_by_type(self, member_type):
        """
        Get all members of a specific type

        Args:
            member_type: Type name ("Student", "Teacher", or "Member")

        Returns:
            list: List of members of the specified type
        """
        return [member for member in self.members.values() if member._member_type == member_type]

    def get_available_books(self):
        """Get all available books"""
        return [book for book in self.books.values() if book.is_available]

    def get_borrowed_books(self):
        """Get all borrowed books"""
        return [book for book in self.books.values() if not book.is_available]

    def get_overdue_books(self):
        """Get all overdue books"""
        from datetime import datetime

        overdue = []
        today = datetime.now().strftime("%Y-%m-%d")

        for book in self.books.values():
            if not book.is_available and book.due_date and book.due_date < today:
                overdue.append(book)

        return overdue

    def get_member_borrowed_books(self, member_id):
        """Get all books borrowed by a specific member"""
        if member_id not in self.members:
            return []

        member = self.members[member_id]
        borrowed_books = []

        for isbn in member.borrowed_books:
            if isbn in self.books:
                borrowed_books.append(self.books[isbn])

        return borrowed_books

    def save_to_file(self, filename="data/library.json"):
        """Save library data to JSON file"""
        data = {
            "name": self.name,
            "books": [book.to_dict() for book in self.books.values()],
            "members": [member.to_dict() for member in self.members.values()]
        }

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_from_file(filename="data/library.json"):
        """Load library data from JSON file"""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)

            library = Library(data["name"])

            # Load books using factory function
            for book_data in data.get("books", []):
                book = create_book_from_dict(book_data)
                library.books[book.isbn] = book

            # Load members using factory function
            for member_data in data.get("members", []):
                member = create_member_from_dict(member_data)
                library.members[member.member_id] = member

            return library

        except FileNotFoundError:
            return None
        except Exception as e:
            print(f"Error loading library: {e}")
            return None
