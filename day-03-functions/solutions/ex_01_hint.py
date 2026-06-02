"""Hints for ex_01

words = ["banana", "apple", "cherry", "date", "elderberry", "fig"]

# Key returns a tuple — first sort by length, then alphabetically
sorted_words = sorted(words, key=lambda w: (len(w), w))
print(sorted_words)
# Expected: ['date', 'fig', 'apple', 'banana', 'cherry', 'elderberry']
"""
