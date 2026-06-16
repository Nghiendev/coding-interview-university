"""
Binary Search — Day 5 templates + tests
"""

from __future__ import annotations


def binary_search_exact(a: list[int], target: int) -> int:
    """Return index of target, or -1."""
    raise NotImplementedError


def lower_bound(a: list[int], target: int) -> int:
    """Return first index i such that a[i] >= target. If none, return len(a)."""
    raise NotImplementedError


def upper_bound(a: list[int], target: int) -> int:
    """Return first index i such that a[i] > target. If none, return len(a)."""
    raise NotImplementedError


def search_on_answer(lo: int, hi: int, ok) -> int:
    """Return min x in [lo, hi] such that ok(x) is True. Assume monotonic."""
    raise NotImplementedError


def _run_tests() -> None:
    a = [1, 2, 2, 2, 5, 7]
    assert binary_search_exact([1, 3, 5], 3) == 1
    assert binary_search_exact([1, 3, 5], 2) == -1

    assert lower_bound(a, 2) == 1
    assert upper_bound(a, 2) == 4
    assert lower_bound(a, 6) == 5
    assert lower_bound(a, 0) == 0
    assert lower_bound([], 10) == 0

    # search on answer: smallest x s.t. x*x >= 30 is 6
    def ok(x: int) -> bool:
        return x * x >= 30

    assert search_on_answer(0, 100, ok) == 6

    print("All tests passed!")


if __name__ == "__main__":
    _run_tests()

