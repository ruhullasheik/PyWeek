# Day 02 — Control Flow

**How was the day?**
Solid day. The `for...else` on prime checker blew my mind — didn't know loops could have an else. Truthiness examples made Python's "falsy" values click immediately. The enumerate/zip comparison is exactly what I needed to stop writing C-style loops.

**What's good?**
- Loop `else` example (prime checker) — brilliant. I'll never forget this pattern.
- Truthiness demo with all the types — running it myself was better than reading about it
- `match/case` with pattern matching is powerful. The command parser example is neat.
- Exercises are fun — FizzBuzz, guessing game, diamond pattern. Practical.

**What can be improved?**
- Caesar cipher exercise mentions `str.maketrans` in the hint but it's not in the primer. Might confuse students who don't peek at hints.
- Matrix multiplication (ex_05) might be too much for day-02. Triple nested loops are hard enough in any language. Maybe move to day-04 as an advanced exercise.

**What I struggled with:**
- `for...else` — initially thought the else runs after the loop always. The prime example clears it up but took two reads.
- Diamond pattern (ex_03) — spacing logic took some trial and error.

**What clicked easily:**
- `enumerate()` — so much better than `range(len(...))`. No more off-by-one errors.
- Truthiness — coming from C where only 0 is false, the Python rules feel natural.
- `match/case` — feels like a better switch. The `_` wildcard is neat.

**As a B.Tech student, I'd say:**
> "for...else is dark magic. I'm going to use it everywhere and confuse my friends."

**Confidence after this day:** High

**Time spent:** ~3.5 hours
