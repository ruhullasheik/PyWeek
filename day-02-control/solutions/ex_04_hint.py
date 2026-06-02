"""Hints for ex_04

    msg = input("Message: ")
    shift = int(input("Shift: "))

    result = []
    for ch in msg:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)

    print("".join(result))

    # Alternative with str.translate:
    # import string; ...
"""
