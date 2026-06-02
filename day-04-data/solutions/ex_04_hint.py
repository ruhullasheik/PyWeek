"""Hints for ex_04

    from collections import Counter

    class Cart:
        def __init__(self):
            self.items = Counter()

        def add(self, item, count=1):
            self.items[item] += count

        def remove(self, item, count=1):
            self.items[item] -= count
            if self.items[item] <= 0:
                del self.items[item]

        def show(self):
            for item, count in self.items.most_common():
                print(f"{item}: {count}")
"""
