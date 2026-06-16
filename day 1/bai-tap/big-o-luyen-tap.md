# Bài tập Big-O — Day 1

Làm **trên giấy** trước, ghi Time và Space complexity. Đáp án ở cuối file — chỉ mở sau khi đã thử.

---

## Phần A — Nhận diện (10 câu)

Cho `n = len(arr)`. Xác định **Time** và **Space** (worst case):

### 1
```python
def sum_array(arr):
    total = 0
    for x in arr:
        total += x
    return total
```

### 2
```python
def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])
```

### 3
```python
def get_first(arr):
    return arr[0]
```

### 4
```python
def binary_search(arr, target):
  # arr đã sort tăng dần
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

### 5
```python
def copy_array(arr):
    result = []
    for x in arr:
        result.append(x)
    return result
```

### 6
```python
def has_zero(arr):
    for x in arr:
        if x == 0:
            return True
    return False
```

### 7
```python
def mystery(n):
    i = n
    while i > 1:
        i = i // 2
    return i
```

### 8
```python
def insert_at_front(arr, val):
    arr.insert(0, val)  # list Python
    return arr
```

### 9
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

### 10
```python
def merge_sorted(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out
```
*(Gợi ý: `len(a) = n`, `len(b) = m`)*

---

## Phần B — So sánh (5 câu)

Trả lời ngắn:

11. Thuật toán O(n) và O(n²) — với n = 10,000, cái nào chạy lâu hơn đáng kể?

12. Tại sao `push` vào cuối dynamic array được gọi là **amortized O(1)**?

13. `find` trong mảng chưa sort vs binary search — khác Big-O thế nào?

14. Đệ quy dùng thêm stack call — `fib(n)` naive có Space complexity là gì?

15. Sắp xếp 1 triệu số: chọn O(n²) hay O(n log n)? Vì sao?

---

## Đáp án

<details>
<summary>Nhấn để xem đáp án (sau khi đã làm xong)</summary>

| # | Time | Space |
|---|------|-------|
| 1 | O(n) | O(1) |
| 2 | O(n²) | O(1) |
| 3 | O(1) | O(1) |
| 4 | O(log n) | O(1) |
| 5 | O(n) | O(n) |
| 6 | O(n) worst, O(1) best | O(1) |
| 7 | O(log n) | O(1) |
| 8 | O(n) | O(1) hoặc O(n) nếu resize — thường ghi O(n) cho insert đầu |
| 9 | O(2ⁿ) | O(n) call stack |
| 10 | O(n + m) | O(n + m) |

**Phần B:**
11. O(n²) — 10,000² vs 10,000.
12. Hầu hết lần push O(1); thỉnh thoảng O(n) khi resize; trung bình trên n lần vẫn O(1).
13. Linear search O(n); binary search O(log n) nhưng cần mảng đã sort.
14. O(n) depth của call stack.
15. O(n log n) — n² với 1 triệu phần tử không khả thi.

</details>

---

## Tự chấm

- 13–15/15: sẵn sàng sang Arrays + LeetCode
- 10–12/15: xem lại [01-big-o.md](../tai-lieu/01-big-o.md) + 1 video
- &lt; 10/15: xem lại Harvard CS50 Big-O, làm lại Phần A
