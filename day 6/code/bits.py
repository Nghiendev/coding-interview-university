"""
Bit helpers — Day 6

Note: Python ints are unbounded, so some operations involving ~ may need masking
if you want 32-bit behavior (not required for most LeetCode problems).
"""

from __future__ import annotations


def is_bit_set(x: int, i: int) -> bool:
    raise NotImplementedError


def set_bit(x: int, i: int) -> int:
    raise NotImplementedError


def clear_bit(x: int, i: int) -> int:
    raise NotImplementedError


def toggle_bit(x: int, i: int) -> int:
    raise NotImplementedError


def lowbit(x: int) -> int:
    """Return lowest set bit value (x & -x). For x=0 return 0."""
    raise NotImplementedError


def popcount(x: int) -> int:
    """Count number of set bits."""
    raise NotImplementedError


def _run_tests() -> None:
    assert is_bit_set(0b101100, 2) is True
    assert set_bit(0b101100, 0) == 0b101101
    assert clear_bit(0b101100, 3) == 0b100100
    assert toggle_bit(0b101100, 5) == 0b001100
    assert lowbit(0b101100) == 0b000100
    assert popcount(0b101100) == 3
    assert popcount(0) == 0
    print("All tests passed!")


if __name__ == "__main__":
    _run_tests()

