# Bit Drills — Day 6

Làm nhanh, tính tay trước khi code.

---

## A) Tính nhị phân (8 câu)

1. `13` ở dạng nhị phân?
2. `0b101101` ở dạng thập phân?
3. `1 << 5` = ?
4. `40 >> 3` = ?
5. `13 & 7` = ?
6. `13 | 7` = ?
7. `13 ^ 7` = ?
8. `~0` là gì trong Python?

---

## B) Bit ops thực tế (7 câu)

Cho `x = 0b101100`:

9. Bit 2 (0-based) có bật không?
10. Set bit 0.
11. Clear bit 3.
12. Toggle bit 5.
13. `x & (x-1)` bằng bao nhiêu?
14. `x & -x` bằng bao nhiêu?
15. Popcount của `x`?

---

## Đáp án nhanh

<details>
<summary>Mở đáp án</summary>

1) 1101  
2) 45  
3) 32  
4) 5  
5) 5  
6) 15  
7) 10  
8) -1 (Python int vô hạn bit, ~0 == -1)

Với x=0b101100 (44):
9) bit2 = 1 (vì 44 & 4 != 0)  
10) 0b101101 (45)  
11) clear bit3 (8): 44 & ~8 = 36 (0b100100)  
12) toggle bit5 (32): 44 ^ 32 = 12 (0b001100)  
13) 44 & 43 = 40 (0b101000)  
14) 44 & -44 = 4 (0b000100)  
15) 3

</details>

