"""
Queue (FIFO) — Day 3 practice

Implement 2 versions:
1) LinkedListQueue: linked list with tail pointer
2) CircularBufferQueue: fixed-size array circular buffer
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class _Node:
    value: Any
    next: Optional["_Node"] = None


class LinkedListQueue:
    def __init__(self) -> None:
        self._head: Optional[_Node] = None
        self._tail: Optional[_Node] = None
        self._size: int = 0

    def size(self) -> int:
        raise NotImplementedError

    def empty(self) -> bool:
        raise NotImplementedError

    def front(self) -> Any:
        raise NotImplementedError

    def enqueue(self, x: Any) -> None:
        raise NotImplementedError

    def dequeue(self) -> Any:
        raise NotImplementedError


class CircularBufferQueue:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._cap = capacity
        self._data: list[Optional[Any]] = [None] * capacity
        self._head = 0  # index of current front element
        self._tail = 0  # index of next write position
        self._size = 0

    def size(self) -> int:
        raise NotImplementedError

    def empty(self) -> bool:
        raise NotImplementedError

    def full(self) -> bool:
        raise NotImplementedError

    def front(self) -> Any:
        raise NotImplementedError

    def enqueue(self, x: Any) -> None:
        raise NotImplementedError

    def dequeue(self) -> Any:
        raise NotImplementedError


def _run_tests() -> None:
    q = LinkedListQueue()
    assert q.empty() is True
    assert q.size() == 0
    try:
        q.dequeue()
        raise AssertionError("dequeue() should raise on empty")
    except IndexError:
        pass

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.front() == 1
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.empty() is True

    cb = CircularBufferQueue(3)
    assert cb.empty() is True
    cb.enqueue("a")
    cb.enqueue("b")
    cb.enqueue("c")
    assert cb.full() is True
    try:
        cb.enqueue("x")
        raise AssertionError("enqueue() should raise on full")
    except OverflowError:
        pass
    assert cb.dequeue() == "a"
    assert cb.dequeue() == "b"
    cb.enqueue("d")
    cb.enqueue("e")
    assert cb.dequeue() == "c"
    assert cb.dequeue() == "d"
    assert cb.dequeue() == "e"
    assert cb.empty() is True

    print("All tests passed!")


if __name__ == "__main__":
    _run_tests()

