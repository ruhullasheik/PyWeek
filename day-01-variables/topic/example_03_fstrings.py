"""Example 3: F-String Playground

Experiment with f-string formatting.
"""

name = "Python"
year = 1991
version = 3.12
features = ["dynamic typing", "list comprehensions", "f-strings"]

# Basic
print(f"Hello, {name}!")

# Expressions
print(f"{name} was created in {year}, which is {2026 - year} years ago.")

# Method calls
print(f"Uppercase: {name.upper()}")
print(f"Length of name: {len(name)}")

# Format specifiers
pi = 3.1415926535
print(f"Pi to 2 decimals: {pi:.2f}")
print(f"Pi to 4 decimals: {pi:.4f}")

# Alignment
print(f"|{'left':<10}|{'center':^10}|{'right':>10}|")
