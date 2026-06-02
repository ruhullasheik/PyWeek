# Primer: Classes & Objects

In Python, **everything is an object**. Even functions, modules, and classes themselves.

## Basic Class

```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, age):
        self.name = name    # Instance attribute
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"

    # String representation
    def __str__(self):
        return f"{self.name} ({self.age} years)"

    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"


# Usage
d = Dog("Rex", 3)
print(d.bark())       # Rex says woof!
print(d.species)       # Canis familiaris
print(str(d))          # Rex (3 years)
```

## `self` is explicit

Unlike Java's `this`, Python requires `self` as the first parameter of every instance method. The name `self` is convention (you could call it `this`), but **always use `self`**.

## Dunder (Double Underscore) Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):       # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):      # v * 3
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):        # v1 == v2
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```

## Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"
```

## `@property` — Computed Attributes

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

# Usage
c = Circle(5)
print(c.area)      # No parentheses needed!
c.radius = 10      # Uses setter
# c.radius = -5    # ValueError!
```

## `@staticmethod` vs `@classmethod`

```python
class MathUtils:
    @staticmethod
    def add(a, b):          # No self/cls — just a function in a class
        return a + b

    @classmethod
    def from_string(cls, text):  # Gets the class, not the instance
        return cls()
```

## Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    def distance_from(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

# __init__, __repr__, __eq__ are auto-generated
p1 = Point(1, 2)
p2 = Point(4, 6)
print(p1)                   # Point(x=1, y=2)
print(p1 == Point(1, 2))    # True
```
