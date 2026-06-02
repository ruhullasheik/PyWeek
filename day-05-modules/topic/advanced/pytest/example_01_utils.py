"""Example 1: Basic pytest — Testing a Utility Module

Run: uv run pytest day-05-modules/topic/advanced/pytest/
"""


def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])
