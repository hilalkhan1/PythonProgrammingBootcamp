"""
Week 8: Unit Tests for Library Class
Tests for library management operations
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from library import Library
from books import Book, EBook, PhysicalBook
from members import Member, StudentMember, TeacherMember


class TestLibrary(unittest.TestCase):
    """Test cases for the Library class"""

    def setUp(self):
        """Set up test fixtures"""
        self.library = Library("Test Library")
        self.book1 = Book("ISBN1", "Book 1", "Author 1", 2020)
        self.book2 = EBook("ISBN2", "EBook 1", "Author 2", 2021, 3.5, "PDF")
        self.member1 = Member("M001", "John Doe", "john@example.com")
        self.member2 = StudentMember("S001", "Alice", "alice@uni.edu", "STU123", "CS")

    def test_library_creation(self):
        """Test library is created correctly"""
        self.assertEqual(self.library.name, "Test Library")
        self.assertEqual(len(self.library.books), 0)
        self.assertEqual(len(self.library.members), 0)

    def test_add_book(self):
        """Test adding a book to library"""
        success, message = self.library.add_book(self.book1)
        self.assertTrue(success)
        self.assertEqual(len(self.library.books), 1)
        self.assertIn("ISBN1", self.library.books)

    def test_add_duplicate_book(self):
        """Test adding duplicate book fails"""
        self.library.add_book(self.book1)
        success, message = self.library.add_book(self.book1)
        self.assertFalse(success)
        self.assertEqual(len(self.library.books), 1)

    def test_remove_book(self):
        """Test removing a book from library"""
        self.library.add_book(self.book1)
        success, message = self.library.remove_book("ISBN1")
        self.assertTrue(success)
        self.assertEqual(len(self.library.books), 0)

    def test_remove_borrowed_book(self):
        """Test removing borrowed book fails"""
        self.library.add_book(self.book1)
        self.library.add_member(self.member1)
        self.library.borrow_book("M001", "ISBN1")

        success, message = self.library.remove_book("ISBN1")
        self.assertFalse(success)

    def test_add_member(self):
        """Test adding a member to library"""
        success, message = self.library.add_member(self.member1)
        self.assertTrue(success)
        self.assertEqual(len(self.library.members), 1)

    def test_add_duplicate_member(self):
        """Test adding duplicate member fails"""
        self.library.add_member(self.member1)
        success, message = self.library.add_member(self.member1)
        self.assertFalse(success)

    def test_remove_member(self):
        """Test removing a member from library"""
        self.library.add_member(self.member1)
        success, message = self.library.remove_member("M001")
        self.assertTrue(success)
        self.assertEqual(len(self.library.members), 0)

    def test_remove_member_with_books(self):
        """Test removing member with borrowed books fails"""
        self.library.add_book(self.book1)
        self.library.add_member(self.member1)
        self.library.borrow_book("M001", "ISBN1")

        success, message = self.library.remove_member("M001")
        self.assertFalse(success)

    def test_borrow_book(self):
        """Test borrowing a book"""
        self.library.add_book(self.book1)
        self.library.add_member(self.member1)

        success, message = self.library.borrow_book("M001", "ISBN1")
        self.assertTrue(success)
        self.assertFalse(self.book1.is_available)
        self.assertIn("ISBN1", self.member1.borrowed_books)

    def test_borrow_nonexistent_book(self):
        """Test borrowing non-existent book fails"""
        self.library.add_member(self.member1)
        success, message = self.library.borrow_book("M001", "FAKE_ISBN")
        self.assertFalse(success)

    def test_borrow_by_nonexistent_member(self):
        """Test borrowing by non-existent member fails"""
        self.library.add_book(self.book1)
        success, message = self.library.borrow_book("FAKE_ID", "ISBN1")
        self.assertFalse(success)

    def test_borrow_already_borrowed_book(self):
        """Test borrowing already borrowed book fails"""
        self.library.add_book(self.book1)
        self.library.add_member(self.member1)
        self.library.add_member(self.member2)

        self.library.borrow_book("M001", "ISBN1")
        success, message = self.library.borrow_book("S001", "ISBN1")
        self.assertFalse(success)

    def test_return_book(self):
        """Test returning a book"""
        self.library.add_book(self.book1)
        self.library.add_member(self.member1)
        self.library.borrow_book("M001", "ISBN1")

        success, message = self.library.return_book("M001", "ISBN1")
        self.assertTrue(success)
        self.assertTrue(self.book1.is_available)
        self.assertNotIn("ISBN1", self.member1.borrowed_books)

    def test_return_book_wrong_member(self):
        """Test returning book borrowed by different member fails"""
        self.library.add_book(self.book1)
        self.library.add_member(self.member1)
        self.library.add_member(self.member2)
        self.library.borrow_book("M001", "ISBN1")

        success, message = self.library.return_book("S001", "ISBN1")
        self.assertFalse(success)

    def test_search_books(self):
        """Test searching books by keyword"""
        book3 = Book("ISBN3", "Python Programming", "Author 3", 2022)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(book3)

        results = self.library.search_books("Python")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Python Programming")

    def test_get_available_books(self):
        """Test getting available books"""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_member(self.member1)
        self.library.borrow_book("M001", "ISBN1")

        available = self.library.get_available_books()
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].isbn, "ISBN2")

    def test_get_borrowed_books(self):
        """Test getting borrowed books"""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_member(self.member1)
        self.library.borrow_book("M001", "ISBN1")

        borrowed = self.library.get_borrowed_books()
        self.assertEqual(len(borrowed), 1)
        self.assertEqual(borrowed[0].isbn, "ISBN1")

    def test_get_books_by_type(self):
        """Test getting books filtered by type"""
        self.library.add_book(self.book1)  # Regular Book
        self.library.add_book(self.book2)  # EBook

        ebooks = self.library.get_books_by_type("EBook")
        self.assertEqual(len(ebooks), 1)
        self.assertIsInstance(ebooks[0], EBook)

    def test_get_members_by_type(self):
        """Test getting members filtered by type"""
        self.library.add_member(self.member1)  # Regular Member
        self.library.add_member(self.member2)  # Student

        students = self.library.get_members_by_type("Student")
        self.assertEqual(len(students), 1)
        self.assertIsInstance(students[0], StudentMember)


if __name__ == '__main__':
    unittest.main(verbosity=2)
