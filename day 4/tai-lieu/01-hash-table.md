# Hash Table — Ghi chú Day 4

## 1) Hash table là gì?

Hash table ánh xạ **key → value** để truy cập trung bình O(1).

Ý tưởng:
- Tính `h = hash(key)`
- Map `h` về index trong mảng kích thước `m` (thường dùng `h % m`)
- Xử lý **collision** khi nhiều key cùng index

---

## 2) Collision resolution

### A) Chaining

Mỗi bucket chứa một danh sách (linked list / dynamic array) các entry.

- `add/get/remove`: trung bình O(1), xấu nhất O(n) nếu bucket quá dài
- Dễ implement, remove đơn giản

### B) Open addressing (linear probing)

Mỗi slot trong array chứa tối đa 1 entry.
Khi collision, thử slot kế tiếp:

```
i = h % m
while table[i] occupied and table[i].key != key:
    i = (i + 1) % m
```

**Remove** cần tombstone (đánh dấu “đã xóa”) để không phá chuỗi probe.

---

## 3) Load factor & resize

\(\alpha = \frac{n}{m}\) (n: số phần tử, m: capacity)

Với linear probing:
- khi \(\alpha\) cao, probe dài → chậm
- thường resize (rehash) khi \(\alpha\) vượt ngưỡng, ví dụ 0.6–0.75

Resize nghĩa là:
- tạo table mới capacity lớn hơn (thường gấp đôi)
- **rehash lại tất cả entries** (vì `h % m` thay đổi)

---

## 4) Big-O (average vs worst)

| Operation | Average | Worst |
|---|---:|---:|
| add / get / exists / remove | O(1) | O(n) |

Trong phỏng vấn, bạn thường nói:
- “Average O(1), worst O(n), nhưng với resize hợp lý và hash tốt thì thực tế ổn.”

---

## 5) Sai lầm hay gặp khi implement probing

- Không dùng tombstone → `get` có thể “stop sớm” và báo sai
- Resize nhưng không rehash
- Không phân biệt **Empty slot** vs **Deleted slot**

