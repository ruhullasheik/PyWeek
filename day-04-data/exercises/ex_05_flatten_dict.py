"""Exercise 5: JSON Flatten

Given a nested dict, flatten it into a single-level dict
where keys are dot-separated paths.

nested = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3
        }
    },
    "f": [4, 5]
}

Output:
    {"a": 1, "b.c": 2, "b.d.e": 3, "f.0": 4, "f.1": 5}

Hint: recursion + isinstance(x, dict)
"""
