"""Hints for ex_01

    class Item:
        def __init__(self, title, year):
            self.title = title
            self.year = year
            self.is_checked_out = False

        def check_out(self):
            if self.is_checked_out:
                raise ValueError(f"{self.title} is already checked out")
            self.is_checked_out = True

        def return_item(self):
            self.is_checked_out = False

    class Book(Item):
        def __init__(self, title, year, author, pages):
            super().__init__(title, year)
            self.author = author
            self.pages = pages

        def __str__(self):
            return f"Book: {self.title} by {self.author} ({self.year})"

    class Library:
        def __init__(self):
            self.items = []

        def add(self, item):
            self.items.append(item)

        def search(self, query):
            query = query.lower()
            return [i for i in self.items if query in i.title.lower()]
"""
