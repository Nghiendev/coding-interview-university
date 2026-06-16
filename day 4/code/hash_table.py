"""
Hash Table — Day 4 practice (Linear Probing)

Implement open addressing with linear probing + tombstones + resize (rehash).

Notes:
- We intentionally avoid using Python dict for storage.
- We'll store entries in a fixed-size list.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


_EMPTY = object()
_DELETED = object()


@dataclass
class _Entry:
    key: Any
    value: Any


class HashTable:
    def __init__(self, initial_capacity: int = 16, max_load_factor: float = 0.7) -> None:
        if initial_capacity <= 0:
            raise ValueError("initial_capacity must be positive")
        if not (0 < max_load_factor < 1):
            raise ValueError("max_load_factor must be between 0 and 1")

        cap = 1
        while cap < initial_capacity:
            cap *= 2

        self._cap = cap
        self._max_lf = max_load_factor
        self._size = 0  # number of ACTIVE entries (not deleted)
        self._table: list[object] = [_EMPTY] * self._cap  # _EMPTY | _DELETED | _Entry

    def size(self) -> int:
        raise NotImplementedError

    def capacity(self) -> int:
        raise NotImplementedError

    def _hash(self, key: Any) -> int:
        """Return raw hash value (non-negative)."""
        raise NotImplementedError

    def _find_slot(self, key: Any) -> int:
        """
        Find slot index for key.
        - If key exists, return its index.
        - If key doesn't exist, return index to insert (possibly tombstone).
        Raise RuntimeError if table is full (shouldn't happen if resize works).
        """
        raise NotImplementedError

    def exists(self, key: Any) -> bool:
        raise NotImplementedError

    def get(self, key: Any) -> Any:
        raise NotImplementedError

    def add(self, key: Any, value: Any) -> None:
        """Insert or update."""
        raise NotImplementedError

    def remove(self, key: Any) -> bool:
        """Remove key if present. Return True if removed."""
        raise NotImplementedError

    def _resize(self, new_capacity: int) -> None:
        raise NotImplementedError


def _run_tests() -> None:
    ht = HashTable(initial_capacity=4, max_load_factor=0.6)
    assert ht.size() == 0
    assert ht.exists("a") is False

    ht.add("a", 1)
    ht.add("b", 2)
    assert ht.get("a") == 1
    assert ht.get("b") == 2
    assert ht.exists("a") is True

    # update
    ht.add("a", 99)
    assert ht.get("a") == 99

    # remove
    assert ht.remove("a") is True
    assert ht.exists("a") is False
    assert ht.remove("a") is False

    # resize + correctness
    for i in range(100):
        ht.add(i, i * 10)
    for i in range(100):
        assert ht.get(i) == i * 10

    print("All tests passed!")


if __name__ == "__main__":
    _run_tests()

