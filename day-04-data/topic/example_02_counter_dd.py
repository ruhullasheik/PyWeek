"""Example 2: Counter and DefaultDict

Useful utilities from collections.
"""

from collections import Counter, defaultdict

# Word frequency
text = "python is great and python is fun and python is powerful"
words = text.split()
freq = Counter(words)
print("Most common:")
for word, count in freq.most_common(3):
    print(f"  {word}: {count}")

# Grouping with defaultdict
students = [
    ("Alice", "CS"), ("Bob", "EE"), ("Charlie", "CS"),
    ("Diana", "ME"), ("Eve", "EE"), ("Frank", "CS"),
]

dept_students = defaultdict(list)
for name, dept in students:
    dept_students[dept].append(name)

print("\nBy department:")
for dept, names in sorted(dept_students.items()):
    print(f"  {dept}: {', '.join(names)}")
