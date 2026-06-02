"""Example 3: Closure

A function that remembers its enclosing scope.
"""

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

c1 = make_counter()
print(c1())  # 1
print(c1())  # 2
print(c1())  # 3

c2 = make_counter()
print(c2())  # 1 (independent state)
