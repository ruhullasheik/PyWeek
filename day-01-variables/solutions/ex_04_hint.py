"""Hints for ex_04

    word = input("Enter word: ")
    count = int(input("Enter count: "))

    print((word + " ") * count)       # separated by spaces
    print(word * count)               # no separator
    print(word[::-1])                 # reversed (slicing trick)

Note: [::-1] is a stride slice technique covered in Day 04 (Data).
If it feels unfamiliar, just use a loop to reverse for now.
"""
