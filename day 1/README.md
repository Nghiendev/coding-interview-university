# Day 1 — Bắt đầu DSA

Chào mừng bạn đến ngày học đầu tiên. Hôm nay tập trung **2 chủ đề nền tảng** theo [README-vi.md](../translations/README-vi.md):

1. **Big-O** — cách đo độ phức tạp thuật toán
2. **Arrays** — mảng tĩnh, mảng động, và tự implement `DynamicArray`

> Mục tiêu cuối ngày: hiểu Big-O ở mức phân tích được code đơn giản; implement xong dynamic array; làm 3 bài LeetCode Easy về mảng.

---

## Cấu trúc thư mục

```
day 1/
├── README.md              ← Bạn đang đọc file này
├── links.md               ← Tất cả link video/bài đọc (từ CIU)
├── tai-lieu/
│   ├── 01-big-o.md        ← Ghi chú Big-O
│   └── 02-arrays.md       ← Ghi chú Arrays
├── bai-tap/
│   ├── big-o-luyen-tap.md ← 15 câu phân tích độ phức tạp
│   └── leetcode-day1.md   ← 3 bài LeetCode + gợi ý
└── code/
    └── dynamic_array.py   ← Template implement mảng động
```

---

## Lịch học gợi ý (8 giờ)

| Khung giờ | Việc làm | File / link |
|-----------|----------|-------------|
| **09:00 – 10:30** | Xem video Big-O (chọn 2–3 video, không cần hết) | [links.md](links.md) → mục Big-O |
| **10:30 – 11:00** | Đọc ghi chú + cheat sheet | [tai-lieu/01-big-o.md](tai-lieu/01-big-o.md) |
| **11:00 – 12:00** | Làm bài tập Big-O | [bai-tap/big-o-luyen-tap.md](bai-tap/big-o-luyen-tap.md) |
| **12:00 – 13:00** | Nghỉ trưa | |
| **13:00 – 14:00** | Xem video Arrays | [links.md](links.md) → mục Arrays |
| **14:00 – 14:30** | Đọc ghi chú Arrays | [tai-lieu/02-arrays.md](tai-lieu/02-arrays.md) |
| **14:30 – 17:00** | Implement `DynamicArray` (không dùng `list` sẵn có) | [code/dynamic_array.py](code/dynamic_array.py) |
| **17:00 – 19:00** | 3 bài LeetCode Easy | [bai-tap/leetcode-day1.md](bai-tap/leetcode-day1.md) |
| **19:00 – 19:30** | Ôn flashcard / ghi chú; tick checkbox trong README-vi | Xem checklist bên dưới |

---

## Checklist — tick trong README-vi

Sau khi hoàn thành, mở [translations/README-vi.md](../translations/README-vi.md) và đánh dấu `[x]`:

**Big-O** (chọn những mục bạn đã xem/làm):
- [ ] Harvard CS50 - Asymptotic Notation
- [ ] Big O Notations (quick tutorial)
- [ ] Cheat sheet (bigocheatsheet.com)
- [ ] [Review] Analyzing Algorithms in 18 minutes

**Arrays**:
- [ ] Arrays CS50 Harvard
- [ ] Dynamic Arrays (Coursera video)
- [ ] Implement dynamic array (size, capacity, push, pop, insert, delete, resize…)
- [ ] Nắm O(1) vs O(n) cho từng thao tác

---

## Quy tắc học hôm nay

1. **Không xem hết mọi link** — CIU liệt kê nhiều nguồn; chọn 1–2 video chất lượng là đủ.
2. **Viết code tay trước** — phác thảo trên giấy, rồi mới gõ máy (theo CIU).
3. **Làm bài LeetCode song song** — đừng đợi học xong mới luyện.
4. **Ghi chú bằng lời của bạn** — sửa file trong `tai-lieu/` hoặc tạo `ghi-chu-cua-toi.md`.

---

## Ngày mai (Day 2 preview)

Linked Lists — lý thuyết + implement singly linked list + 2–3 bài LeetCode.

Chúc học hiệu quả!
