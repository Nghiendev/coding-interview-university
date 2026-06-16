# Checklist implement Singly Linked List — Day 2

Mục tiêu: tự implement linked list (không dùng `collections.deque` hay thư viện sẵn có).

Bạn sẽ code trong: `../code/linked_list.py`

---

## A) Operations bắt buộc

Tự implement các hàm sau:

- [ ] `size()`
- [ ] `empty()`
- [ ] `value_at(index)`
- [ ] `push_front(value)`
- [ ] `pop_front()`
- [ ] `push_back(value)` (khuyến khích có `tail`)
- [ ] `pop_back()` (sẽ O(n) dù có tail)
- [ ] `front()`
- [ ] `back()`
- [ ] `insert(index, value)`
- [ ] `erase(index)`
- [ ] `find(value)` (trả index đầu tiên, hoặc -1)
- [ ] `remove_value(value)` (xóa node đầu tiên khớp value)
- [ ] `reverse()`
- [ ] `value_n_from_end(n)` (two pointers)

---

## B) Test cases tối thiểu

### 1) Empty list
- [ ] `empty()` = True
- [ ] `size()` = 0
- [ ] `pop_front()` raise
- [ ] `pop_back()` raise

### 2) One element
- [ ] push_front(10) → front/back = 10, size = 1
- [ ] pop_front() → returns 10, list empty

### 3) Insert/Erase
- [ ] push_back: 10, 20, 30
- [ ] insert(1, 15) → 10, 15, 20, 30
- [ ] erase(2) → 10, 15, 30
- [ ] erase(0) → 15, 30

### 4) Reverse
- [ ] reverse empty
- [ ] reverse [1]
- [ ] reverse [1,2,3] → [3,2,1]

### 5) value_n_from_end
- [ ] list [10,20,30,40] → n=0 => 40, n=1 => 30, n=3 => 10
- [ ] n >= size => raise

---

## C) “Interview explain” (5 phút)

Tự trả lời (nói to hoặc viết):

1. Vì sao `value_at(i)` là O(n)?
2. Vì sao `pop_back()` là O(n) với singly linked list?
3. Tại sao linked list thường chậm hơn array trong thực tế?

