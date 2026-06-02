"""Example 3: Prime Checker with Loop Else

The `else` on a for loop runs only if the loop didn't break.
This is great for search-style loops.
"""

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            print(f"  {n} is divisible by {d}")
            break
    else:
        # This runs if we never hit break — meaning no divisor found
        return True
    return False

for num in [2, 3, 4, 5, 9, 11, 15, 17, 25, 29]:
    result = is_prime(num)
    print(f"  {num}: prime={result}")
