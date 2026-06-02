"""Hints for ex_03

    import time

    def time_this(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            print(f"{func.__name__} took {elapsed:.4f}s")
            return result
        return wrapper

    @time_this
    def slow_op():
        return sum(range(10_000_000))

    slow_op()
"""
