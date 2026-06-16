# Day 2 — Linked Lists (Danh sách liên kết)

Hôm nay tập trung **Linked Lists** theo [README-vi.md](../translations/README-vi.md):

1. **Singly Linked List** (có/không có tail pointer)
2. So sánh **Linked List vs Array**
3. Thực hành bài phỏng vấn: **two pointers**, **reverse**, **cycle**

> Mục tiêu cuối ngày: tự implement xong singly linked list (đủ các operations); giải 3 bài LeetCode Easy/Medium cơ bản về linked list; nói được trade-off so với array và Big-O.

---

## Cấu trúc thư mục

```
day 2/
├── README.md                 ← Bạn đang đọc file này
├── links.md                  ← Link video/bài đọc (từ CIU)
├── tai-lieu/
│   └── 01-linked-lists.md    ← Ghi chú Linked Lists + Big-O
├── bai-tap/
│   ├── linked-list-implement.md ← Checklist implement + test case gợi ý
│   └── leetcode-day2.md      ← 3 bài LeetCode + gợi ý
└── code/
    └── linked_list.py        ← Template implement Singly Linked List
```

---

## Lịch học gợi ý (8 giờ)

| Khung giờ | Việc làm | File / link |
|-----------|----------|-------------|
| **09:00 – 10:00** | Xem 1–2 video trực quan về linked list | [links.md](links.md) → Linked Lists |
| **10:00 – 10:30** | Đọc ghi chú & nắm trade-off vs arrays | [tai-lieu/01-linked-lists.md](tai-lieu/01-linked-lists.md) |
| **10:30 – 12:00** | Implement core operations (head-only) | [code/linked_list.py](code/linked_list.py) |
| **12:00 – 13:00** | Nghỉ trưa | |
| **13:00 – 14:30** | Implement phần tail + reverse + value_n_from_end | [bai-tap/linked-list-implement.md](bai-tap/linked-list-implement.md) |
| **14:30 – 16:30** | Tự viết test theo checklist + sửa bug | `code/linked_list.py` |
| **16:30 – 18:30** | 3 bài LeetCode về linked list | [bai-tap/leetcode-day2.md](bai-tap/leetcode-day2.md) |
| **18:30 – 19:00** | Ôn lại: Big-O cho từng operation + 5 phút “giải thích như phỏng vấn” | `tai-lieu/01-linked-lists.md` |

---

## Checklist — tick trong README-vi

Sau khi hoàn thành, mở [translations/README-vi.md](../translations/README-vi.md) và đánh dấu `[x]` ở phần **Linked Lists** (các video bạn đã xem và các mục implement bạn đã làm).

---

## Quy tắc học hôm nay

1. **Ưu tiên code + test**: Linked list dễ sai ở case rỗng/1 phần tử.
2. **Nói được invariants**: head/tail/size thay đổi thế nào sau mỗi operation.
3. **Làm bài phỏng vấn ngay**: sau khi hiểu reverse/cycle, chuyển qua LeetCode luôn.

