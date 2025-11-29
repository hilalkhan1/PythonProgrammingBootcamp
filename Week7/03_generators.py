"""
Week 7: Generators Examples
Topics: yield, generator expressions
"""

# Generator function
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("Fibonacci numbers:")
for num in fibonacci(10):
    print(num, end=" ")
print()

# Generator expression
squares = (x**2 for x in range(10))
print(f"First 5 squares: {list(squares)[:5]}")

# Memory efficient file reading
def read_large_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()
