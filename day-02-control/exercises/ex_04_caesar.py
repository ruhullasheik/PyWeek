"""Exercise 4: Caesar Cipher

Implement a Caesar cipher: shift each letter by a fixed number.

- Ask the user for a message and a shift value (integer)
- For each character: if it's a letter, shift it; otherwise leave it
- Preserve case ('a' shifted by 1 -> 'b', 'z' wraps to 'a')
- Print both the original and encrypted message

Example:
    Message: Hello, World!
    Shift: 3
    Encrypted: Khoor, Zruog!

Hint: ord() and chr(), or str.maketrans()
"""
