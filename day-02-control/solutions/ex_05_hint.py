"""Hints for ex_05

    while True:
        line = input("Enter first number: ")
        if line == "":
            print("Goodbye!")
            break
        try:
            a = float(line)
            b = float(input("Enter second number: "))
            result = a / b
            print(f"Result: {result}")
        except ValueError:
            print("Please enter numbers only")
        except ZeroDivisionError:
            print("Cannot divide by zero")

Tip: catching specific exceptions (ValueError, ZeroDivisionError)
is better than a bare except — it won't hide bugs.
"""