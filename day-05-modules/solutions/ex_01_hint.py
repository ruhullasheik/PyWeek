"""Hints for ex_01

    import random
    import string
    import sys

    length = int(sys.argv[1]) if len(sys.argv) > 1 else 12

    # Ensure at least one of each category
    chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%&*"),
    ]

    # Fill the rest randomly
    all_chars = string.ascii_letters + string.digits + "!@#$%&*"
    chars += [random.choice(all_chars) for _ in range(length - 4)]

    random.shuffle(chars)
    print("".join(chars))
"""
