"""Hints for ex_02

    cache = {}

    def fib(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    # Or use a closure to hide the cache
    # Or use functools.lru_cache (but implement manually for practice)
"""
