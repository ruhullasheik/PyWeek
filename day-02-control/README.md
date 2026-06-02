# Day 02 — Control Flow

**Estimated time**: 4–5 hours  
**Practice required**: Yes — exercises are mandatory

## Learning Objectives

- Write idiomatic `for` loops (Python style, not C style)
- Use `range()`, `enumerate()`, `zip()` effectively
- Write `if`/`elif`/`else` chains with truthiness
- Use `match`/`case` (Python 3.10+)
- Understand `break`, `continue`, `else` on loops

## Key Python Concepts

| You Know (C/Java) | Do This In Python |
|---|---|
| `for (int i=0; i<n; i++)` | `for i in range(n):` |
| `for (int x : arr)` | `for x in arr:` |
| `if (x > 0 && y < 10)` | `if x > 0 and y < 10:` |
| `switch (x) { case 1: ... }` | `match x: case 1: ...` |
| `do { ... } while (x)` | No do-while. Use `while True: ... if cond: break` |
