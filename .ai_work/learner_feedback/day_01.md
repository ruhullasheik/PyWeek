# Day 01 — Variables & Types

**How was the day?**
Finally writing actual Python! The type detective and mutable/immutable examples were really good — I finally understand why Python doesn't have `++`. The f-string example was a highlight, I can see myself using this everywhere. Exercises were fair, currency converter was straightforward.

**What's good?**
- The "You Know (C/Java) — Here's What's Different" table in the primer is perfect. That's exactly what I needed.
- F-string examples are practical — the formatting cheatsheet with alignment (`:<10`, `:^10`, `:>10`) was super useful
- Mutable vs immutable with `id()` makes it visual and memorable
- 5 exercises with clear progression — easy to hard

**What can be improved?**
- The primer is a bit long. Could cut the comparison table in half — I don't need both C and Java side by side, just the Python way.
- Exercise 4 (string replicator) uses `[::-1]` which isn't explained until day-04 (slicing). Had to peek at the hint to figure that out. Either move it to day-04 or add a note saying "you'll learn slicing later, for now just use a loop."
- The type checker exercise (ex_02) asks to check mutability — the hint mentions `mutable_types = {"list", "dict", "set"}` as a magic list. Would be better if the primer had a table showing which types are mutable.

**What I struggled with:**
- `id()` and object identity — took me a couple of runs of the example to understand why ints get new ids but lists don't. Maybe add a quick sentence: "immutable = can't change in place = new object = new id."
- String replication with `[::-1]` — not explained yet. Minor frustration.

**What clicked easily:**
- Dynamic typing — coming from C where I declare types, Python feels freeing
- F-strings — instant favorite feature
- The currency converter exercise — practical, immediately useful

**As a B.Tech student, I'd say:**
> "I wrote real Python today. F-strings are life-changing. Why doesn't C have this?"

**Confidence after this day:** Medium (still wrapping my head around immutability)

**Time spent:** ~3 hours
