"""Example 2: Truthiness

Run this to see what's truthy and what's falsy.
"""

values = [True, False, None, 0, 1, -1, 0.0, 3.14, "", "hello", [], [1], {}, {"a": 1}, set(), (1,)]

for v in values:
    if v:
        print(f"  TRUTHY: {v!r}")
    else:
        print(f"  FALSY:  {v!r}")
