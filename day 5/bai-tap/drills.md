# Binary Search Drills — Day 5

Làm nhanh, không cần code cho mọi câu. Mục tiêu là chọn đúng **template** và tránh off-by-one.

---

## A) Chọn template (10 câu)

Ghi A/B/C cho từng câu:

1. Tìm index của target trong mảng tăng dần, không có trùng.
2. Tìm vị trí chèn để giữ mảng sorted (insert position).
3. Tìm phần tử đầu tiên >= target.
4. Tìm phần tử cuối cùng <= target.
5. Tìm “first bad version”.
6. Tìm min tốc độ ăn để hoàn thành trong H giờ.
7. Tìm sqrt nguyên (floor).
8. Tìm min capacity ship packages trong D ngày.
9. Tìm peak trong mountain array.
10. Tìm rotation pivot trong rotated sorted array.

---

## B) Boundary mini-cases (10 câu)

Với mảng `a = [1,2,2,2,5,7]`:

11. `lower_bound(2)` = ?
12. `upper_bound(2)` = ? (first index > 2)
13. Số lần 2 xuất hiện = ?
14. `lower_bound(6)` = ?
15. `lower_bound(0)` = ?

Edge cases:
16. Mảng rỗng `[]`, `lower_bound(10)` = ?
17. Mảng `[3]`, `lower_bound(3)` = ?
18. Mảng `[3]`, `lower_bound(4)` = ?

---

## Đáp án nhanh

<details>
<summary>Mở đáp án</summary>

1 A  
2 B  
3 B  
4 B (biến thể: tìm first > target rồi -1)  
5 C (min True)  
6 C  
7 C  
8 C  
9 C (predicate dạng “đang lên/đang xuống”)  
10 C  

11 1  
12 4  
13 4-1 = 3  
14 5  
15 0  
16 0  
17 0  
18 1  

</details>

