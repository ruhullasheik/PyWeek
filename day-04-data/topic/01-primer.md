# Primer: Data Structures

## List Comprehensions (The Killer Feature)

```python
# Instead of:
squares = []
for i in range(10):
    squares.append(i ** 2)

# Do this:
squares = [i ** 2 for i in range(10)]

# With condition
evens = [i for i in range(20) if i % 2 == 0]

# Nested loop
pairs = [(x, y) for x in range(3) for y in range(3)]

# Dict comprehension
square_dict = {i: i ** 2 for i in range(5)}
```

## Slicing

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst[2:5]     # [2, 3, 4]        — start:end (end exclusive)
lst[:4]      # [0, 1, 2, 3]     — from beginning
lst[6:]      # [6, 7, 8, 9]     — to end
lst[-3:]     # [7, 8, 9]        — last 3
lst[::2]     # [0, 2, 4, 6, 8]  — every other
lst[::-1]    # [9, 8, 7, ...]   — reversed

# Strings work too
"hello"[::-1]  # "olleh"
```

## Lists vs Tuples

```python
# List — mutable
lst = [1, 2, 3]
lst.append(4)
lst[0] = 99

# Tuple — immutable (use for fixed data, dict keys)
tup = (1, 2, 3)
# tup[0] = 99  # TypeError
```

## Dict Operations

```python
d = {"a": 1, "b": 2}

# Access
d["a"]            # 1
d.get("c", 0)     # 0 (safe access with default)

# Check key
"a" in d          # True

# Iteration
for key in d:
for key, val in d.items():
for val in d.values():

# Default dict
from collections import defaultdict
counts = defaultdict(int)  # int() returns 0
counts["a"] += 1           # no KeyError!

# Counter
from collections import Counter
c = Counter("hello world")
print(c.most_common(3))    # [('l', 3), ('o', 2), ('h', 1)]
```

## Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b  # union:     {1,2,3,4,5,6}
a & b  # intersect: {3,4}
a - b  # difference: {1,2}
a ^ b  # symmetric:  {1,2,5,6}
```
