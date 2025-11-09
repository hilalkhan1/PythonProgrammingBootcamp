"""
Week 1: Loops Examples
Topics: for loop, while loop, break, continue
"""

# For loop with range
print("=== For Loop ===")
for i in range(5):
    print(f"Iteration {i}")

# For loop with start and end
print("\n=== For Loop with Range ===")
for num in range(1, 6):
    print(f"Number: {num}")

# For loop with step
print("\n=== For Loop with Step ===")
for num in range(0, 11, 2):
    print(f"Even number: {num}")

# While loop
print("\n=== While Loop ===")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Break statement
print("\n=== Break Statement ===")
for i in range(10):
    if i == 5:
        print(f"Breaking at {i}")
        break
    print(i)

# Continue statement
print("\n=== Continue Statement ===")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")

# Nested loops
print("\n=== Nested Loops ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
