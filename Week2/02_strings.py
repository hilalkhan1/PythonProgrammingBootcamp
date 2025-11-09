"""
Week 2: Strings Examples
Topics: String methods, formatting, slicing
"""

# String creation
message = "Hello, Python Programming!"
print(f"Message: {message}")

# String indexing and slicing
print("\n=== Indexing and Slicing ===")
print(f"First character: {message[0]}")
print(f"Last character: {message[-1]}")
print(f"First 5 characters: {message[0:5]}")
print(f"Every 2nd character: {message[::2]}")

# String methods
print("\n=== String Methods ===")

text = "  python programming  "
print(f"Original: '{text}'")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
print(f"Strip: '{text.strip()}'")

# Find and replace
sentence = "I love Java. Java is great!"
print(f"\nOriginal: {sentence}")
print(f"Find 'Java': {sentence.find('Java')}")
print(f"Count 'Java': {sentence.count('Java')}")
print(f"Replace: {sentence.replace('Java', 'Python')}")

# Split and join
print("\n=== Split and Join ===")
words = "Python is awesome"
word_list = words.split()
print(f"Split: {word_list}")

joined = "-".join(word_list)
print(f"Join with '-': {joined}")

# String formatting
print("\n=== String Formatting ===")
name = "Alice"
age = 25
score = 95.5

# f-strings
print(f"{name} is {age} years old and scored {score}%")

# format method
print("{} is {} years old and scored {}%".format(name, age, score))

# String checking methods
print("\n=== Checking Methods ===")
text1 = "Python123"
text2 = "Python"
text3 = "123"

print(f"'{text1}' is alphanumeric: {text1.isalnum()}")
print(f"'{text2}' is alphabetic: {text2.isalpha()}")
print(f"'{text3}' is digit: {text3.isdigit()}")
