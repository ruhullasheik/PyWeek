# Primer: Modules & Packages

## Import Basics

```python
# Option 1: import the module (use module.thing)
import math
print(math.sqrt(16))
print(math.pi)

# Option 2: import specific names
from math import sqrt, pi
print(sqrt(16))
print(pi)

# Option 3: alias
import numpy as np
import pandas as pd
```

## Creating Your Own Module

Any `.py` file is a module. Create `mylib.py`:

```python
# mylib.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159
```

Then use it:

```python
import mylib
print(mylib.greet("Alice"))
print(mylib.PI)
```

## Creating a Package

A package is a directory with `__init__.py`:

```
mypackage/
├── __init__.py     # Can be empty, or import submodules
├── utils.py
└── models.py
```

```python
# mypackage/utils.py
def add(a, b):
    return a + b

# mypackage/__init__.py
from .utils import add    # make add available at mypackage.add
```

## `__name__ == "__main__"` Idiom

```python
# my_script.py
def main():
    print("Running as script")

if __name__ == "__main__":
    main()
```

- When run directly: `python my_script.py` → `__name__` is `"__main__"` → `main()` runs
- When imported: `import my_script` → `__name__` is `"my_script"` → `main()` does NOT run

## Standard Library Highlights

```python
import os           # OS interaction: os.getcwd(), os.listdir(), os.environ
import sys          # System: sys.argv, sys.exit(), sys.version
import json         # JSON: json.dumps(), json.loads()
import datetime     # Dates: datetime.date.today(), timedelta
import random       # Random: random.randint(), random.choice()
import re           # Regex: re.search(), re.findall(), re.sub()
import pathlib      # Paths: Path(".").glob("*.py")
import argparse     # CLI args
import csv          # CSV files
```

## Installing Third-Party Packages

```bash
# Using uv (recommended — fast)
uv venv                  # Create virtual environment
uv pip install requests  # Install package
uv pip install "rich>=13"  # With version constraint
uv pip list               # See installed packages

# Freeze requirements
uv pip freeze > requirements.txt
```
