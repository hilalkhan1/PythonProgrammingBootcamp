"""
Week 4 Project: File Handler Module
Handles loading and saving student data to JSON files
Includes error handling for file operations
"""

import json
import os


def save_students(students, filename="data/students.json"):
    """
    Save student data to a JSON file

    Args:
        students: List of student dictionaries
        filename: Path to the JSON file

    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        # Ensure the data directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Convert set to list for subjects (if needed)
        with open(filename, 'w') as file:
            json.dump(students, file, indent=4)

        return True, f"Data saved successfully to {filename}"

    except PermissionError:
        return False, f"Error: Permission denied to write to {filename}"
    except Exception as e:
        return False, f"Error saving data: {str(e)}"


def load_students(filename="data/students.json"):
    """
    Load student data from a JSON file

    Args:
        filename: Path to the JSON file

    Returns:
        tuple: (students: list, all_subjects: set, message: str)
    """
    try:
        # Check if file exists
        if not os.path.exists(filename):
            return [], set(), f"No existing data file found. Starting fresh."

        # Read and parse JSON file
        with open(filename, 'r') as file:
            students = json.load(file)

        # Validate data structure
        if not isinstance(students, list):
            return [], set(), "Error: Invalid data format in file. Starting fresh."

        # Extract all unique subjects from loaded data
        all_subjects = set()
        for student in students:
            if 'grades' in student and isinstance(student['grades'], dict):
                all_subjects.update(student['grades'].keys())

        return students, all_subjects, f"Loaded {len(students)} students from {filename}"

    except json.JSONDecodeError:
        return [], set(), f"Error: File {filename} contains invalid JSON. Starting fresh."
    except PermissionError:
        return [], set(), f"Error: Permission denied to read {filename}. Starting fresh."
    except Exception as e:
        return [], set(), f"Error loading data: {str(e)}. Starting fresh."


def validate_student_data(student):
    """
    Validate that a student dictionary has the required fields

    Args:
        student: Student dictionary to validate

    Returns:
        bool: True if valid, False otherwise
    """
    try:
        # Check required fields
        if 'name' not in student or not isinstance(student['name'], str):
            return False

        if 'grades' not in student or not isinstance(student['grades'], dict):
            return False

        if 'average' not in student or not isinstance(student['average'], (int, float)):
            return False

        # Validate grades
        for subject, grade in student['grades'].items():
            if not isinstance(subject, str) or not isinstance(grade, (int, float)):
                return False
            if grade < 0 or grade > 100:
                return False

        return True

    except Exception:
        return False


def create_backup(filename="data/students.json"):
    """
    Create a backup of the current data file

    Args:
        filename: Path to the JSON file

    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        if not os.path.exists(filename):
            return False, "No data file to backup."

        backup_filename = filename.replace('.json', '_backup.json')

        with open(filename, 'r') as source:
            data = source.read()

        with open(backup_filename, 'w') as backup:
            backup.write(data)

        return True, f"Backup created: {backup_filename}"

    except Exception as e:
        return False, f"Error creating backup: {str(e)}"
