"""Exercise 5: Flatten and Map

Write two functions:

1. flatten(nested) — takes a nested list and flattens it one level
   flatten([[1,2], [3,4,5], [6]]) -> [1,2,3,4,5,6]

2. flatten_map(func, nested) — applies func to each element, then flattens
   flatten_map(lambda x: x*2, [[1,2], [3]]) -> [2,4,6]

Hint: sum(list, []) or a list comprehension.
"""
