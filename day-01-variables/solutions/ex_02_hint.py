"""Hints for ex_02

    values = [42, "hello", [1,2], (3,4), {"a":1}, {1,2}, True, None, 3.14]

    for v in values:
        t = type(v).__name__
        # Check mutability — see the Mutability Cheatsheet table in the primer
        # Quick ref: list, dict, set are mutable; str, int, float, bool, tuple, NoneType are not
        mutable_types = {"list", "dict", "set"}
        m = "mutable" if t in mutable_types else "immutable"
        print(f"{v!r:10} -> {t:15} ({m})")
"""
