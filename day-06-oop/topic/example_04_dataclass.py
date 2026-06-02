"""Example 4: Dataclass Comparison

Compare a manual class vs a dataclass.
"""

from dataclasses import dataclass


# Manual way (lots of boilerplate)
class BookManual:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __eq__(self, other):
        if not isinstance(other, BookManual):
            return NotImplemented
        return self.isbn == other.isbn


# Dataclass way
@dataclass
class Book:
    title: str
    author: str
    year: int
    isbn: str
    checked_out: bool = False  # default


b1 = Book("1984", "Orwell", 1949, "978-0451524935")
b2 = Book("1984", "Orwell", 1949, "978-0451524935")
b3 = Book("Brave New World", "Huxley", 1932, "978-0060850524")

print(f"b1: {b1}")
print(f"b1 == b2: {b1 == b2}")  # True — compares all fields
print(f"b1 == b3: {b1 == b3}")  # False

# Dataclass is also mutable by default
b1.checked_out = True
print(f"b1 checked out: {b1.checked_out}")
