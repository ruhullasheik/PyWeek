"""Hints for ex_03

    n = int(input("Enter odd number: "))

    # Top half (including middle)
    for i in range(1, n + 1, 2):
        spaces = (n - i) // 2
        print(" " * spaces + "*" * i)

    # Bottom half
    for i in range(n - 2, 0, -2):
        spaces = (n - i) // 2
        print(" " * spaces + "*" * i)
"""
