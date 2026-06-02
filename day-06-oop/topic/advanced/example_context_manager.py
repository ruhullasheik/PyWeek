"""Advanced Example 3: Custom Context Manager

Two ways to write a context manager.
"""

from contextlib import contextmanager


# Class-based
class Timer:
    """Context manager that times a block of code."""

    def __init__(self, name="block"):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"{self.name} took {elapsed:.4f}s")


# Generator-based (simpler)
@contextmanager
def timer(name="block"):
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name} took {elapsed:.4f}s")


import time

# Usage
with Timer("sleep"):
    time.sleep(0.5)

with timer("sleep again"):
    time.sleep(0.3)
