"""Hints for ex_05

    from math import pi, sqrt

    class Shape:
        def area(self):
            raise NotImplementedError

        def perimeter(self):
            raise NotImplementedError

        def describe(self):
            return f"Shape: {type(self).__name__}, Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self): return pi * self.radius ** 2
        def perimeter(self): return 2 * pi * self.radius

    class Rectangle(Shape):
        def __init__(self, w, h):
            self.w, self.h = w, h

        def area(self): return self.w * self.h
        def perimeter(self): return 2 * (self.w + self.h)

    class Square(Rectangle):
        def __init__(self, side):
            super().__init__(side, side)

    # Triangle with Heron's formula
    # s = (a + b + c) / 2
    # area = sqrt(s * (s-a) * (s-b) * (s-c))
"""
