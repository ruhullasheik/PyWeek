"""Example 4: Match/Case (Python 3.10+)

Pattern matching — more powerful than a switch statement.
"""

def handle_command(cmd):
    match cmd.split():
        case ["quit"]:
            print("Goodbye!")
            return False
        case ["hello", name]:
            print(f"Hello, {name}!")
        case ["add", *nums]:
            total = sum(int(n) for n in nums)
            print(f"Sum = {total}")
        case ["repeat", count, *words]:
            for _ in range(int(count)):
                print(" ".join(words))
        case _:
            print(f"Unknown command: {cmd}")
    return True

# Try it
commands = ["hello world", "add 1 2 3 4 5", "repeat 3 go", "quit"]
for cmd in commands:
    if not handle_command(cmd):
        break
