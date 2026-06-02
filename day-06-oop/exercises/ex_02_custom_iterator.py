"""Exercise 2: Custom Iterator

Implement a class Range that works like Python's range() but with __iter__ and __next__.

Range(5)     -> 0, 1, 2, 3, 4
Range(2, 6)   -> 2, 3, 4, 5
Range(1, 10, 2) -> 1, 3, 5, 7, 9
Range(10, 0, -2) -> 10, 8, 6, 4, 2

Implement it so it works with:
    for x in Range(5):
        print(x)
    list(Range(2, 6))
"""
