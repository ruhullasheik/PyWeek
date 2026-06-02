"""Hints for ex_02

    import random
    target = random.randint(1, 100)
    attempts = 0

    while attempts < 7:
        guess = int(input("Guess: "))
        attempts += 1
        if guess < target:
            print("Too low")
        elif guess > target:
            print("Too high")
        else:
            print(f"You got it in {attempts} attempts!")
            break
    else:
        print(f"Out of attempts. The number was {target}")
"""
