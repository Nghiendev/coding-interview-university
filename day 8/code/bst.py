"""
BST — Day 8 starter code
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BST:
    def __init__(self) -> None:
        self._root: Optional[Node] = None
        self._count = 0

    def get_node_count(self) -> int:
        raise NotImplementedError

    def insert(self, val: int) -> None:
        raise NotImplementedError

    def is_in_tree(self, val: int) -> bool:
        raise NotImplementedError

    def print_values(self) -> list[int]:
        """Return inorder traversal (sorted for BST)."""
        raise NotImplementedError

    def get_height(self) -> int:
        """Height of a single node tree is 1. Empty tree is 0."""
        raise NotImplementedError

    def get_min(self) -> int:
        raise NotImplementedError

    def get_max(self) -> int:
        raise NotImplementedError

    def is_binary_search_tree(self) -> bool:
        raise NotImplementedError

    def delete_value(self, val: int) -> bool:
        """Delete val if present. Return True if deleted."""
        raise NotImplementedError

    def get_successor(self, val: int) -> int:
        """Return inorder successor of val, or -1 if not found."""
        raise NotImplementedError


def _run_tests() -> None:
    bst = BST()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(v)

    assert bst.get_node_count() == 7
    assert bst.print_values() == [2, 3, 4, 5, 6, 7, 8]
    assert bst.get_min() == 2
    assert bst.get_max() == 8
    assert bst.is_binary_search_tree() is True
    assert bst.is_in_tree(6) is True
    assert bst.is_in_tree(10) is False

    assert bst.delete_value(2) is True
    assert bst.print_values() == [3, 4, 5, 6, 7, 8]

    print("All tests passed!")


if __name__ == "__main__":
    _run_tests()

