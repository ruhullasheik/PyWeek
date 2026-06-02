"""Exercise: Write Tests for Previous Days

Pick functions from days 01–04 and write pytest tests for them.

## Task 1 — Test a function from day-02

Take the prime checker from `day-02-control/topic/example_03_prime_checker.py`.
Write tests for `is_prime()` covering:
- Prime numbers (2, 3, 17, 97)
- Non-prime numbers (0, 1, 4, 15, 100)
- Negative numbers (should return False)
- Large prime (997)

## Task 2 — Test the Currency Converter logic from day-01

Write the conversion logic as a function and test it:

```python
def convert_currency(usd, rate=0.92):
    return round(usd * rate, 2)
```

Test:
- Basic conversion (100 USD @ 0.92 → 92.00)
- Zero USD → 0.00
- Large amount
- Rounding behavior

## Task 3 — Test a data structure from day-04

Take the anagram grouper logic from `day-04-data/exercises/ex_03_anagrams.py`.
Test:
- Basic anagram detection (listen, silent)
- No anagrams in list → each word in its own group
- Empty list → empty result
- Single word → single group

## Task 4 — Parametrize it

Convert at least one test above to use `@pytest.mark.parametrize`.
"""
