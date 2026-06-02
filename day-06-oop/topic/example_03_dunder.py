"""Example 3: Dunder Methods

Implementing operator overloading with dunder methods.
"""

from math import sqrt


class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(f"v1 + v2 = {v1 + v2}")
print(f"v2 - v1 = {v2 - v1}")
print(f"v1 * 3  = {v1 * 3}")
print(f"|v1|    = {abs(v1):.2f}")
print(f"v1 == v1: {v1 == v1}")
print(f"v1 == v2: {v1 == v2}")
