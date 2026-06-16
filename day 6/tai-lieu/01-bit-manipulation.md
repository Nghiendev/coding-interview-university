# Bit Manipulation — Ghi chú Day 6

## 1) Các phép toán bit cơ bản

Giả sử `a`, `b` là số nguyên.

| Operator | Ý nghĩa | Ví dụ |
|---|---|---|
| `&` | AND | `1 & 1 = 1`, `1 & 0 = 0` |
| `|` | OR | `1 | 0 = 1` |
| `^` | XOR | khác nhau thì 1 (`1^0=1`, `1^1=0`) |
| `~` | NOT | đảo bit |
| `<<` | shift left | nhân 2^k |
| `>>` | shift right | chia 2^k (phụ thuộc ngôn ngữ với số âm) |

---

## 2) Bit tricks kinh điển

### A) Check bit i có bật không

- `x & (1 << i)` khác 0 → bit i = 1

### B) Set/Clear/Toggle bit i

- Set: `x | (1 << i)`
- Clear: `x & ~(1 << i)`
- Toggle: `x ^ (1 << i)`

### C) Lowbit / remove lowest set bit

- `x & -x` lấy bit 1 thấp nhất (lowbit)
- `x & (x - 1)` xóa bit 1 thấp nhất

Ứng dụng:
- counting set bits (Kernighan)
- subset iteration

### D) XOR patterns

- `a ^ a = 0`
- `a ^ 0 = a`
- XOR giao hoán/ kết hợp

Ứng dụng kinh điển:
- Single Number (mọi số xuất hiện 2 lần, 1 số xuất hiện 1 lần)

---

## 3) Two’s complement (cực quan trọng)

Trong đa số hệ thống:
- số âm được lưu theo **two’s complement**
- `-x` = `~x + 1`

Điều này giải thích vì sao:
- `x & -x` hoạt động

---

## 4) Popcount (đếm bit 1)

Kernighan:
```
count = 0
while x != 0:
  x &= x-1
  count += 1
```
Time: O(number_of_set_bits)

---

## 5) “Bẫy” thường gặp

- Shift với số âm: tùy ngôn ngữ (arithmetic vs logical shift)
- `~x` trong Python cho ra số âm vì int không giới hạn bit (cần mask nếu giả lập 32-bit)

