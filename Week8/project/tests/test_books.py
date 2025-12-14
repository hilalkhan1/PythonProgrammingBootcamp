"""
Week 8: Unit Tests for Book Classes
Tests for Book, EBook, and PhysicalBook classes
"""

import unittest
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from books import Book, EBook, PhysicalBook, create_book_from_dict


class TestBook(unittest.TestCase):
    """Test cases for the Book class"""

    def setUp(self):
        """Set up test fixtures"""
        self.book = Book("978-0-123456-47-2", "Test Book", "Test Author", 2020)

    def test_book_creation(self):
        """Test book is created with correct attributes"""
        self.assertEqual(self.book.isbn, "978-0-123456-47-2")
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.year, 2020)
        self.assertTrue(self.book.is_available)
        self.assertIsNone(self.book.borrowed_by)

    def test_borrow_book(self):
        """Test borrowing a book"""
        result = self.book.borrow("M001")
        self.assertTrue(result)
        self.assertFalse(self.book.is_available)
        self.assertEqual(self.book.borrowed_by, "M001")
        self.assertIsNotNone(self.book.due_date)

    def test_borrow_already_borrowed_book(self):
        """Test borrowing an already borrowed book fails"""
        self.book.borrow("M001")
        result = self.book.borrow("M002")
        self.assertFalse(result)
        self.assertEqual(self.book.borrowed_by, "M001")  # Still borrowed by M001

    def test_return_book(self):
        """Test returning a borrowed book"""
        self.book.borrow("M001")
        result = self.book.return_book()
        self.assertTrue(result)
        self.assertTrue(self.book.is_available)
        self.assertIsNone(self.book.borrowed_by)
        self.assertIsNone(self.book.due_date)

    def test_return_non_borrowed_book(self):
        """Test returning a book that wasn't borrowed fails"""
        result = self.book.return_book()
        self.assertFalse(result)

    def test_to_dict(self):
        """Test book serialization to dictionary"""
        book_dict = self.book.to_dict()
        self.assertEqual(book_dict['isbn'], "978-0-123456-47-2")
        self.assertEqual(book_dict['title'], "Test Book")
        self.assertEqual(book_dict['type'], "Book")


class TestEBook(unittest.TestCase):
    """Test cases for the EBook class"""

    def setUp(self):
        """Set up test fixtures"""
        self.ebook = EBook("978-0-111111-11-1", "Test EBook", "Test Author", 2021, 5.2, "PDF")

    def test_ebook_creation(self):
        """Test ebook is created with correct attributes"""
        self.assertEqual(self.ebook.isbn, "978-0-111111-11-1")
        self.assertEqual(self.ebook.file_size_mb, 5.2)
        self.assertEqual(self.ebook.file_format, "PDF")
        self.assertEqual(self.ebook._type, "EBook")

    def test_ebook_extended_loan_period(self):
        """Test ebooks have extended loan period (30 days)"""
        self.ebook.borrow("M001")
        # EBooks should have different loan period than regular books
        self.assertIsNotNone(self.ebook.due_date)

    def test_ebook_download_link(self):
        """Test ebook download link generation"""
        link = self.ebook.download_link()
        self.assertIn(self.ebook.isbn, link)
        self.assertIn("pdf", link.lower())


class TestPhysicalBook(unittest.TestCase):
    """Test cases for the PhysicalBook class"""

    def setUp(self):
        """Set up test fixtures"""
        self.physical = PhysicalBook("978-0-222222-22-2", "Physical Book", "Author", 2019, "A3-15", "Good")

    def test_physical_book_creation(self):
        """Test physical book is created with correct attributes"""
        self.assertEqual(self.physical.shelf_location, "A3-15")
        self.assertEqual(self.physical.condition, "Good")
        self.assertEqual(self.physical._type, "PhysicalBook")

    def test_update_condition(self):
        """Test updating book condition"""
        result = self.physical.update_condition("Fair")
        self.assertTrue(result)
        self.assertEqual(self.physical.condition, "Fair")

    def test_invalid_condition(self):
        """Test updating to invalid condition fails"""
        result = self.physical.update_condition("Excellent")  # Invalid
        self.assertFalse(result)
        self.assertEqual(self.physical.condition, "Good")  # Unchanged


class TestBookFactory(unittest.TestCase):
    """Test cases for the book factory function"""

    def test_create_regular_book(self):
        """Test creating regular book from dict"""
        data = {
            "type": "Book",
            "isbn": "123",
            "title": "Test",
            "author": "Author",
            "year": 2020,
            "is_available": True,
            "borrowed_by": None,
            "due_date": None
        }
        book = create_book_from_dict(data)
        self.assertIsInstance(book, Book)
        self.assertEqual(book._type, "Book")

    def test_create_ebook(self):
        """Test creating ebook from dict"""
        data = {
            "type": "EBook",
            "isbn": "123",
            "title": "Test",
            "author": "Author",
            "year": 2020,
            "file_size_mb": 3.5,
            "file_format": "EPUB",
            "is_available": True,
            "borrowed_by": None,
            "due_date": None
        }
        book = create_book_from_dict(data)
        self.assertIsInstance(book, EBook)
        self.assertEqual(book.file_format, "EPUB")

    def test_create_physical_book(self):
        """Test creating physical book from dict"""
        data = {
            "type": "PhysicalBook",
            "isbn": "123",
            "title": "Test",
            "author": "Author",
            "year": 2020,
            "shelf_location": "B2-10",
            "condition": "New",
            "is_available": True,
            "borrowed_by": None,
            "due_date": None
        }
        book = create_book_from_dict(data)
        self.assertIsInstance(book, PhysicalBook)
        self.assertEqual(book.shelf_location, "B2-10")


if __name__ == '__main__':
    unittest.main(verbosity=2)
