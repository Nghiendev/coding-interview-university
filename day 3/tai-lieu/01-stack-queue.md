# Stack & Queue — Ghi chú Day 3

## 1) Stack (LIFO)

**LIFO**: vào sau ra trước.

Operations:
- `push(x)`: thêm vào top
- `pop()`: lấy và xóa top
- `peek()`: xem top

**Big-O** (array/dynamic array):
- `push`, `pop`, `peek`: **O(1)** (push có thể amortized O(1))

### Mô phỏng Stack (push/pop)

```
push(1) push(2) push(3)     pop() → 3

        top
         ↓
      +-----+
      |  3  |  ← pop lấy đây
      +-----+
      |  2  |
      +-----+
      |  1  |
      +-----+
```

Valid Parentheses — stack khớp ngoặc:

```
Input:  ( [ { } ] )

Step:   (  → push '('
        [  → push '['
        {  → push '{'
        }  → pop '{'  ✓
        ]  → pop '['  ✓
        )  → pop '('  ✓  → hợp lệ
```

Use cases phỏng vấn:
- Dấu ngoặc hợp lệ, expression evaluation
- DFS (iterative)
- Backtracking / undo history

### Tư duy (mental model)

- Stack là “**history**”: cái gì vào sau cùng sẽ được xử lý/hoàn tác trước.
- Khi bài toán có dạng:
  - “khớp cặp” (parentheses)
  - “phần tử gần nhất bên trái/phải thỏa điều kiện”
  - “duyệt cây/đồ thị không đệ quy”
  → nghĩ tới stack.

### Monotonic stack (cực hay gặp)

Giữ stack theo **tăng dần** hoặc **giảm dần** để xử lý “phần tử kế tiếp lớn hơn/nhỏ hơn”.

Mẫu câu hỏi kinh điển:
- Next Greater Element
- Daily Temperatures
- Largest Rectangle in Histogram

Invariants:
- Stack lưu **index** (hay dùng hơn value vì cần tính khoảng cách).
- Duyệt từ trái sang phải: khi gặp phần tử “phá” tính đơn điệu → pop cho đến khi hợp lệ.

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

### Mô phỏng Queue (linked list + tail)

```
head                              tail
 ↓                                  ↓
[A|next] -> [B|next] -> [C|None]

enqueue(D): tail.next = D, tail = D
dequeue():  lấy A, head = head.next
```

### Mô phỏng Circular buffer (capacity=4)

```
Ban đầu:  [ _ | _ | _ | _ ]   head=0 tail=0 size=0

enqueue(A,B,C):
          [ A | B | C | _ ]   head=0 tail=3 size=3

dequeue() → A:
          [ _ | B | C | _ ]   head=1 tail=3 size=2

enqueue(D,E) — wrap-around:
          [ E | B | C | D ]   head=1 tail=1 size=4 (full)
           ↑tail wraps to 0
```

Use cases phỏng vấn:
- BFS
- Sliding window (kết hợp deque)
- Producer/consumer conceptual

### Tư duy (mental model)

- Queue là “**worklist**”: phần tử đến trước xử lý trước → phù hợp cho BFS, pipeline.
- Với circular buffer, nghĩ như “vòng tròn”: head/tail chạy vòng theo modulo, invariants quyết định đúng/sai.

### Deque (double-ended queue)

Deque là cấu trúc cho phép:
- push/pop ở **cả 2 đầu**: O(1)

Trong phỏng vấn, deque thường xuất hiện ở:
- Sliding window maximum (monotonic deque)
- 0-1 BFS (graph trọng số 0/1)

---

## 3) Edge cases phải test

- pop/dequeue khi rỗng (raise)
- enqueue khi full (với circular buffer)
- chuyển trạng thái rỗng → 1 phần tử → rỗng (head/tail reset đúng)

---

## 4) Các “bẫy” thường gặp khi implement

### Stack
- `pop/peek` khi rỗng → nên raise `IndexError`
- Không nhất quán: top ở cuối list hay đầu list? (nên để **cuối** để O(1))

### Queue (linked list)
- Khi dequeue phần tử cuối cùng: cần set cả `head = None` và `tail = None`
- Quên cập nhật `size`

### Queue (circular buffer)
- Phân biệt `empty` vs `full`:
  - Cách 1: lưu biến `size`
  - Cách 2: “chừa 1 slot trống” (khó hơn, dễ nhầm)
- Wrap-around:
  - `idx = (idx + 1) % capacity`

---

## 5) Ứng dụng thực tế

### Stack
- **Call stack** (runtime)
- **Undo/redo** trong editor
- **Expression evaluation** (RPN, shunting-yard)

### Queue/Deque
- **Message queue / event loop** (concept)
- **BFS/level-order** trong trees/graphs
- **Streaming buffer** (circular buffer) trong audio/networking
- **Rate limiting** theo time window (queue)

