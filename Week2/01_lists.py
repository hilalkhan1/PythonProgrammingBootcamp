"""
Week 2: Lists Examples
Topics: Creating lists, indexing, slicing, methods
"""

# Creating lists
fruits = ["apple", "banana", "cherry", "date"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print("=== Creating Lists ===")
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")

# Indexing
print("\n=== Indexing ===")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second fruit: {fruits[1]}")

# Slicing
print("\n=== Slicing ===")
print(f"First two fruits: {fruits[0:2]}")
print(f"Last two fruits: {fruits[-2:]}")
print(f"All fruits: {fruits[:]}")

# List methods
print("\n=== List Methods ===")

# append
fruits.append("elderberry")
print(f"After append: {fruits}")

# insert
fruits.insert(1, "avocado")
print(f"After insert: {fruits}")

# remove
fruits.remove("banana")
print(f"After remove: {fruits}")

# pop
popped = fruits.pop()
print(f"Popped item: {popped}, List: {fruits}")

# sort
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(f"Sorted numbers: {numbers}")

# reverse
numbers.reverse()
print(f"Reversed numbers: {numbers}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares using list comprehension: {squares}")

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nMatrix: {matrix}")
print(f"Element at [1][2]: {matrix[1][2]}")
