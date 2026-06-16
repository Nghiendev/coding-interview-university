# Linked Lists — Ghi chú Day 2

## 1) Linked list là gì?

Linked list là chuỗi các **node** rời rạc trong bộ nhớ, mỗi node chứa:

- `value`
- `next` (con trỏ/tham chiếu tới node kế tiếp)

```
head -> [A|next] -> [B|next] -> [C|None]
```

---

## Tư duy thiết kế (mental model)

- **Linked list = “con trỏ + node rời rạc”**: tối ưu cho **chèn/xóa** khi đã có con trỏ tới vị trí.
- Cái giá phải trả: **không có random access** → `value_at(i)` phải đi lần lượt O(n).
- Khi implement, giữ rõ **invariants**:
  - `head` trỏ node đầu hoặc `None`
  - `tail` (nếu có) trỏ node cuối hoặc `None`
  - `size` luôn đúng sau mọi operation

Trong phỏng vấn, linked list thường không phải để “lưu danh sách” mà để luyện pattern:
- **two pointers**
- **reverse**
- **cycle detection**

---

## 2) So sánh với Array (mảng)

| Tiêu chí | Array | Singly Linked List |
|---|---|---|
| Truy cập `i`-th element | O(1) | O(n) |
| Duyệt tuần tự | O(n) (cache-friendly) | O(n) |
| Thêm/xóa đầu | O(n) | O(1) |
| Thêm/xóa cuối | O(1) amortized (dynamic array) | O(1) nếu có tail, **O(n)** nếu không |
| Bộ nhớ | Liên tục | Rời rạc + tốn thêm `next` |

**Điểm phỏng vấn hay hỏi:** “Vì sao linked list thường chậm hơn array trong thực tế?”  
→ Vì **cache locality** kém, pointer chasing, overhead node.

---

## 3) Operations & Big-O (singly linked list)

Giả sử có `head`, (tùy chọn) `tail`, và `size`.

| Operation | Big-O | Ghi chú |
|---|---|---|
| `size()` | O(1) | nếu bạn lưu biến `size` |
| `value_at(i)` | O(n) | phải đi từ head |
| `push_front(x)` | O(1) | đổi head |
| `pop_front()` | O(1) | đổi head |
| `push_back(x)` | O(1) | nếu có tail, ngược lại O(n) |
| `pop_back()` | O(n) | cần tìm “node trước tail” |
| `insert(i, x)` | O(n) | tìm node trước `i` |
| `erase(i)` | O(n) | tìm node trước `i` |
| `reverse()` | O(n) | đổi chiều link |
| `value_n_from_end(n)` | O(n) | two pointers |

---

## 4) Kỹ thuật phỏng vấn thường gặp

### A. Two pointers

- Tìm node giữa
- Tìm `k`-th từ cuối (fast/slow)
- Detect cycle (Floyd)

### B. Reverse linked list

Invariants:
- `prev` là head của đoạn đã reverse
- `cur` là node đang xử lý
- `next` lưu lại phần còn lại

Pseudocode:

```
prev = None
cur = head
while cur:
  nxt = cur.next
  cur.next = prev
  prev = cur
  cur = nxt
head = prev
```

---

## 5) Edge cases phải test

- list rỗng
- list 1 phần tử
- insert/erase ở đầu, ở giữa, ở cuối
- value không tồn tại
- reverse rỗng / 1 phần tử / nhiều phần tử

---

## Ứng dụng thực tế

- **Free list / allocator** (khái niệm): quản lý block rảnh trong hệ thống cấp phát bộ nhớ.
- **LRU cache**: thường dùng **doubly linked list + hash map** để O(1) get/put.
- **Hệ thống/driver**: danh sách các task/descriptor đôi khi dùng linked list (nhưng nhiều hệ thống hiện đại vẫn ưu tiên array vì cache).
- **Queue bằng linked list**: enqueue/dequeue O(1) ổn định (Day 3).

