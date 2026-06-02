"""Example 2: Creating and Using a Module

Run this as: python day-05-modules/topic/example_02_my_module.py

It will import itself as a module (silly but demonstrates the concept).
"""

MESSAGE = "Hello from my_module!"


def greet(name):
    return f"{MESSAGE} Nice to meet you, {name}."


def add(a, b):
    return a + b


if __name__ == "__main__":
    # This only runs when executed directly
    print("Running as a script...")
    print(greet("Alice"))
    print(f"5 + 3 = {add(5, 3)}")
else:
    # This runs when imported
    print(f"'my_module' imported — __name__ is '{__name__}'")
