"""
Week 2: Tuples Examples
Topics: Creating tuples, immutability, tuple methods
"""

# Creating tuples
coordinates = (10, 20)
colors = ("red", "green", "blue")
mixed_tuple = (1, "hello", 3.14, True)

print("=== Creating Tuples ===")
print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"Mixed: {mixed_tuple}")

# Single element tuple
single = (42,)  # Note the comma
print(f"Single element tuple: {single}")

# Indexing and slicing
print("\n=== Indexing and Slicing ===")
print(f"First color: {colors[0]}")
print(f"Last color: {colors[-1]}")
print(f"First two colors: {colors[0:2]}")

# Tuple unpacking
print("\n=== Tuple Unpacking ===")
x, y = coordinates
print(f"x = {x}, y = {y}")

r, g, b = colors
print(f"Red: {r}, Green: {g}, Blue: {b}")

# Tuple methods
print("\n=== Tuple Methods ===")
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Numbers: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

# Immutability demonstration
print("\n=== Immutability ===")
print("Tuples are immutable - you cannot change their elements")
print("Uncommenting the line below would cause an error:")
print("# colors[0] = 'yellow'  # TypeError: 'tuple' object does not support item assignment")

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print(f"\nNested tuple: {nested}")
print(f"Element at [1][0]: {nested[1][0]}")

# Converting between list and tuple
print("\n=== Conversions ===")
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(f"List to tuple: {my_tuple}")

back_to_list = list(my_tuple)
print(f"Tuple to list: {back_to_list}")
