"""Example 2: Mutable vs Immutable

This demonstrates the difference.
"""

# Immutable: x points to 10, then points to 11 (new object)
x = 10
print(f"x = {x}, id = {id(x)}")
x += 1
print(f"x = {x}, id = {id(x)}")  # Different id — new object!

# Mutable: lst changes in place
lst = [1, 2, 3]
print(f"lst = {lst}, id = {id(lst)}")
lst.append(4)
print(f"lst = {lst}, id = {id(lst)}")  # Same id — modified in place!

# String: looks like you're modifying, but you're not
s = "hello"
print(f"s = {s}, id = {id(s)}")
s = s.upper()
print(f"s = {s}, id = {id(s)}")  # Different id — new string!
