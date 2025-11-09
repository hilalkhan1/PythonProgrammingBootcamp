"""
Week 2: Sets Examples
Topics: Creating sets, operations, methods
"""

# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

print("=== Creating Sets ===")
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")

# Sets remove duplicates
duplicates = {1, 2, 2, 3, 3, 3, 4}
print(f"Set with duplicates removed: {duplicates}")

# Adding and removing
print("\n=== Adding/Removing ===")
fruits.add("orange")
print(f"After add: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

# discard (doesn't raise error if not found)
fruits.discard("grape")  # Won't raise error
print(f"After discard: {fruits}")

# Set operations
print("\n=== Set Operations ===")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Union (method): {set1.union(set2)}")

# Intersection
print(f"Intersection: {set1 & set2}")
print(f"Intersection (method): {set1.intersection(set2)}")

# Difference
print(f"Difference (set1 - set2): {set1 - set2}")
print(f"Difference (set2 - set1): {set2 - set1}")

# Symmetric difference
print(f"Symmetric Difference: {set1 ^ set2}")

# Set methods
print("\n=== Set Methods ===")
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(f"A: {a}, B: {b}")
print(f"A is subset of B: {a.issubset(b)}")
print(f"B is superset of A: {b.issuperset(a)}")

# Checking membership
print("\n=== Membership ===")
print(f"Is 'apple' in fruits: {'apple' in fruits}")
print(f"Is 'grape' in fruits: {'grape' in fruits}")

# Set comprehension
squares_set = {x**2 for x in range(1, 6)}
print(f"\nSquares set: {squares_set}")
