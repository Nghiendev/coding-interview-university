# Hash Table — Ghi chú Day 4

## 1) Hash table là gì?

Hash table ánh xạ **key → value** để truy cập trung bình O(1).

Ý tưởng:
- Tính `h = hash(key)`
- Map `h` về index trong mảng kích thước `m` (thường dùng `h % m`)
- Xử lý **collision** khi nhiều key cùng index

### Mô phỏng: hash → index + linear probing

```
keys:  "cat"→h%7=3,  "dog"→h%7=3 (collision!),  "bird"→h%7=1

index:  0    1      2    3     4    5    6
      +----+------+----+-----+----+----+----+
      |    | bird |    | cat |dog |    |    |
      +----+------+----+-----+----+----+----+
                    ↑           ↑
                  h%7=1      h%7=3, probe→4
```

### Mô phỏng: tombstone khi remove

```
Trước remove "cat":  [ bird | cat | dog ]
Sau remove "cat":    [ bird | DEL  | dog ]   ← DEL = tombstone (không phải empty!)
get("dog") vẫn probe qua DEL để tìm ở index 2.
```

### Mô phỏng: resize (load factor vượt ngưỡng)

```
Table cũ (m=4, n=3, α=0.75):  [ A | B | C | _ ]
→ resize gấp đôi m=8, rehash TẤT CẢ entries (vì h%8 khác h%4)
```

---

## Tư duy (mental model)

Hash table giải bài toán: **tra cứu/đếm theo key nhanh**.

Khi gặp bài toán, thử hỏi:
- Có cần “đã thấy chưa?” → **set**
- Có cần “đếm số lần xuất hiện” → **map key → count**
- Có cần “ghép nhóm theo signature” → **map signature → list**
- Có cần “prefix sum / trạng thái đã gặp” → **map state → frequency**

Trong implement/thiết kế, 3 đòn bẩy chính:
- **hash function** (phân tán tốt)
- **collision strategy** (chaining vs open addressing)
- **resize policy** (load factor, rehash)

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

#### Tại sao tombstone quan trọng?

Vì `get(key)` phải probe qua các slot đã bị xóa trước đó để tìm key nằm sâu hơn trong cluster.
Nếu bạn biến slot “đã xóa” thành “empty” thì `get` sẽ dừng sớm và trả sai.

---

## 3) Load factor & resize

\(\alpha = \frac{n}{m}\) (n: số phần tử, m: capacity)

Với linear probing:
- khi \(\alpha\) cao, probe dài → chậm
- thường resize (rehash) khi \(\alpha\) vượt ngưỡng, ví dụ 0.6–0.75

Resize nghĩa là:
- tạo table mới capacity lớn hơn (thường gấp đôi)
- **rehash lại tất cả entries** (vì `h % m` thay đổi)

### Khi nào resize?

Gợi ý thực dụng cho linear probing:
- Resize up khi load factor > 0.6–0.75
- (Tùy chọn) Rehash/cleanup khi tombstone quá nhiều (vì tombstone làm probe dài)

---

## 4) Big-O (average vs worst)

| Operation | Average | Worst |
|---|---:|---:|
| add / get / exists / remove | O(1) | O(n) |

Trong phỏng vấn, bạn thường nói:
- “Average O(1), worst O(n), nhưng với resize hợp lý và hash tốt thì thực tế ổn.”

---

## 5) Probing variants (biết để nói)

- **Linear probing**: `i+1, i+2, ...` (đơn giản, cache-friendly nhưng dễ primary clustering)
- **Quadratic probing**: `i+1², i+2², ...` (giảm clustering)
- **Double hashing**: bước nhảy phụ thuộc key (giảm clustering tốt hơn)

Bạn implement linear probing là đủ cho Day 4.

---

## 6) Sai lầm hay gặp khi implement probing

- Không dùng tombstone → `get` có thể “stop sớm” và báo sai
- Resize nhưng không rehash
- Không phân biệt **Empty slot** vs **Deleted slot**
- Probe vòng quanh table nhưng không có điều kiện dừng an toàn (có thể loop vô hạn)

---

## 7) “Bài kinh điển” gắn với hash table

### Hash map / counting
- Two Sum
- Group Anagrams
- Top K Frequent Elements (đếm + heap/bucket)

### Hash set
- Longest Consecutive Sequence
- Contains Duplicate

### Prefix sum + hash map (rất hay gặp)
- Subarray Sum Equals K
- Continuous Subarray Sum

### Design (hash table + linked list)
- LRU Cache (hash map + doubly linked list)

---

## 8) Ứng dụng thực tế

- **Index** trong database / search engine (khái niệm tra cứu theo key)
- **Cache**: key → value (cộng thêm TTL/LRU/LFU)
- **Dedupe**: set để loại trùng (hash fingerprint)
- **Router / load balancer**: consistent hashing (mức nâng cao)
- **Compiler/interpreter**: symbol table (tên biến → địa chỉ/thông tin)

