"""
Dynamic Array — Day 1 practice
Coding Interview University: implement without using Python list methods for core logic.

Yêu cầu: dùng mảng thô (list cố định làm storage) + tự quản lý size/capacity.
Không dùng: list.append, list.insert, list.pop (trong class — test code được dùng list thường).
"""

from typing import Any, Optional


class DynamicArray:
    def __init__(self, initial_capacity: int = 16) -> None:
        self._capacity = max(1, initial_capacity)
        self._size = 0
        self._data: list[Optional[Any]] = [None] * self._capacity

    def size(self) -> int:
        """Số phần tử hiện có."""
        raise NotImplementedError

    def capacity(self) -> int:
        """Sức chứa tối đa trước khi cần resize."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def at(self, index: int) -> Any:
        """Lấy phần tử tại index. Raise IndexError nếu sai."""
        raise NotImplementedError

    def push(self, item: Any) -> None:
        """Thêm vào cuối. Resize gấp đôi nếu đầy."""
        raise NotImplementedError

    def pop(self) -> Any:
        """Xóa và trả phần tử cuối. Raise IndexError nếu rỗng."""
        raise NotImplementedError

    def insert(self, index: int, item: Any) -> None:
        """Chèn tại index, dịch các phần tử phía sau."""
        raise NotImplementedError

    def prepend(self, item: Any) -> None:
        """Chèn tại index 0."""
        raise NotImplementedError

    def delete(self, index: int) -> None:
        """Xóa phần tử tại index."""
        raise NotImplementedError

    def remove(self, item: Any) -> bool:
        """Xóa phần tử đầu tiên khớp giá trị. Trả True nếu xóa được."""
        raise NotImplementedError

    def find(self, item: Any) -> int:
        """Index đầu tiên hoặc -1."""
        raise NotImplementedError

    def _resize(self, new_capacity: int) -> None:
        """Private: copy sang mảng mới."""
        raise NotImplementedError

    def __repr__(self) -> str:
        items = [self._data[i] for i in range(self._size)]
        return f"DynamicArray({items}, size={self._size}, cap={self._capacity})"


# --- Tests: chạy sau khi implement ---
# python "day 1/code/dynamic_array.py"

def _run_tests() -> None:
    arr = DynamicArray(initial_capacity=4)

    assert arr.is_empty()
    assert arr.size() == 0
    assert arr.capacity() == 4

    arr.push(10)
    arr.push(20)
    arr.push(30)
    assert arr.size() == 3
    assert arr.at(1) == 20

    arr.insert(1, 15)
    assert list_repr(arr) == [10, 15, 20, 30]

    arr.prepend(5)
    assert list_repr(arr) == [5, 10, 15, 20, 30]

    assert arr.pop() == 30
    assert arr.find(15) == 2
    assert arr.find(99) == -1

    arr.remove(15)
    assert list_repr(arr) == [5, 10, 20]

    arr.delete(0)
    assert list_repr(arr) == [10, 20]

    # trigger resize
    for i in range(20):
        arr.push(i)
    assert arr.size() == 22
    assert arr.capacity() >= arr.size()

    print("All tests passed!")


def list_repr(arr: DynamicArray) -> list:
    return [arr.at(i) for i in range(arr.size())]


if __name__ == "__main__":
    _run_tests()
