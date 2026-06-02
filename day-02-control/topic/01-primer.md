# Primer: Control Flow

## Truthiness (This Will Trip You Up)

In Python, values are *truthy* or *falsy*. The following are **always falsy**:

```python
False, None, 0, 0.0, "", [], (), {}, set()
```

Everything else is truthy.

```python
if "":          # False — empty string
if "hello":     # True — non-empty string
if 0:           # False
if 42:          # True
if []:          # False
if [1, 2]:      # True
```

## Conditionals

```python
# Python uses 'and', 'or', 'not' — NOT &&, ||, !
if x > 0 and x < 10:
    print("single digit")

if not active:
    print("inactive")

# elif — not 'else if'
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

## For Loops — Python Style

**Forget C-style `for (int i=0; i<n; i++)`. Python `for` is a for-each.**

```python
# Iterate over items
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate with index using range(len()) — DON'T do this
for i in range(len(fruits)):        # Works but not Pythonic
    print(fruits[i])

# Instead, use enumerate()
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# range(start, stop, step)
for i in range(0, 10, 2):           # 0, 2, 4, 6, 8
    print(i)

for i in range(5, 0, -1):           # 5, 4, 3, 2, 1
    print(i)
```

## While Loops

```python
# Standard while
count = 0
while count < 5:
    print(count)
    count += 1

# No do-while — use this pattern instead
while True:
    response = input("Continue? (y/n): ")
    if response.lower() == "n":
        break
    print("Continuing...")
```

## Break, Continue, and Loop Else

```python
# break — exit loop
for n in range(100):
    if n > 10:
        break

# continue — skip to next iteration
for n in range(10):
    if n % 2 == 0:
        continue
    print(n)  # only odd numbers

# else on loops — runs ONLY if loop completed without break
for n in range(2, 10):
    for d in range(2, n):
        if n % d == 0:
            break
    else:
        print(f"{n} is prime")  # runs only if inner loop didn't break
```

## Match/Case (Python 3.10+)

Python's `match` is more powerful than C's `switch`. It supports pattern matching.

```python
def describe(value):
    match value:
        case 0:
            print("zero")
        case 1 | 2 | 3:
            print("small")
        case int() as n if n > 100:
            print("big number")
        case str() as s:
            print(f"string of length {len(s)}")
        case _:
            print("something else")
```
