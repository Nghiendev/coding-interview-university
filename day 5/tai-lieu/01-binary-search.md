# Binary Search — Ghi chú Day 5

Binary search không chỉ là “tìm trong mảng sorted”. Trong phỏng vấn nó là **3 pattern**:

1. **Exact search**: tìm đúng phần tử (hoặc -1)
2. **Boundary search**: `lower_bound` / `upper_bound`
3. **Search on answer**: binary search trên “đáp án” (monotonic predicate)

### Mô phỏng: exact search tìm target=7

```
arr = [1, 3, 5, 7, 9, 11, 13]
       0  1  2  3  4   5   6

Bước 1: lo=0 hi=6 mid=3 → arr[3]=7 ✓ tìm thấy!

Nếu target=6:
Bước 1: mid=3 arr[3]=7 > 6 → hi=2
Bước 2: lo=0 hi=2 mid=1 arr[1]=3 < 6 → lo=2
Bước 3: lo=2 hi=2 mid=2 arr[2]=5 < 6 → lo=3
        lo > hi → không có
```

### Mô phỏng: lower_bound (first index >= 6)

```
arr = [1, 3, 5, 7, 9]
       0  1  2  3  4

lo=0 hi=5 → mid=2 arr[2]=5 < 6  → lo=3
lo=3 hi=5 → mid=4 arr[4]=9 >= 6  → hi=4
lo=3 hi=4 → mid=3 arr[3]=7 >= 6  → hi=3
lo=3 hi=3 → dừng, return 3
```

### Mô phỏng: search on answer (min speed ăn đủ trong H giờ)

```
ok(speed): có ăn hết chuối trong H giờ không?
speed:  1  2  4  8  16  32 ...
ok:     F  F  F  T  T   T   ...  → tìm min speed sao cho ok=True
```

---

## Tư duy (mental model)

Binary search là kỹ thuật “**loại bỏ một nửa không gian tìm kiếm**” dựa trên một điều kiện so sánh/monotonic.

Trong khi giải bài:
- Xác định **search space** là gì (index? giá trị? đáp án?)
- Viết rõ **predicate** `ok(x)` (True/False) và kiểm tra nó **monotonic** chưa
- Chọn template phù hợp và **giữ invariants** (đặc biệt boundary search)

Một mẹo phỏng vấn: hãy nói to “Tôi đang tìm *min x* sao cho ok(x)=True” (hoặc max), để tránh nhầm.

---

## 1) Điều kiện để dùng binary search

- Không gian tìm kiếm có thứ tự (sorted) **hoặc**
- Hàm điều kiện `ok(x)` là **monotonic**: khi x tăng, ok chuyển từ False→True (hoặc ngược lại)

---

## 2) Template A — Exact match (index hoặc -1)

Invariants:
- đáp án (nếu tồn tại) luôn nằm trong \([lo, hi]\)

```
lo = 0, hi = n-1
while lo <= hi:
  mid = (lo+hi)//2
  if a[mid] == target: return mid
  if a[mid] < target: lo = mid+1
  else: hi = mid-1
return -1
```

Bẫy:
- vòng lặp `<=` (không phải `<`) vì còn 1 phần tử.

---

## 3) Template B — lower_bound (first index i with a[i] >= target)

Invariants:
- \([lo, hi)\) là khoảng nửa mở
- luôn giữ `lo` là candidate nhỏ nhất chưa loại trừ

```
lo = 0, hi = n
while lo < hi:
  mid = (lo+hi)//2
  if a[mid] >= target:
     hi = mid
  else:
     lo = mid+1
return lo  # có thể = n
```

Ứng dụng:
- First/last occurrence
- Insert position
- “smallest feasible”

---

## 4) Template C — Search on answer (min x such that ok(x) = True)

Giả sử `ok(x)` là False...False True...True.

```
lo = low_possible
hi = high_possible
while lo < hi:
  mid = (lo+hi)//2
  if ok(mid):
     hi = mid
  else:
     lo = mid+1
return lo
```

Ví dụ kinh điển:
- Koko Eating Bananas (min speed)
- Capacity To Ship Packages Within D Days
- Split Array Largest Sum

---

## 5) Bẫy off-by-one thường gặp

- Dùng sai điều kiện vòng lặp (`lo<=hi` vs `lo<hi`)
- Quên “nửa mở” \([lo, hi)\) trong boundary search
- Mid overflow (trong C++/Java dùng `lo + (hi-lo)/2`)
- Infinite loop khi `lo` không tiến (ví dụ `lo = mid` thay vì `mid+1`)

---

## 6) Ứng dụng thực tế

- **Tìm kiếm trên dữ liệu đã sort/index**: trong DB, search engine, file index (khái niệm).
- **Tuning tham số hệ thống** (search on answer): tìm min CPU/memory/capacity đáp ứng SLA, min batch size, min rate limit…
- **Scheduling / capacity planning**: “smallest feasible” (ship capacity, bandwidth).
- **UI/UX**: tìm vị trí chèn/scroll (lower_bound) trong danh sách đã sort.

