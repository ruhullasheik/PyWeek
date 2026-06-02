# Interview-Style Problems

Python-specific interview problems. Unlike generic LeetCode, these test your Python fluency.

## Problem 1: LRU Cache

Implement an LRU (Least Recently Used) cache with O(1) get() and put().

Use `collections.OrderedDict` for a concise solution, then implement manually with a dict + doubly linked list.

```
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)      # returns 1
cache.put(3, 3)   # evicts key 2
cache.get(2)      # returns -1 (not found)
```

## Problem 2: Word Break

Given a string and a dictionary of words, determine if the string can be segmented.

Use dynamic programming + memoization.

```
word_break("leetcode", ["leet", "code"])  # True
word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])  # False
```

## Problem 3: Top K Frequent Elements

Given a list, return the k most frequent elements.

Use `collections.Counter` and a heap.

```
top_k_frequent([1,1,1,2,2,3], 2)  # [1, 2]
```

## Problem 4: Valid Sudoku

Determine if a 9×9 Sudoku board is valid.

Use sets per row, column, and 3×3 box.

## Problem 5: Design a Task Scheduler

Design a scheduler that runs tasks at specified intervals.

Use `heapq` for priority queue, `datetime` for timing.

## Problem 6: JSON Diff

Given two JSON objects, produce a diff showing what was added, removed, or changed.

Use recursion to traverse nested structures.

```
diff({"a": 1, "b": 2}, {"a": 1, "b": 3, "c": 4})
# Changed: b (2 -> 3)
# Added: c (4)
```
