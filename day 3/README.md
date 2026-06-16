# Day 3 — Stack & Queue

Hôm nay theo [README-vi.md](../translations/README-vi.md) bạn sẽ học:

1. **Stack (LIFO)** — dùng mảng là hiển nhiên
2. **Queue (FIFO)** — implement 2 cách: **linked list (tail pointer)** và **circular buffer**

> Mục tiêu cuối ngày: nắm Big-O của stack/queue; tự code được queue bằng linked list và circular buffer; giải 3 bài LeetCode về stack/queue.

---

## Cấu trúc thư mục

```
day 3/
├── README.md
├── links.md
├── tai-lieu/
│   └── 01-stack-queue.md
├── bai-tap/
│   ├── implement.md
│   └── leetcode-day3.md
└── code/
    ├── stack.py
    └── queue.py
```

---

## Lịch học gợi ý (8 giờ)

| Khung giờ | Việc làm | File / link |
|-----------|----------|-------------|
| **09:00 – 10:00** | Xem 1 video Stack + 1 video Queue (ngắn) | [links.md](links.md) |
| **10:00 – 10:30** | Đọc ghi chú + Big-O + khi nào dùng | [tai-lieu/01-stack-queue.md](tai-lieu/01-stack-queue.md) |
| **10:30 – 12:00** | Implement `Stack` + test | [code/stack.py](code/stack.py) |
| **12:00 – 13:00** | Nghỉ trưa | |
| **13:00 – 15:00** | Implement Queue bằng linked list + test | [code/queue.py](code/queue.py) |
| **15:00 – 16:30** | Implement Queue bằng circular buffer + test | [code/queue.py](code/queue.py) |
| **16:30 – 18:30** | 3 bài LeetCode về stack/queue | [bai-tap/leetcode-day3.md](bai-tap/leetcode-day3.md) |
| **18:30 – 19:00** | Ôn lại: invariants + Big-O (nói như phỏng vấn) | `tai-lieu/01-stack-queue.md` |

---

## Checklist — tick trong README-vi

Mở [translations/README-vi.md](../translations/README-vi.md) và tick `[x]`:

- Stack: xem video (Coursera/Review)
- Queue: video + circular buffer + implement linked list tail pointer + fixed-size array queue

