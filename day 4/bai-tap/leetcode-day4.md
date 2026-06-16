# LeetCode Day 4 — Hash Map / Hash Set

Làm 3 bài sau (đúng tinh thần hash table). Mỗi bài: phác thảo → code → test → Big-O.

---

## Bài 1: Two Sum

- Link: https://leetcode.com/problems/two-sum/
- Độ khó: Easy
- Ý tưởng: dict lưu `value -> index`
- Target: Time O(n), Space O(n)

---

## Bài 2: Contains Duplicate

- Link: https://leetcode.com/problems/contains-duplicate/
- Độ khó: Easy
- Ý tưởng: set để phát hiện trùng
- Target: Time O(n), Space O(n)

---

## Bài 3: Group Anagrams

- Link: https://leetcode.com/problems/group-anagrams/
- Độ khó: Medium
- Ý tưởng: map key là “signature” (sort string hoặc count 26)
- Target: Time ~ O(n * k log k) (n string, k độ dài), Space O(n)

---

## Bonus (nếu còn thời gian)

- Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/ (hash map + heap/bucket)
- Longest Consecutive Sequence: https://leetcode.com/problems/longest-consecutive-sequence/ (hash set)

