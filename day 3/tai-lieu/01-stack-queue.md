# Stack & Queue — Ghi chú Day 3

## 1) Stack (LIFO)

**LIFO**: vào sau ra trước.

Operations:
- `push(x)`: thêm vào top
- `pop()`: lấy và xóa top
- `peek()`: xem top

**Big-O** (array/dynamic array):
- `push`, `pop`, `peek`: **O(1)** (push có thể amortized O(1))

Use cases phỏng vấn:
- Dấu ngoặc hợp lệ, expression evaluation
- DFS (iterative)
- Backtracking / undo history

---

## 2) Queue (FIFO)

**FIFO**: vào trước ra trước.

Operations:
- `enqueue(x)`: thêm vào đuôi
- `dequeue()`: lấy và xóa ở đầu
- `front()`: xem phần tử đầu

### Cách A: Linked list + tail pointer

Giữ `head` và `tail`:
- `enqueue`: thêm node vào `tail.next`, cập nhật tail → **O(1)**
- `dequeue`: lấy head, cập nhật head → **O(1)**

Nếu bạn enqueue ở đầu và dequeue ở đuôi mà không có tail/prev thì sẽ tốn **O(n)** (CIU có nhắc).

### Cách B: Circular buffer (fixed-size array)

Giữ:
- `head` (index phần tử đầu)
- `tail` (index vị trí để ghi phần tử tiếp theo)
- `size` (hoặc dùng 1 slot trống để phân biệt full/empty)

Big-O:
- `enqueue`, `dequeue`: **O(1)**
- `empty/full`: **O(1)**

Use cases phỏng vấn:
- BFS
- Sliding window (kết hợp deque)
- Producer/consumer conceptual

---

## 3) Edge cases phải test

- pop/dequeue khi rỗng (raise)
- enqueue khi full (với circular buffer)
- chuyển trạng thái rỗng → 1 phần tử → rỗng (head/tail reset đúng)

