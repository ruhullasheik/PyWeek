# Primer: Functions

## Defining Functions

```python
def greet(name):
    return f"Hello, {name}!"

# No type annotations needed (but you can add them)
def add(a: int, b: int) -> int:
    return a + b
```

## Default Arguments

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))                 # Hello, Alice!
print(greet("Bob", "Hi"))             # Hi, Bob!
print(greet("Charlie", greeting="Yo"))  # Yo, Charlie!
```

### ⚠️ Mutable Default Argument Pitfall

```python
# DON'T do this
def add_item(item, lst=[]):  # The list is created ONCE, at function definition
    lst.append(item)
    return lst

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b']  — surprise!

# DO this instead
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

## Keyword Arguments

```python
def create_user(name, age, role="user"):
    print(f"{name}, {age}, {role}")

# Positional
create_user("Alice", 25, "admin")

# Keyword (order doesn't matter)
create_user(age=30, name="Bob")

# Mixed (positional first, then keyword)
create_user("Charlie", age=22)
```

## *args and **kwargs

```python
# *args — any number of positional args (packed as tuple)
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10

# **kwargs — any number of keyword args (packed as dict)
def print_config(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_config(host="localhost", port=8080, debug=True)
```

## Lambda (Anonymous Functions)

```python
# Lambda is a one-liner function
square = lambda x: x ** 2
print(square(5))  # 25

# Most useful with sorted(), map(), filter()
pairs = [(1, "z"), (3, "a"), (2, "c")]
sorted_pairs = sorted(pairs, key=lambda p: p[1])  # sort by second element
print(sorted_pairs)  # [(3, 'a'), (2, 'c'), (1, 'z')]
```

## Scope (LEGB Rule)

Python looks up variables in this order:

1. **L**ocal — inside the current function
2. **E**nclosing — outer functions (nested functions)
3. **G**lobal — module level
4. **B**uilt-in — Python's built-in names (`print`, `len`, etc.)

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()
    print(x)

outer()
print(x)

# Output:
# local
# enclosing
# global
```

## Docstrings

```python
def factorial(n):
    """Return the factorial of n.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n (n!).
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# View docstring
print(factorial.__doc__)
help(factorial)
```
