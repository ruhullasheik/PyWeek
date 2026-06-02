# Hints for ex_05

# pyweek_utils/__init__.py
"""
from .strings import reverse, count_vowels, is_palindrome
from .numbers import is_prime, gcd, factorial
"""

# pyweek_utils/strings.py
"""
def reverse(s): return s[::-1]

def count_vowels(s): return sum(1 for c in s.lower() if c in "aeiou")

def is_palindrome(s): return s == s[::-1]
"""

# pyweek_utils/numbers.py
"""
def is_prime(n):
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1
"""
