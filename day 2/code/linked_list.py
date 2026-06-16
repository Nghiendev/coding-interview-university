"""
Singly Linked List — Day 2 practice

Mục tiêu: tự implement singly linked list (không dùng deque).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    value: Any
    next: Optional["Node"] = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0

    # --- basic helpers ---
    def size(self) -> int:
        raise NotImplementedError

    def empty(self) -> bool:
        raise NotImplementedError

    def front(self) -> Any:
        raise NotImplementedError

    def back(self) -> Any:
        raise NotImplementedError

    def value_at(self, index: int) -> Any:
        raise NotImplementedError

    # --- mutations ---
    def push_front(self, value: Any) -> None:
        raise NotImplementedError

    def pop_front(self) -> Any:
        raise NotImplementedError

    def push_back(self, value: Any) -> None:
        raise NotImplementedError

    def pop_back(self) -> Any:
        raise NotImplementedError

    def insert(self, index: int, value: Any) -> None:
        """Insert value so it becomes element at `index`."""
        raise NotImplementedError

    def erase(self, index: int) -> None:
        raise NotImplementedError

    def find(self, value: Any) -> int:
        raise NotImplementedError

    def remove_value(self, value: Any) -> bool:
        """Remove first node with matching value. Return True if removed."""
        raise NotImplementedError

    def reverse(self) -> None:
        raise NotImplementedError

    def value_n_from_end(self, n: int) -> Any:
        """0-based from end: n=0 is last element."""
        raise NotImplementedError

    # --- debug helpers ---
    def to_list(self) -> list[Any]:
        out: list[Any] = []
        cur = self._head
        while cur is not None:
            out.append(cur.value)
            cur = cur.next
        return out

    def __repr__(self) -> str:
        return f"SinglyLinkedList({self.to_list()}, size={self._size})"


# --- Tests: chạy sau khi implement ---
# python "day 2/code/linked_list.py"
def _run_tests() -> None:
    ll = SinglyLinkedList()

    assert ll.empty() is True
    assert ll.size() == 0

    ll.push_front(10)
    assert ll.front() == 10
    assert ll.back() == 10
    assert ll.size() == 1

    ll.push_back(20)
    ll.push_back(30)
    assert ll.to_list() == [10, 20, 30]
    assert ll.value_at(1) == 20

    ll.insert(1, 15)
    assert ll.to_list() == [10, 15, 20, 30]

    ll.erase(2)
    assert ll.to_list() == [10, 15, 30]

    assert ll.find(15) == 1
    assert ll.find(99) == -1

    assert ll.value_n_from_end(0) == 30
    assert ll.value_n_from_end(2) == 10

    ll.reverse()
    assert ll.to_list() == [30, 15, 10]

    assert ll.remove_value(15) is True
    assert ll.to_list() == [30, 10]

    assert ll.pop_front() == 30
    assert ll.pop_back() == 10
    assert ll.empty() is True

    print("All tests passed!")


if __name__ == "__main__":
    _run_tests()

