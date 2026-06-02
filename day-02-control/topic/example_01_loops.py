"""Example 1: Different Loop Styles

Compare C-style vs Pythonic loops.
"""

items = ["Python", "Java", "C++", "Rust"]

# C-style (avoid this)
print("C-style:")
for i in range(len(items)):
    print(f"  {i}: {items[i]}")

# Pythonic
print("Pythonic:")
for i, item in enumerate(items):
    print(f"  {i}: {item}")

# Backwards
print("Reversed:")
for item in reversed(items):
    print(f"  {item}")

# Multiple lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print("Zipped:")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")
