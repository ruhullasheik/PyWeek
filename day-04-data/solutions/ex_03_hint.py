"""Hints for ex_03

    from collections import defaultdict

    words = ["listen", "silent", "enlist", "hello", "world", "dlrow", "olelh"]
    groups = defaultdict(list)

    for w in words:
        key = tuple(sorted(w))
        groups[key].append(w)

    print(list(groups.values()))
"""
