"""Example 3: Set Operations

Set theory in action.
"""

python = {"Alice", "Bob", "Charlie", "Diana"}
java = {"Bob", "Eve", "Frank", "Charlie"}

both = python & java
either = python | java
only_python = python - java
only_java = java - python
exclusive = python ^ java

print(f"Python club: {python}")
print(f"Java club: {java}")
print(f"Both: {both}")
print(f"Either: {either}")
print(f"Only Python: {only_python}")
print(f"Only Java: {only_java}")
print(f"Exactly one: {exclusive}")

# Check subset
print(f"Python superset of Both: {python.issuperset(both)}")
print(f"Both subset of Java: {both.issubset(java)}")
