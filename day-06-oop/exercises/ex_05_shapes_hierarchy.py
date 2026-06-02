"""Exercise 5: Shape Hierarchy

Implement shape classes with polymorphic area/perimeter.

Base class: Shape (abstract)
    - area() -> float
    - perimeter() -> float
    - describe() -> "Shape: Circle, Area: 78.54, Perimeter: 31.42"

Subclasses:
    - Circle(radius)
    - Rectangle(width, height)
    - Triangle(a, b, c)  (three sides, use Heron's formula)
    - Square(side)  (bonus: inherits from Rectangle)

Create a list of shapes, loop through and describe each one.

Extension: Add a @classmethod from_description that creates shapes
from a string like "circle radius=5".
"""
