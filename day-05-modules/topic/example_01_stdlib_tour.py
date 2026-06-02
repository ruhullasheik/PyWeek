"""Example 1: Standard Library Tour

A quick tour of useful stdlib modules.
"""

import os
import sys
import json
import datetime
import random
import pathlib
import statistics

# os — operating system
print(f"Current dir: {os.getcwd()}")
print(f"User: {os.environ.get('USER', os.environ.get('USERNAME', 'unknown'))}")

# sys — interpreter
print(f"Python: {sys.version}")
print(f"Args: {sys.argv}")

# datetime
today = datetime.date.today()
print(f"Today: {today}")
print(f"Next week: {today + datetime.timedelta(days=7)}")

# random
print(f"Random 1-10: {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['apple', 'banana', 'cherry'])}")

# json
data = {"name": "PyWeek", "days": 7, "topics": ["tools", "variables", "control"]}
print(f"JSON: {json.dumps(data, indent=2)}")

# statistics
nums = [random.randint(1, 100) for _ in range(20)]
print(f"Mean: {statistics.mean(nums):.1f}, Median: {statistics.median(nums)}")

# pathlib (modern path handling)
p = pathlib.Path(".")
for f in p.glob("*.py"):
    print(f"Python file: {f}")
