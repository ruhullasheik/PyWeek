# Primer: Variables & Types

## Dynamic Typing

In C/Java, a variable is a box that holds a specific type. In Python, a variable is a **name tag** you stick on an object.

```python
x = 5          # x points to an int
x = "hello"    # x now points to a string — perfectly legal
x = [1, 2, 3]  # x now points to a list

# Check the type at runtime
print(type(x))  # <class 'list'>
```

This is called **duck typing**: if it walks like a duck and quacks like a duck, it's a duck. You don't care about the type — you care about behavior.

## Basic Types

```python
# Numbers
age = 25               # int (unbounded — no overflow like C)
pi = 3.14159           # float (double-precision)
complex_num = 3 + 4j   # complex (yes, Python has built-in complex numbers)

# Strings
name = "Alice"         # double or single quotes — both fine
greeting = 'Hello'     # pick one and be consistent

# Boolean
is_python_fun = True   # note: capital T, capital F

# None (null)
result = None          # Python's null — singleton, not null pointer
```

## Key Differences From C/Java

### 1. No type declaration
```python
# C:   int x = 10;
# Java: int x = 10;
# Python:
x = 10  # That's it. Python infers the type.
```

### 2. No `++` or `--`
```python
x += 1   # not x++
x -= 1   # not x--
```

### 3. `and` / `or` / `not` (keywords, not symbols)
```python
if x > 0 and x < 10:    # not &&
if x == 0 or y == 0:    # not ||
if not active:           # not !
```

### 4. `None` instead of `null`/`NULL`/`nil`/`NoneType`
```python
result = None
if result is None:       # Use `is` for None comparison
    print("no result")
```

## F-Strings (Best Thing Since Sliced Bread)

```python
name = "Bob"
age = 30

# Old way (like C printf or Java String.format)
print("Hello %s, you are %d years old" % (name, age))

# Better way (.format)
print("Hello {}, you are {} years old".format(name, age))

# Best way (f-strings — Python 3.6+)
print(f"Hello {name}, you are {age} years old")

# Expressions inside f-strings
print(f"Next year you'll be {age + 1}")
print(f"{name.upper()} IS SHOUTING")
```

## Input

```python
name = input("Enter your name: ")   # Always returns a string
age = int(input("Enter your age: "))  # Convert to int
```

## Type Conversion

```python
int("42")          # 42
float("3.14")      # 3.14
str(100)           # "100"
bool(1)            # True, bool(0) -> False
bool("")           # False (empty string is falsy)
bool("hello")      # True (non-empty string is truthy)
```

## Mutability Cheatsheet

| Type | Mutable? | Notes |
|---|---|---|
| `int` | ❌ | Immutable — `x += 1` creates a new int |
| `float` | ❌ | Immutable |
| `str` | ❌ | Immutable — `s.upper()` returns a new string |
| `bool` | ❌ | Immutable |
| `list` | ✅ | Mutable — `lst.append(1)` changes in place |
| `dict` | ✅ | Mutable |
| `tuple` | ❌ | Immutable — like a frozen list |
| `set` | ✅ | Mutable |
