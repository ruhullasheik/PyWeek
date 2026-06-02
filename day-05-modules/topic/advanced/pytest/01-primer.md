# Pytest — Testing Your Code

## Why Test?

You already write code. You probably test it manually — run the script, check the output, pray. pytest automates this.

Benefits:
- **Confidence** — refactor without fear
- **Documentation** — tests show how your code is *supposed* to work
- **Speed** — `uv run pytest` is faster than manual clicking/running
- **Catch regressions** — when you fix one thing, tests check you didn't break another

## Install

```bash
uv pip install pytest
```

## Your First Test

Create a file named `test_demo.py`:

```python
# test_demo.py
def test_one_plus_one():
    result = 1 + 1
    assert result == 2
```

Run it:

```bash
uv run pytest test_demo.py
```

Output:

```
============================= test session starts ==============================
collected 1 item

test_demo.py .                                                            [100%]

============================== 1 passed in 0.01s ===============================
```

## Naming Conventions

pytest discovers tests by filename and function name:

| Rule | Example |
|---|---|
| File must start or end with `test_` | `test_*.py` or `*_test.py` |
| Function must start with `test_` | `def test_add():` |
| Class must start with `Test` | `class TestCalculator:` |

## Assertions

Use plain Python `assert`. No special `assertEquals` needed.

```python
def test_string():
    assert "hello".upper() == "HELLO"
    assert "hello".__len__() == 5
    assert "python" in "I love python"

def test_collections():
    assert 3 in [1, 2, 3]          # membership
    assert [1, 2, 3] == [1, 2, 3]  # list equality
    assert not [1, 2] == [2, 1]    # order matters

def test_approximate():
    assert 0.1 + 0.2 == pytest.approx(0.3)  # float comparison
```

## Testing Exceptions

```python
import pytest

def test_raises():
    with pytest.raises(ValueError):
        int("not-a-number")
```

## Parametrize — One Test, Many Inputs

```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert a + b == expected
```

## Test Structure: Arrange → Act → Assert

```python
def test_withdraw_reduces_balance():
    # Arrange — set up the object
    account = BankAccount("Alice", 1000)

    # Act — perform the operation
    account.withdraw(200)

    # Assert — check the result
    assert account.balance == 800
```

## Fixtures — Shared Setup

```python
import pytest

@pytest.fixture
def empty_list():
    return []

@pytest.fixture
def populated_list():
    return [1, 2, 3]

def test_empty(empty_list):
    assert len(empty_list) == 0

def test_populated(populated_list):
    assert len(populated_list) == 3
    assert sum(populated_list) == 6
```

## Run All Tests in a Directory

```bash
uv run pytest                    # discover and run all tests
uv run pytest -v                # verbose
uv run pytest -k "string"       # run tests matching expression
uv run pytest --tb=short        # shorter tracebacks
uv run pytest --cov=.           # with coverage (needs pytest-cov)
```
