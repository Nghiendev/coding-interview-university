# Big-O — Ghi chú Day 1

## Big-O là gì?

**Big-O** mô tả **cách thời gian (hoặc bộ nhớ) chạy của thuật toán tăng** khi kích thước input `n` tăng.

- Không phải đo chính xác số giây chạy trên máy.
- Mô tả **xu hướng tăng** — phỏng vấn quan tâm điều này.
- Luôn nói theo **trường hợp xấu nhất** (worst case), trừ khi đề bài nói khác.

---

## Các mức phổ biến (từ nhanh → chậm)

| Ký hiệu | Tên | Ví dụ |
|---------|-----|-------|
| O(1) | Hằng số | Truy cập `arr[i]`, push/pop cuối mảng động (amortized) |
| O(log n) | Logarit | Binary search |
| O(n) | Tuyến tính | Duyệt hết mảng 1 lần |
| O(n log n) | Linearithmic | Merge sort, heapsort |
| O(n²) | Bình phương | 2 vòng lặp lồng nhau trên cùng data |
| O(2ⁿ) | Lũy thừa | Một số bài đệ quy naive |
| O(n!) | Giai thừa | Permutation brute force |

**Ghi nhớ thứ tự:** `O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)`

---

## Quy tắc tính nhanh

### 1. Bỏ hằng số
- `O(2n)` → **O(n)**
- `O(500)` → **O(1)**

### 2. Bỏ số hạng bậc thấp
- `O(n² + n)` → **O(n²)**
- `O(n + log n)` → **O(n)**

### 3. Vòng lặp
```python
for i in range(n):      # O(n)
    ...

for i in range(n):
    for j in range(n):  # O(n²)
        ...
```

### 4. Chia đôi mỗi bước → O(log n)
```python
while n > 1:
    n = n // 2   # O(log n)
```

### 5. Đệ quy
- Mỗi lần gọi tạo thêm 1 nhánh → cộng độ phức tạp các nhánh.
- Merge sort: chia đôi + merge → **O(n log n)**.

### 6. Amortized analysis (quan trọng cho mảng động)
- `push` vào mảng động: thường O(1), thỉnh thoảng O(n) khi resize.
- Trung bình trên n lần push → **amortized O(1)**.

---

## Space complexity (bộ nhớ)

- **O(1)** extra space: chỉ dùng vài biến (two pointers, swap in-place).
- **O(n)** extra space: tạo mảng/hash mới cùng cỡ input.

---

## Tư duy (mental model) khi dùng Big-O

- **Xác định “n” là gì**: số phần tử? số cạnh/đỉnh? độ dài chuỗi? phạm vi tìm kiếm?
- **Đếm phép toán chi phối**: vòng lặp, số lần truy cập cấu trúc dữ liệu, số lần gọi hàm.
- **Tách “average vs worst”**: hash table thường average O(1) nhưng worst O(n); quicksort average O(n log n) nhưng worst O(n²).
- **Đổi chi phí thời gian ↔ bộ nhớ**: dùng hash/set tăng space để giảm time; dùng two pointers để giữ space O(1).
- **Amortized**: một operation có thể thỉnh thoảng đắt (resize), nhưng trung bình vẫn rẻ (dynamic array push).

---

## Ứng dụng thực tế

- **Chọn kiến trúc**: O(n²) có thể OK nếu n ≤ 1e3, nhưng không ổn nếu n = 1e6.
- **Hiệu năng hệ thống**: tránh vòng lặp lồng nhau trên dữ liệu lớn; ưu tiên streaming O(n) thay vì load-all O(n) + sort nếu không cần.
- **Thiết kế API/data model**: thêm index (DB) để từ O(n) scan → O(log n) hoặc tốt hơn theo index.
- **Ước lượng chi phí**: network round-trip thường “đắt” hơn CPU; đôi khi tối ưu Big-O chưa quan trọng bằng giảm số lần gọi mạng.

---

## Ví dụ phân tích

```python
def find_max(arr):           # n = len(arr)
    max_val = arr[0]         # O(1)
    for x in arr:            # O(n) — duyệt n phần tử
        if x > max_val:
            max_val = x      # O(1) mỗi lần
    return max_val
# Time: O(n), Space: O(1)
```

```python
def has_duplicate(arr):
    seen = set()
    for x in arr:
        if x in seen:        # O(1) average cho set
            return True
        seen.add(x)
    return False
# Time: O(n), Space: O(n)
```

---

## Câu hỏi tự kiểm tra

1. Tại sao binary search là O(log n)?
2. Insert vào **đầu** mảng (không phải mảng động) tốn O(n) vì sao?
3. Khác nhau giữa **worst case** và **average case**?
4. `O(n)` và `O(n log n)` — input n = 1,000,000 thì cái nào chấp nhận được hơn?

→ Làm thêm: [../bai-tap/big-o-luyen-tap.md](../bai-tap/big-o-luyen-tap.md)

---

## Ghi chú của tôi

(Viết phần này sau khi xem video — tóm tắt bằng lời bạn hiểu)

- 
- 
- 
