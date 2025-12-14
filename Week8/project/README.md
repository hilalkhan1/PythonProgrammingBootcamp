# Library Management System
## Python Programming Bootcamp - Week 8 Final Project

### Overview
A comprehensive library management system demonstrating professional Python development practices including OOP, functional programming, and comprehensive testing.

### Features

#### Core Functionality
- **Book Management**: Add, remove, search books
- **Member Management**: Handle different member types (Regular, Student, Teacher)
- **Borrowing System**: Borrow and return books with due dates
- **Book Types**: Support for Physical Books and EBooks with specific attributes
- **Member Types**: Different borrowing limits and privileges based on member type

#### Advanced Features (Week 6-8)
- **Inheritance & Polymorphism**: Book and Member hierarchies
- **Encapsulation**: Protected attributes with property decorators
- **Analytics**: Data analysis using lambda, map, filter, reduce
- **Report Generation**: Memory-efficient generators for large datasets
- **Custom Decorators**: Logging, timing, validation
- **Comprehensive Testing**: Unit tests for all major components

### Project Structure

```
Week8/project/
├── main.py                 # Entry point
├── books.py                # Book class hierarchy
├── members.py              # Member class hierarchy
├── library.py              # Library management class
├── analytics.py            # Data analysis functions
├── reports.py              # Report generators
├── decorators.py           # Custom decorators
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_books.py
│   ├── test_members.py
│   └── test_library.py
├── data/                   # Data storage
│   └── library.json
├── requirements.txt        # Dependencies
└── README.md              # This file
```

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd Week8/project
   ```

2. **No external dependencies required!**
   This project uses only Python standard library.

3. **Optional: Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

### Usage

#### Running the Application
```bash
python main.py
```

#### Running Tests
```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests.test_books

# Run with verbose output
python -m unittest discover tests -v

# Run a specific test class
python -m unittest tests.test_library.TestLibrary

# Run a specific test method
python -m unittest tests.test_books.TestBook.test_borrow_book
```

### Class Hierarchy

#### Books
```
Book (base class)
├── EBook
│   ├── file_size_mb
│   ├── file_format
│   └── Extended loan period (30 days)
└── PhysicalBook
    ├── shelf_location
    ├── condition
    └── Standard loan period (14 days)
```

#### Members
```
Member (base class) - 3 books max
├── StudentMember - 5 books max
│   ├── student_id
│   └── major
└── TeacherMember - 10 books max
    ├── faculty_id
    ├── department
    └── Extended loan privileges
```

### Key Concepts Demonstrated

#### Week 5 - OOP Basics
- Classes and objects
- Methods and attributes
- Encapsulation

#### Week 6 - Advanced OOP
- Inheritance
- Polymorphism
- Abstract base classes
- Property decorators (@property)
- Method overriding

#### Week 7 - Functional Programming
- Lambda functions
- map(), filter(), reduce()
- Generators and yield
- Custom decorators
- List comprehensions

#### Week 8 - Testing & Best Practices
- Unit testing with unittest
- Test fixtures (setUp/tearDown)
- Assertions and test cases
- Code organization
- Documentation
- Type hints (optional)

### Analytics Features

#### Popular Authors
```python
# Get top N authors by book count
authors = get_popular_authors(library, top_n=5)
```

#### Borrowing Statistics
```python
# Get comprehensive borrowing stats
stats = get_borrowing_statistics(library)
```

#### Library Value Estimation
```python
# Calculate estimated collection value
value = calculate_library_value(library)
```

#### Filter by Year Range
```python
# Filter books published between years
books = filter_books_by_year(library, 2010, 2023)
```

### Report Generation

#### Overdue Books Report
```python
# Generate report of overdue books (using generator)
for overdue in generate_overdue_report(library):
    print(f"{overdue['title']} - {overdue['days_overdue']} days overdue")
```

#### Member Activity Report
```python
# Generate member activity report
for activity in generate_member_activity_report(library):
    print(f"{activity['name']}: {activity['books_borrowed']} books")
```

### Testing Coverage

- **Book Tests**: 15+ test cases covering all book types
- **Member Tests**: 12+ test cases covering all member types
- **Library Tests**: 20+ test cases covering all operations

### Development

#### Running in Development Mode
```bash
# Enable debug mode (if implemented)
python main.py --debug
```

#### Adding New Features
1. Write failing tests first (TDD approach)
2. Implement the feature
3. Run tests to verify
4. Refactor if needed

### Best Practices Implemented

✅ **Code Organization**: Modular structure with separate concerns
✅ **Encapsulation**: Protected/private attributes
✅ **DRY Principle**: Reusable functions and methods
✅ **Documentation**: Docstrings for all classes and functions
✅ **Error Handling**: Proper exception handling throughout
✅ **Type Safety**: Return tuples with (success, message) pattern
✅ **Testing**: Comprehensive unit test coverage
✅ **Version Control Ready**: Proper .gitignore patterns
✅ **Data Persistence**: JSON-based storage

### Future Enhancements

- [ ] Database integration (SQLite)
- [ ] Web interface (Flask/Django)
- [ ] User authentication
- [ ] Fine calculation for overdue books
- [ ] Book reservations
- [ ] Email notifications
- [ ] Multi-library support
- [ ] ISBN validation
- [ ] Barcode scanning

### Learning Outcomes

By completing this project, you have demonstrated:

1. **Object-Oriented Programming**
   - Class design and implementation
   - Inheritance and polymorphism
   - Encapsulation and data hiding

2. **Functional Programming**
   - Higher-order functions
   - Lambda expressions
   - Generators and iterators

3. **Software Engineering**
   - Testing and TDD
   - Code organization
   - Documentation
   - Best practices

4. **Python Mastery**
   - Advanced Python features
   - Standard library usage
   - Professional code structure

### License

Educational project for Python Programming Bootcamp

### Contact

For questions or issues, contact your instructor.

---

**Congratulations on completing the Python Programming Bootcamp!** 🎉
