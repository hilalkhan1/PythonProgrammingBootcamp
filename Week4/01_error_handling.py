"""
Week 4: Error Handling Examples
Topics: try-except, else, finally, raising exceptions
"""

# Basic try-except
print("=== Basic Try-Except ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Multiple except blocks
print("\n=== Multiple Except Blocks ===")
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Value error occurred!")

# Catching multiple exceptions
print("\n=== Catching Multiple Exceptions ===")
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error occurred: {e}")

# Try-except-else
print("\n=== Try-Except-Else ===")
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print(f"You entered: {number}")
    print("This runs only if no exception occurred")

# Try-except-finally
print("\n=== Try-Except-Finally ===")
try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always executes - cleanup code goes here")
    # file.close() if file exists

# Raising exceptions
print("\n=== Raising Exceptions ===")


def validate_age(age):
    """Validate age and raise exception if invalid"""
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return True


try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

# General exception handling
print("\n=== General Exception ===")
try:
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {type(e).__name__}: {e}")

# Practical example: Safe division
def safe_divide(a, b):
    """Safely divide two numbers"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Please provide numeric values!")
        return None
    else:
        return result
    finally:
        print("Division operation completed")


print("\n=== Safe Division Function ===")
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
