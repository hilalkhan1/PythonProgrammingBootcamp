"""
Week 3: Recursion Examples
Topics: Recursive functions
"""

# Simple recursion - countdown
def countdown(n):
    """Recursively count down from n to 0"""
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)

print("=== Countdown ===")
countdown(5)

# Factorial using recursion
def factorial(n):
    """
    Calculate factorial recursively
    n! = n * (n-1) * (n-2) * ... * 1
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("\n=== Factorial ===")
print(f"5! = {factorial(5)}")
print(f"7! = {factorial(7)}")

# Fibonacci sequence
def fibonacci(n):
    """
    Calculate nth Fibonacci number recursively
    F(n) = F(n-1) + F(n-2)
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("\n=== Fibonacci ===")
print("First 10 Fibonacci numbers:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# Sum of list using recursion
def sum_list(numbers):
    """Calculate sum of list recursively"""
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

print("\n=== Sum of List ===")
numbers = [1, 2, 3, 4, 5]
print(f"Sum of {numbers}: {sum_list(numbers)}")

# Power function using recursion
def power(base, exponent):
    """Calculate base^exponent recursively"""
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

print("\n=== Power Function ===")
print(f"2^5 = {power(2, 5)}")
print(f"3^4 = {power(3, 4)}")

# Greatest Common Divisor (GCD)
def gcd(a, b):
    """Calculate GCD using Euclidean algorithm (recursive)"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print("\n=== GCD ===")
print(f"GCD(48, 18) = {gcd(48, 18)}")
print(f"GCD(100, 35) = {gcd(100, 35)}")
