# Day 4 — Hash Table (Linear Probing)

Hôm nay theo [README-vi.md](../translations/README-vi.md) bạn sẽ học **Hash Table** và tự implement bằng **open addressing (linear probing)**.

> Mục tiêu cuối ngày: hiểu collision + load factor + resize + tombstone; tự code `HashTable` (add/exists/get/remove); làm **Core 3** LeetCode (lookup + grouping + prefix sum) và chọn thêm 1–2 bài kinh điển.

---

## Cấu trúc thư mục

```
day 4/
├── README.md
├── links.md
├── tai-lieu/
│   └── 01-hash-table.md
├── bai-tap/
│   ├── implement.md
│   └── leetcode-day4.md
└── code/
    └── hash_table.py
```

---

## Lịch học gợi ý (8 giờ)

| Khung giờ | Việc làm | File / link |
|-----------|----------|-------------|
| **09:00 – 10:30** | Xem 2 video: chaining + open addressing | [links.md](links.md) |
| **10:30 – 11:00** | Đọc ghi chú: collision, load factor, resize | [tai-lieu/01-hash-table.md](tai-lieu/01-hash-table.md) |
| **11:00 – 12:00** | Implement khung `HashTable` (hash/add/get/exists) | [code/hash_table.py](code/hash_table.py) |
| **12:00 – 13:00** | Nghỉ trưa | |
| **13:00 – 15:00** | Implement remove (tombstone) + resize | `code/hash_table.py` |
| **15:00 – 16:00** | Viết test theo checklist | [bai-tap/implement.md](bai-tap/implement.md) |
| **16:00 – 18:30** | LeetCode: Core 3 + 1–2 bài classic | [bai-tap/leetcode-day4.md](bai-tap/leetcode-day4.md) |
| **18:30 – 19:00** | Ôn: trade-off chaining vs probing, Big-O | `tai-lieu/01-hash-table.md` |

---

## Checklist — tick trong README-vi

Mở [translations/README-vi.md](../translations/README-vi.md) và tick `[x]` phần **Hash table**:

- Video bạn đã xem
- Cài đặt với mảng sử dụng thăm dò tuyến tính: `hash/add/exists/get/remove`

