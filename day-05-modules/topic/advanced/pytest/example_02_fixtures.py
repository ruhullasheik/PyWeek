"""Example 2: Fixtures for Setup/Teardown

Fixtures help avoid duplicating setup code across tests.
"""

import pytest
from dataclasses import dataclass


@dataclass
class Todo:
    id: int
    title: str
    completed: bool = False


class TodoList:
    def __init__(self):
        self._todos = []
        self._next_id = 1

    def add(self, title):
        todo = Todo(self._next_id, title)
        self._todos.append(todo)
        self._next_id += 1
        return todo

    def complete(self, todo_id):
        for todo in self._todos:
            if todo.id == todo_id:
                todo.completed = True
                return todo
        raise ValueError(f"Todo {todo_id} not found")

    def pending(self):
        return [t for t in self._todos if not t.completed]

    def completed(self):
        return [t for t in self._todos if t.completed]

    def count(self):
        return len(self._todos)


@pytest.fixture
def empty_todo():
    return TodoList()


@pytest.fixture
def todo_with_items():
    tl = TodoList()
    tl.add("Learn Python")
    tl.add("Write tests")
    tl.add("Ship project")
    return tl


def test_empty_todo(empty_todo):
    assert empty_todo.count() == 0
    assert empty_todo.pending() == []
    assert empty_todo.completed() == []


def test_add_returns_todo(empty_todo):
    todo = empty_todo.add("Learn pytest")
    assert todo.id == 1
    assert todo.title == "Learn pytest"
    assert not todo.completed


def test_complete(todo_with_items):
    todo_with_items.complete(1)
    assert len(todo_with_items.completed()) == 1
    assert len(todo_with_items.pending()) == 2


def test_complete_all(todo_with_items):
    for i in range(1, 4):
        todo_with_items.complete(i)
    assert len(todo_with_items.completed()) == 3
    assert todo_with_items.pending() == []


def test_complete_invalid_id(todo_with_items):
    with pytest.raises(ValueError, match="not found"):
        todo_with_items.complete(99)
