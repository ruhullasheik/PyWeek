"""Example 1: Higher-Order Functions

Functions that take or return other functions.
"""

def apply_twice(f, value):
    """Apply a function f twice to value."""
    return f(f(value))

def add_one(x):
    return x + 1

result = apply_twice(add_one, 5)
print(f"apply_twice(add_one, 5) = {result}")  # 7

# Lambda version
result = apply_twice(lambda x: x * 2, 5)
print(f"apply_twice(lambda x: x*2, 5) = {result}")  # 20

# map, filter with lambda
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"squares: {squares}")
print(f"evens: {evens}")
