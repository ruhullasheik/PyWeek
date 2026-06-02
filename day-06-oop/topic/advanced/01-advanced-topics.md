# Advanced: Decorators, Generators, Context Managers

These stretch beyond OOP basics. Work through them if you have time and appetite.

## Decorators (Recap + Parametrized)

```python
# Decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")
```

## Generators

```python
def fibonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

for n in fibonacci(10):
    print(n)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

**Why generators?** They produce values lazily — one at a time, not all at once. Great for infinite sequences or large data.

## Context Managers

```python
# The with statement
with open("file.txt", "r") as f:
    content = f.read()
# File is auto-closed here

# Custom context manager (class-based)
class ManagedFile:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Custom context manager (generator-based)
from contextlib import contextmanager

@contextmanager
def managed_file(name, mode):
    f = open(name, mode)
    try:
        yield f
    finally:
        f.close()
```
