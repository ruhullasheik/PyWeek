"""Hints for ex_05

    def flatten(nested):
        # [item for sublist in nested for item in sublist]
        return sum(nested, [])
        # or: [x for sub in nested for x in sub]

    def flatten_map(func, nested):
        # Apply func to each sublist element, then flatten
        return flatten([func(x) for sub in nested for x in sub])

        # Or: [func(x) for sub in nested for x in sub]
"""
