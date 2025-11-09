"""
Week 1: Conditionals Examples
Topics: if, elif, else
"""

# Simple if statement
age = 18
if age >= 18:
    print("You are eligible to vote!")

# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("Weather is pleasant.")

# if-elif-else statement
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Score: {score}, Grade: {grade}")

# Nested conditionals
username = "admin"
password = "secret123"

if username == "admin":
    if password == "secret123":
        print("Login successful!")
    else:
        print("Incorrect password!")
else:
    print("User not found!")

# Multiple conditions
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
else:
    print("You cannot drive.")
