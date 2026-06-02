"""Hints for the testing exercise.

These are test skeletons — fill in the logic.
"""

import pytest

# ------------------------------------------------------------------
# Task 1: Test is_prime
# ------------------------------------------------------------------

# Copy the is_prime function here or import it
# from ... import is_prime


class TestIsPrime:
    def test_prime_numbers(self):
        """2, 3, 5, 7, 11, 13 are prime"""
        # assert is_prime(2)
        # assert is_prime(3)
        ...

    def test_non_prime_numbers(self):
        """0, 1, 4, 6, 8, 9, 10 are not prime"""
        pass

    def test_negative(self):
        """Negative numbers are not prime"""
        pass

    def test_large_prime(self):
        """997 is prime"""
        pass

# ------------------------------------------------------------------
# Task 2: Test currency converter
# ------------------------------------------------------------------

def convert_currency(usd, rate=0.92):
    return round(usd * rate, 2)


class TestCurrencyConverter:
    def test_basic(self):
        # assert convert_currency(100) == 92.00
        pass

    def test_zero(self):
        pass

    def test_custom_rate(self):
        # assert convert_currency(100, 1.0) == 100.0
        pass

# ------------------------------------------------------------------
# Task 3: Test anagram grouper
# ------------------------------------------------------------------

def group_anagrams(words):
    """Return list of groups where each group is a list of anagrams."""
    from collections import defaultdict
    groups = defaultdict(list)
    for w in words:
        key = tuple(sorted(w))
        groups[key].append(w)
    return list(groups.values())


class TestAnagramGrouper:
    def test_basic(self):
        # result = group_anagrams(["listen", "silent", "enlist"])
        # assert ["listen", "silent", "enlist"] in result
        pass

    def test_no_anagrams(self):
        pass

    def test_empty(self):
        pass

    def test_single_word(self):
        pass

# ------------------------------------------------------------------
# Task 4: Parametrize one test
# ------------------------------------------------------------------
# @pytest.mark.parametrize("n, expected", [
#     (2, True),
#     (3, True),
#     (4, False),
#     (9, False),
# ])
# def test_is_prime_parametrized(n, expected):
#     assert is_prime(n) == expected
