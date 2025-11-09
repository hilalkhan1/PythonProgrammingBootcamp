"""
Week 4: CSV File Operations Examples
Topics: Reading and writing CSV files
"""

import csv

# Writing CSV file
print("=== Writing CSV File ===")

students = [
    ["Name", "Age", "Grade", "Score"],
    ["Alice", "20", "A", "95"],
    ["Bob", "21", "B", "85"],
    ["Charlie", "19", "A", "92"],
    ["David", "22", "C", "78"]
]

with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully!")

# Reading CSV file
print("\n=== Reading CSV File ===")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Reading CSV with header
print("\n=== Reading CSV with Header ===")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header
    print(f"Header: {header}")
    print("\nStudent Data:")
    for row in reader:
        print(f"  {row[0]}: Age {row[1]}, Grade {row[2]}, Score {row[3]}")

# Using DictReader
print("\n=== Using DictReader ===")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']}: {row['Score']}%")

# Using DictWriter
print("\n=== Using DictWriter ===")

products = [
    {"Product": "Laptop", "Price": "1000", "Quantity": "5"},
    {"Product": "Mouse", "Price": "25", "Quantity": "50"},
    {"Product": "Keyboard", "Price": "75", "Quantity": "30"}
]

with open("products.csv", "w", newline='') as file:
    fieldnames = ["Product", "Price", "Quantity"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(products)

print("Products CSV created!")

# Reading products
print("\nReading products:")
with open("products.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_value = int(row['Price']) * int(row['Quantity'])
        print(f"{row['Product']}: ${row['Price']} x {row['Quantity']} = ${total_value}")

# Appending to CSV
print("\n=== Appending to CSV ===")
new_student = ["Eve", "20", "A", "97"]

with open("students.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(new_student)

print("New student added!")

# Processing CSV data
print("\n=== Processing CSV Data ===")


def calculate_class_average(filename):
    """Calculate average score from CSV file"""
    total_score = 0
    count = 0

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_score += int(row['Score'])
            count += 1

    return total_score / count if count > 0 else 0


average = calculate_class_average("students.csv")
print(f"Class average: {average:.2f}%")

# Cleanup
import os
os.remove("students.csv")
os.remove("products.csv")
print("\nCleanup: CSV files removed")
