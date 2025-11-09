"""
Week 4: File Operations Examples
Topics: Reading, writing, appending files
"""

# Writing to a file
print("=== Writing to File ===")
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is a sample file.\n")
    file.write("Learning file operations.\n")
print("File written successfully!")

# Reading entire file
print("\n=== Reading Entire File ===")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
print("\n=== Reading Line by Line ===")
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())

# Reading with readlines()
print("\n=== Reading with readlines() ===")
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")

# Appending to file
print("\n=== Appending to File ===")
with open("sample.txt", "a") as file:
    file.write("This line is appended.\n")
print("Content appended!")

# Reading updated file
print("\nUpdated file content:")
with open("sample.txt", "r") as file:
    print(file.read())

# File operations with error handling
print("\n=== File Operations with Error Handling ===")


def safe_read_file(filename):
    """Safely read a file with error handling"""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'!")
        return None


content = safe_read_file("sample.txt")
if content:
    print("File read successfully!")

# Writing lists to file
print("\n=== Writing Lists to File ===")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

# Reading into list
with open("fruits.txt", "r") as file:
    loaded_fruits = [line.strip() for line in file]
    print(f"Loaded fruits: {loaded_fruits}")

# File modes reference
print("\n=== File Modes ===")
print("'r'  - Read (default)")
print("'w'  - Write (overwrites)")
print("'a'  - Append")
print("'r+' - Read and Write")
print("'w+' - Write and Read (overwrites)")
print("'a+' - Append and Read")

# Cleanup
import os
os.remove("sample.txt")
os.remove("fruits.txt")
print("\nCleanup: Sample files removed")
