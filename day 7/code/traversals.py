"""
Tree traversals — Day 7
"""

from __future__ import annotations

from dataclasses import dataclass
from collections import deque
from typing import Optional


@dataclass
class Node:
    val: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def preorder_recursive(root: Optional[Node]) -> list[int]:
    raise NotImplementedError


def inorder_recursive(root: Optional[Node]) -> list[int]:
    raise NotImplementedError


def postorder_recursive(root: Optional[Node]) -> list[int]:
    raise NotImplementedError


def inorder_iterative(root: Optional[Node]) -> list[int]:
    raise NotImplementedError


def level_order(root: Optional[Node]) -> list[list[int]]:
    raise NotImplementedError


def _sample_tree() -> Node:
    #        1
    #      /   \
    #     2     3
    #    / \     \
    #   4   5     6
    return Node(
        1,
        left=Node(2, left=Node(4), right=Node(5)),
        right=Node(3, right=Node(6)),
    )


def _run_tests() -> None:
    root = _sample_tree()
    assert preorder_recursive(root) == [1, 2, 4, 5, 3, 6]
    assert inorder_recursive(root) == [4, 2, 5, 1, 3, 6]
    assert postorder_recursive(root) == [4, 5, 2, 6, 3, 1]
    assert inorder_iterative(root) == [4, 2, 5, 1, 3, 6]
    assert level_order(root) == [[1], [2, 3], [4, 5, 6]]
    print("All tests passed!")


if __name__ == "__main__":
    _run_tests()

