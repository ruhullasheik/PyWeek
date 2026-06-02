"""Hints for ex_01

    import re
    from collections import Counter

    text = "The quick brown fox jumps over the lazy dog. The dog sleeps."
    words = re.findall(r"\w+", text.lower())
    freq = Counter(words)

    for word, count in freq.most_common():
        print(f"{word}: {count}")
"""
