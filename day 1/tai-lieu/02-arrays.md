# Arrays — Ghi chú Day 1

## Mảng là gì?

**Array (mảng)** lưu các phần tử **liên tiếp trong bộ nhớ**, truy cập theo **index** (thường bắt đầu từ 0).

```
index:  0    1    2    3    4
      +----+----+----+----+----+
      | 10 | 20 | 30 | 40 | 50 |
      +----+----+----+----+----+
```

---

## Ưu / nhược điểm

| Ưu điểm | Nhược điểm |
|---------|------------|
| Truy cập theo index: **O(1)** | Chèn/xóa ở giữa: **O(n)** (phải dịch phần tử) |
| Bộ nhớ liên tục → cache-friendly | Kích thước cố định (mảng tĩnh) hoặc phải resize |
| Đơn giản, nhanh cho đọc tuần tự | Xóa ở đầu/giữa tốn kém |

---

## Mảng tĩnh vs mảng động (Dynamic Array)

| | Mảng tĩnh | Mảng động (vector) |
|---|-----------|---------------------|
| Kích thước | Cố định lúc tạo | Tự tăng khi đầy |
| Python | Không có sẵn (dùng `list`) | `list` bên trong là dynamic array |
| Resize | Không | Thường **gấp đôi capacity** |

### Cơ chế resize (quan trọng!)

1. Ban đầu: `capacity = 16`, `size = 0`
2. `push` khi `size == capacity` → cấp phát mảng mới capacity × 2, copy toàn bộ
3. Một lần push có thể O(n), nhưng trung bình n lần push → **amortized O(1)**

**Shrink (thu nhỏ):** một số implementation giảm capacity khi `size <= capacity/4` để tiết kiệm bộ nhớ.

---

## Độ phức tạp thao tác (theo CIU)

| Thao tác | Mảng / Dynamic Array |
|----------|----------------------|
| `at(i)` / truy cập index | O(1) |
| `push` / thêm cuối | O(1) amortized |
| `pop` / xóa cuối | O(1) |
| `insert(i)` / thêm giữa | O(n) |
| `delete(i)` / xóa giữa | O(n) |
| `find(value)` | O(n) |
| `prepend` / thêm đầu | O(n) |

**Không gian:** O(n) — lưu n phần tử (capacity có thể 2n nhưng vẫn ký hiệu O(n)).

---

## Các method cần implement hôm nay

Theo [README-vi](../translations/README-vi.md):

```
size()           — số phần tử hiện có
capacity()       — sức chứa tối đa
is_empty()
at(index)        — lấy phần tử, lỗi nếu index sai
push(item)       — thêm cuối
insert(index, item)
prepend(item)    — thêm đầu
pop()            — xóa và trả phần tử cuối
delete(index)    — xóa tại index
remove(item)     — xóa phần tử đầu tiên khớp giá trị
find(item)       — index đầu tiên hoặc -1
resize(new_cap)  — private, gọi khi cần
```

→ Code template: [../code/dynamic_array.py](../code/dynamic_array.py)

---

## Mảng đa chiều & jagged array (đọc lướt)

- **2D array:** `matrix[row][col]` — hàng liên tục hoặc mảng các mảng.
- **Jagged array:** mỗi hàng có độ dài khác nhau.

Không cần implement hôm nay; chỉ biết khái niệm.

---

## Arrays vs Linked List (nhắc sớn cho Day 2)

| | Array | Linked List |
|---|-------|-------------|
| Truy cập index | O(1) | O(n) |
| Chèn đầu | O(n) | O(1) với con trỏ head |
| Bộ nhớ | Liên tục | Rải rác (node + pointer) |

---

## Ghi chú của tôi

- 
- 
- 
