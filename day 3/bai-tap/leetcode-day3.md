# LeetCode Day 3 — Stack & Queue (Classic set)

Hôm nay mục tiêu là nắm **pattern** (stack cơ bản, monotonic stack, queue/deque).  
Làm theo thứ tự: **Core 3** → (nếu còn thời gian) **Classic set**.

---

## Core 3 (bắt buộc)

### 1) Valid Parentheses (stack cơ bản)

- Link: https://leetcode.com/problems/valid-parentheses/
- Độ khó: Easy
- Ý tưởng: stack lưu dấu mở, gặp dấu đóng thì pop và check match
- Target: Time O(n), Space O(n)

---

### 2) Min Stack (two-stack)

- Link: https://leetcode.com/problems/min-stack/
- Độ khó: Medium
- Ý tưởng: 2 stack (stack chính + stack min)
- Target: mọi operation O(1)

---

### 3) Implement Queue using Stacks (stack/queue chuyển đổi)

- Link: https://leetcode.com/problems/implement-queue-using-stacks/
- Độ khó: Easy
- Ý tưởng: 2 stack (in/out) để amortized O(1)

---

## Classic set (chọn 2–4)

### Monotonic stack

- Daily Temperatures: https://leetcode.com/problems/daily-temperatures/
- Next Greater Element I: https://leetcode.com/problems/next-greater-element-i/
- Largest Rectangle in Histogram: https://leetcode.com/problems/largest-rectangle-in-histogram/ (Hard nhưng cực kinh điển)

### Queue / Deque / BFS

- Sliding Window Maximum (deque): https://leetcode.com/problems/sliding-window-maximum/
- Number of Recent Calls (queue): https://leetcode.com/problems/number-of-recent-calls/
- Binary Tree Level Order Traversal (BFS queue): https://leetcode.com/problems/binary-tree-level-order-traversal/

---

## Bonus (nếu còn thời gian)

- Evaluate Reverse Polish Notation: https://leetcode.com/problems/evaluate-reverse-polish-notation/
- Simplify Path: https://leetcode.com/problems/simplify-path/

