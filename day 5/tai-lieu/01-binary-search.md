# Binary Search — Ghi chú Day 5

Binary search không chỉ là “tìm trong mảng sorted”. Trong phỏng vấn nó là **3 pattern**:

1. **Exact search**: tìm đúng phần tử (hoặc -1)
2. **Boundary search**: `lower_bound` / `upper_bound`
3. **Search on answer**: binary search trên “đáp án” (monotonic predicate)

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

