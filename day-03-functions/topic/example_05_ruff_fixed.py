"""Example 5: Ruff Fix Demo

Now run: ruff check day-03-functions/topic/example_04_ruff_demo.py --fix
And see this cleaned up.

Then try: ruff format day-03-functions/topic/example_04_ruff_demo.py
"""

def is_large(x):
    """Returns True if x > 10."""
    return x > 10

y = is_large(5)
print(y)
