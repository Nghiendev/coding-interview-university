"""
Stack (LIFO) — Day 3 practice
"""

from typing import Any


class Stack:
    def __init__(self) -> None:
        self._data: list[Any] = []

    def size(self) -> int:
        raise NotImplementedError

    def empty(self) -> bool:
        raise NotImplementedError

    def push(self, x: Any) -> None:
        raise NotImplementedError

    def peek(self) -> Any:
        raise NotImplementedError

    def pop(self) -> Any:
        raise NotImplementedError


def _run_tests() -> None:
    s = Stack()
    assert s.empty() is True
    assert s.size() == 0

    try:
        s.pop()
        raise AssertionError("pop() should raise on empty")
    except IndexError:
        pass

    s.push(1)
    s.push(2)
    s.push(3)
    assert s.peek() == 3
    assert s.size() == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.empty() is True

    print("All tests passed!")


if __name__ == "__main__":
    _run_tests()

