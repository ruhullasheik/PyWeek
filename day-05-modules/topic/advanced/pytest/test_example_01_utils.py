"""Tests for example_01_utils.py

These tests demonstrate different pytest features.
"""

import pytest
from .example_01_utils import add, is_even, factorial, reverse_words


def test_add_positive():
    result = add(3, 5)
    assert result == 8


def test_add_negative():
    assert add(-1, 1) == 0
    assert add(-5, -3) == -8


def test_add_zero():
    assert add(0, 0) == 0
    assert add(7, 0) == 7
    assert add(0, 7) == 7


@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, False),
    (0, True),
    (100, True),
    (101, False),
])
def test_is_even(n, expected):
    assert is_even(n) == expected


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_factorial_negative():
    with pytest.raises(ValueError, match="non-negative"):
        factorial(-1)


def test_reverse_words():
    result = reverse_words("hello world")
    assert result == "world hello"


def test_reverse_words_single():
    assert reverse_words("python") == "python"


def test_reverse_words_empty():
    assert reverse_words("") == ""


def test_reverse_words_multiple():
    assert reverse_words("a b c d") == "d c b a"
