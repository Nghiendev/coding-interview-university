# LeetCode Day 1 — Arrays

Làm **3 bài Easy** sau khi đã đọc ghi chú Arrays. Mỗi bài: đọc đề → phác thảo trên giấy → code → tự test → ghi Big-O.

---

## Bài 1: Two Sum

- **Link:** https://leetcode.com/problems/two-sum/
- **Độ khó:** Easy
- **Ý tưởng:** Với mỗi `nums[i]`, cần `target - nums[i]` đã xuất hiện chưa?
- **Gợi ý DS:** Hash map (dict) lưu `value → index`
- **Target complexity:** Time O(n), Space O(n)

### Checklist khi làm
- [ ] Đọc đề, ví dụ, edge case (2 phần tử trùng index?)
- [ ] Viết pseudo-code trên giấy
- [ ] Code và chạy test
- [ ] Giải thích solution như đang phỏng vấn

---

## Bài 2: Best Time to Buy and Sell Stock

- **Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- **Độ khó:** Easy
- **Ý tưởng:** Duyệt 1 lần — theo dõi giá mua thấp nhất và lợi nhuận max
- **Gợi ý DS:** Chỉ cần mảng + 2 biến
- **Target complexity:** Time O(n), Space O(1)

### Checklist
- [ ] Xử lý mảng rỗng / 1 phần tử
- [ ] Không bán trước khi mua
- [ ] Một pass duy nhất qua mảng

---

## Bài 3: Contains Duplicate

- **Link:** https://leetcode.com/problems/contains-duplicate/
- **Độ khó:** Easy
- **Ý tưởng:** Có phần tử nào lặp không?
- **Cách 1:** Set — O(n) time, O(n) space
- **Cách 2:** Sort rồi so sánh liền kề — O(n log n) time, O(1) extra nếu sort in-place

### Thử thách
Làm **cả 2 cách** và so sánh trade-off.

---

## Bài bonus (nếu còn giờ)

| Bài | Link |
|-----|------|
| Maximum Subarray | https://leetcode.com/problems/maximum-subarray/ |
| Move Zeroes | https://leetcode.com/problems/move-zeroes/ |
| Remove Duplicates from Sorted Array | https://leetcode.com/problems/remove-duplicates-from-sorted-array/ |

---

## Template ghi chú sau mỗi bài

Tạo file `bai-tap/loi-giai-<ten-bai>.md` hoặc ghi vào đây:

```
### Tên bài
- Approach:
- Time:
- Space:
- Khó khăn:
- Học được gì:
```

---

## Không có tài khoản LeetCode?

Dùng HackerRank tương đương:
- https://www.hackerrank.com/challenges/arrays-ds/problem
- https://www.hackerrank.com/challenges/2d-array-1/problem

Hoặc làm bài **implement DynamicArray** trong [../code/dynamic_array.py](../code/dynamic_array.py) — quan trọng không kém LeetCode cho Day 1.
