"""Example 1: List Comprehension Variations

See the different forms.
"""

numbers = range(1, 21)

# Basic
squares = [n ** 2 for n in numbers]
print(f"squares: {squares[:10]}...")

# With condition
evens = [n for n in numbers if n % 2 == 0]
print(f"evens: {evens}")

# Ternary in comprehension
labels = ["even" if n % 2 == 0 else "odd" for n in range(1, 11)]
print(f"labels: {labels}")

# Flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(f"flattened: {flat}")
