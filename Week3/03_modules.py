"""
Week 3: Modules Examples
Topics: Importing modules, using built-in modules
"""

# Importing entire module
import math

print("=== Import Module ===")
print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Factorial of 5: {math.factorial(5)}")

# Importing specific functions
from math import pow, ceil, floor

print("\n=== From Import ===")
print(f"2^3 = {pow(2, 3)}")
print(f"Ceil of 4.3: {ceil(4.3)}")
print(f"Floor of 4.7: {floor(4.7)}")

# Importing with alias
import random as rnd

print("\n=== Import with Alias ===")
print(f"Random number (1-10): {rnd.randint(1, 10)}")
print(f"Random choice: {rnd.choice(['apple', 'banana', 'cherry'])}")

# Random module examples
import random

print("\n=== Random Module ===")
print(f"Random float (0-1): {random.random()}")
print(f"Random int (1-100): {random.randint(1, 100)}")

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

# Datetime module
from datetime import datetime, timedelta

print("\n=== Datetime Module ===")
now = datetime.now()
print(f"Current date and time: {now}")
print(f"Current year: {now.year}")
print(f"Current month: {now.month}")
print(f"Current day: {now.day}")

tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

# OS module
import os

print("\n=== OS Module ===")
print(f"Current directory: {os.getcwd()}")
print(f"User: {os.getenv('USER', 'Unknown')}")

# Collections module
from collections import Counter

print("\n=== Collections Module ===")
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
word_count = Counter(words)
print(f"Word count: {word_count}")
print(f"Most common: {word_count.most_common(2)}")
