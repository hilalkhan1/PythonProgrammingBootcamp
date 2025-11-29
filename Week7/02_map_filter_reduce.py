"""
Week 7: map, filter, reduce Examples
"""

from functools import reduce

# map() - apply function to all items
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")

# filter() - filter items based on condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# reduce() - reduce to single value
sum_all = reduce(lambda x, y: x + y, numbers)
print(f"Sum: {sum_all}")

product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")
