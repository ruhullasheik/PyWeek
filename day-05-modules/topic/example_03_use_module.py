"""Example 3: Using a Module

Run after looking at example_02_my_module.py.
"""

# Import our module
from topic.example_02_my_module import greet, add, MESSAGE

print(f"Message from module: {MESSAGE}")
print(greet("Bob"))
print(f"10 + 20 = {add(10, 20)}")

# Show that __name__ is NOT '__main__' when imported
import topic.example_02_my_module as mymod

# The import above already ran the module's code, printing the else branch
