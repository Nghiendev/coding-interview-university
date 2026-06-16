# Linked Lists — Ghi chú Day 2

## 1) Linked list là gì?

Linked list là chuỗi các **node** rời rạc trong bộ nhớ, mỗi node chứa:

- `value`
- `next` (con trỏ/tham chiếu tới node kế tiếp)

```
head -> [A|next] -> [B|next] -> [C|None]
```

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

