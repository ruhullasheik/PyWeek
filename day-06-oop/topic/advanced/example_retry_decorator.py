"""Advanced Example 2: Parametrized Decorator

A decorator with configurable behavior.
"""

import time
from functools import wraps


def retry(max_attempts=3, delay=1):
    """Retry a function if it raises an exception."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
                    time.sleep(delay)
            return None

        return wrapper
    return decorator


@retry(max_attempts=3, delay=0.5)
def unreliable_network_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network timeout")
    return "Success!"


print(unreliable_network_call())
