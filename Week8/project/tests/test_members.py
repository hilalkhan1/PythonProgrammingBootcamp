"""
Week 8: Unit Tests for Member Classes
Tests for Member, StudentMember, and TeacherMember classes
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from members import Member, StudentMember, TeacherMember, create_member_from_dict


class TestMember(unittest.TestCase):
    """Test cases for the Member class"""

    def setUp(self):
        """Set up test fixtures"""
        self.member = Member("M001", "John Doe", "john@example.com")

    def test_member_creation(self):
        """Test member is created with correct attributes"""
        self.assertEqual(self.member.member_id, "M001")
        self.assertEqual(self.member.name, "John Doe")
        self.assertEqual(self.member.email, "john@example.com")
        self.assertEqual(len(self.member.borrowed_books), 0)
        self.assertEqual(self.member.max_books, 3)

    def test_member_id_readonly(self):
        """Test that member_id is read-only"""
        with self.assertRaises(AttributeError):
            self.member.member_id = "M002"

    def test_name_property(self):
        """Test name property getter and setter"""
        self.member.name = "Jane Smith"
        self.assertEqual(self.member.name, "Jane Smith")

    def test_email_property(self):
        """Test email property getter and setter"""
        self.member.email = "jane@example.com"
        self.assertEqual(self.member.email, "jane@example.com")

    def test_invalid_email(self):
        """Test setting invalid email is rejected"""
        original_email = self.member.email
        self.member.email = "invalid-email"  # No @ symbol
        self.assertEqual(self.member.email, original_email)  # Unchanged

    def test_borrow_book(self):
        """Test borrowing a book"""
        success, message = self.member.borrow_book("ISBN123")
        self.assertTrue(success)
        self.assertIn("ISBN123", self.member.borrowed_books)

    def test_borrow_duplicate_book(self):
        """Test borrowing same book twice fails"""
        self.member.borrow_book("ISBN123")
        success, message = self.member.borrow_book("ISBN123")
        self.assertFalse(success)

    def test_borrow_limit(self):
        """Test borrowing limit enforcement"""
        self.member.borrow_book("ISBN1")
        self.member.borrow_book("ISBN2")
        self.member.borrow_book("ISBN3")

        # Should fail - limit reached
        success, message = self.member.borrow_book("ISBN4")
        self.assertFalse(success)
        self.assertIn("limit", message.lower())

    def test_return_book(self):
        """Test returning a book"""
        self.member.borrow_book("ISBN123")
        success, message = self.member.return_book("ISBN123")
        self.assertTrue(success)
        self.assertNotIn("ISBN123", self.member.borrowed_books)

    def test_return_non_borrowed_book(self):
        """Test returning a book not borrowed fails"""
        success, message = self.member.return_book("ISBN999")
        self.assertFalse(success)


class TestStudentMember(unittest.TestCase):
    """Test cases for the StudentMember class"""

    def setUp(self):
        """Set up test fixtures"""
        self.student = StudentMember("S001", "Alice Student", "alice@uni.edu", "STU123", "Computer Science")

    def test_student_creation(self):
        """Test student member is created with correct attributes"""
        self.assertEqual(self.student.student_id, "STU123")
        self.assertEqual(self.student.major, "Computer Science")
        self.assertEqual(self.student._member_type, "Student")

    def test_student_higher_limit(self):
        """Test students have higher borrowing limit"""
        self.assertEqual(self.student.max_books, 5)
        self.assertGreater(self.student.max_books, 3)  # More than regular members

    def test_student_can_borrow_more(self):
        """Test student can borrow up to their limit"""
        for i in range(5):
            success, _ = self.student.borrow_book(f"ISBN{i}")
            self.assertTrue(success)

        # 6th book should fail
        success, _ = self.student.borrow_book("ISBN6")
        self.assertFalse(success)


class TestTeacherMember(unittest.TestCase):
    """Test cases for the TeacherMember class"""

    def setUp(self):
        """Set up test fixtures"""
        self.teacher = TeacherMember("T001", "Prof. Smith", "smith@uni.edu", "FAC456", "Mathematics")

    def test_teacher_creation(self):
        """Test teacher member is created with correct attributes"""
        self.assertEqual(self.teacher.faculty_id, "FAC456")
        self.assertEqual(self.teacher.department, "Mathematics")
        self.assertEqual(self.teacher._member_type, "Teacher")

    def test_teacher_highest_limit(self):
        """Test teachers have highest borrowing limit"""
        self.assertEqual(self.teacher.max_books, 10)
        self.assertGreater(self.teacher.max_books, 5)  # More than students

    def test_teacher_extended_loan(self):
        """Test teachers have extended loan privileges"""
        self.assertTrue(self.teacher.has_extended_loan)

    def test_teacher_loan_period(self):
        """Test teacher loan period is extended"""
        loan_period = self.teacher.get_loan_period()
        self.assertEqual(loan_period, 30)


class TestMemberFactory(unittest.TestCase):
    """Test cases for the member factory function"""

    def test_create_regular_member(self):
        """Test creating regular member from dict"""
        data = {
            "type": "Member",
            "member_id": "M001",
            "name": "Test User",
            "email": "test@example.com",
            "borrowed_books": [],
            "join_date": "2024-01-01",
            "max_books": 3
        }
        member = create_member_from_dict(data)
        self.assertIsInstance(member, Member)
        self.assertEqual(member._member_type, "Member")

    def test_create_student(self):
        """Test creating student from dict"""
        data = {
            "type": "Student",
            "member_id": "S001",
            "name": "Student",
            "email": "student@uni.edu",
            "student_id": "STU123",
            "major": "CS",
            "borrowed_books": [],
            "join_date": "2024-01-01",
            "max_books": 5
        }
        member = create_member_from_dict(data)
        self.assertIsInstance(member, StudentMember)
        self.assertEqual(member.student_id, "STU123")

    def test_create_teacher(self):
        """Test creating teacher from dict"""
        data = {
            "type": "Teacher",
            "member_id": "T001",
            "name": "Teacher",
            "email": "teacher@uni.edu",
            "faculty_id": "FAC456",
            "department": "Math",
            "extended_loan": True,
            "borrowed_books": [],
            "join_date": "2024-01-01",
            "max_books": 10
        }
        member = create_member_from_dict(data)
        self.assertIsInstance(member, TeacherMember)
        self.assertEqual(member.faculty_id, "FAC456")


if __name__ == '__main__':
    unittest.main(verbosity=2)
