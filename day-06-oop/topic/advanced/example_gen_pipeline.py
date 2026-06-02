"""Advanced Example 1: Generator Pipeline

Chaining generators for a data processing pipeline.
"""

def read_lines(filename):
    """Generator that yields lines from a file."""
    with open(filename) as f:
        for line in f:
            yield line.strip()


def filter_comments(lines):
    """Generator that removes comment lines."""
    for line in lines:
        if not line.startswith("#"):
            yield line


def split_words(lines):
    """Generator that splits lines into words."""
    for line in lines:
        yield from line.split()


def lowercase(words):
    """Generator that lowercases words."""
    for word in words:
        yield word.lower()


# Pipeline — nothing executes until we iterate
words = lowercase(split_words(filter_comments(read_lines("example.txt"))))
for word in words:
    print(word)
