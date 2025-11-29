"""
Week 6 Project: Member Class Hierarchy
Demonstrates: Inheritance, Polymorphism, Encapsulation
Classes: Member (base), StudentMember, TeacherMember
"""

from datetime import datetime


class Member:
    """Base class representing a library member"""

    def __init__(self, member_id, name, email):
        """
        Initialize a member

        Args:
            member_id: Unique member ID
            name: Member's full name
            email: Member's email address
        """
        self._member_id = member_id  # Protected
        self._name = name  # Protected
        self._email = email  # Protected
        self._borrowed_books = []  # Protected: List of ISBNs
        self._join_date = datetime.now().strftime("%Y-%m-%d")
        self._member_type = "Member"
        self._max_books = 3  # Protected: Default borrowing limit

    # Property for member_id (read-only)
    @property
    def member_id(self):
        """Get member ID"""
        return self._member_id

    # Property for name
    @property
    def name(self):
        """Get member name"""
        return self._name

    @name.setter
    def name(self, value):
        """Set member name"""
        if value and len(value.strip()) > 0:
            self._name = value.strip()

    # Property for email
    @property
    def email(self):
        """Get member email"""
        return self._email

    @email.setter
    def email(self, value):
        """Set member email"""
        if value and '@' in value:
            self._email = value

    # Property for borrowed books (read-only)
    @property
    def borrowed_books(self):
        """Get list of borrowed book ISBNs"""
        return self._borrowed_books.copy()  # Return copy to protect internal list

    # Property for max books
    @property
    def max_books(self):
        """Get maximum borrowing limit"""
        return self._max_books

    def can_borrow(self):
        """
        Check if member can borrow more books

        Returns:
            bool: True if can borrow, False otherwise
        """
        return len(self._borrowed_books) < self._max_books

    def borrow_book(self, isbn):
        """
        Add a book to member's borrowed list

        Args:
            isbn: ISBN of the borrowed book

        Returns:
            tuple: (success: bool, message: str)
        """
        if isbn in self._borrowed_books:
            return False, "Book already borrowed by this member"

        if not self.can_borrow():
            return False, f"Borrowing limit reached ({self._max_books} books)"

        self._borrowed_books.append(isbn)
        return True, "Book added to borrowed list"

    def return_book(self, isbn):
        """
        Remove a book from member's borrowed list

        Args:
            isbn: ISBN of the book to return

        Returns:
            tuple: (success: bool, message: str)
        """
        if isbn not in self._borrowed_books:
            return False, "Book not in borrowed list"

        self._borrowed_books.remove(isbn)
        return True, "Book removed from borrowed list"

    def get_info(self):
        """Get member information - polymorphic method"""
        return (f"{self._name} ({self._email}) - "
                f"{len(self._borrowed_books)}/{self._max_books} books borrowed")

    def __str__(self):
        """String representation of the member"""
        return f"[{self._member_type}] [{self._member_id}] {self.get_info()}"

    def to_dict(self):
        """Convert member to dictionary for JSON serialization"""
        return {
            "type": self._member_type,
            "member_id": self._member_id,
            "name": self._name,
            "email": self._email,
            "borrowed_books": self._borrowed_books,
            "join_date": self._join_date,
            "max_books": self._max_books
        }


class StudentMember(Member):
    """Student member with student ID and major"""

    def __init__(self, member_id, name, email, student_id, major):
        """
        Initialize a student member

        Args:
            member_id: Unique member ID
            name: Student's full name
            email: Student's email address
            student_id: Student ID number
            major: Academic major/field of study
        """
        super().__init__(member_id, name, email)
        self.student_id = student_id
        self.major = major
        self._member_type = "Student"
        self._max_books = 5  # Students can borrow more books

    def get_info(self):
        """Get student-specific information - polymorphic override"""
        base_info = super().get_info()
        return f"{base_info} | Student ID: {self.student_id} | Major: {self.major}"

    def to_dict(self):
        """Convert student member to dictionary"""
        data = super().to_dict()
        data.update({
            "student_id": self.student_id,
            "major": self.major
        })
        return data


class TeacherMember(Member):
    """Teacher member with department and faculty ID"""

    def __init__(self, member_id, name, email, faculty_id, department):
        """
        Initialize a teacher member

        Args:
            member_id: Unique member ID
            name: Teacher's full name
            email: Teacher's email address
            faculty_id: Faculty ID number
            department: Department name
        """
        super().__init__(member_id, name, email)
        self.faculty_id = faculty_id
        self.department = department
        self._member_type = "Teacher"
        self._max_books = 10  # Teachers can borrow most books
        self._extended_loan = True  # Teachers get extended loan periods

    @property
    def has_extended_loan(self):
        """Check if teacher has extended loan privileges"""
        return self._extended_loan

    def get_loan_period(self):
        """
        Get loan period for teacher

        Returns:
            int: Number of days for loan
        """
        return 30 if self._extended_loan else 14

    def get_info(self):
        """Get teacher-specific information - polymorphic override"""
        base_info = super().get_info()
        return f"{base_info} | Faculty ID: {self.faculty_id} | Dept: {self.department}"

    def to_dict(self):
        """Convert teacher member to dictionary"""
        data = super().to_dict()
        data.update({
            "faculty_id": self.faculty_id,
            "department": self.department,
            "extended_loan": self._extended_loan
        })
        return data


def create_member_from_dict(data):
    """
    Factory function to create appropriate member type from dictionary

    Args:
        data: Dictionary containing member data

    Returns:
        Member object (Member, StudentMember, or TeacherMember)
    """
    member_type = data.get("type", "Member")

    if member_type == "Student":
        member = StudentMember(
            data["member_id"],
            data["name"],
            data["email"],
            data.get("student_id", ""),
            data.get("major", "")
        )
    elif member_type == "Teacher":
        member = TeacherMember(
            data["member_id"],
            data["name"],
            data["email"],
            data.get("faculty_id", ""),
            data.get("department", "")
        )
        member._extended_loan = data.get("extended_loan", True)
    else:
        member = Member(data["member_id"], data["name"], data["email"])

    # Restore borrowing state
    member._borrowed_books = data.get("borrowed_books", [])
    member._join_date = data.get("join_date", datetime.now().strftime("%Y-%m-%d"))
    member._max_books = data.get("max_books", member._max_books)

    return member
