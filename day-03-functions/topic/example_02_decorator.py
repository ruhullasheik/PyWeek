"""Example 2: Decorator Pattern

A decorator wraps a function to add behavior.
"""

def timer(func):
    """Decorator that prints how long a function takes."""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

result = slow_sum(10_000_000)
print(f"result = {result}")

# Equivalent without @ syntax:
# slow_sum = timer(slow_sum)
