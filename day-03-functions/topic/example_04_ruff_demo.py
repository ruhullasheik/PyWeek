"""Example 4: Ruff Lint Demo

This file has deliberate style issues.
Run: ruff check day-03-functions/topic/example_04_ruff_demo.py

"""

def bad_naming  (  x ) :
    """Bad spacing and naming"""
    if x>10:
        return True
    else:
        return False

y=bad_naming( 5 )
print( y )
