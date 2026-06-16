# LeetCode Day 4 — Hash Map / Hash Set (Classic set)

Hôm nay mục tiêu là nắm 3 pattern chính:
- **lookup O(1)** (Two Sum / membership)
- **grouping/counting** (anagrams, frequency)
- **prefix sum + hash map** (rất hay gặp)

Làm theo thứ tự: **Core 3** → (nếu còn thời gian) **Classic set**.

---

## Core 3 (bắt buộc)

### 1) Two Sum

- Link: https://leetcode.com/problems/two-sum/
- Độ khó: Easy
- Ý tưởng: dict lưu `value -> index`
- Target: Time O(n), Space O(n)

---

### 2) Group Anagrams

- Link: https://leetcode.com/problems/group-anagrams/
- Độ khó: Medium
- Ý tưởng: map key là “signature” (sort string hoặc count 26)
- Target: Time ~ O(n * k log k) (n string, k độ dài), Space O(n)

---

### 3) Subarray Sum Equals K (prefix sum + hash map)

- Link: https://leetcode.com/problems/subarray-sum-equals-k/
- Độ khó: Medium
- Ý tưởng: prefixSum, đếm số lần prefixSum xuất hiện
- Target: Time O(n), Space O(n)

---

## Classic set (chọn 2–4)

### Hash set

- Contains Duplicate: https://leetcode.com/problems/contains-duplicate/
- Longest Consecutive Sequence: https://leetcode.com/problems/longest-consecutive-sequence/

### Counting / frequency

- Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/ (hash map + heap/bucket)

### Design

- LRU Cache: https://leetcode.com/problems/lru-cache/ (hash map + doubly linked list)

