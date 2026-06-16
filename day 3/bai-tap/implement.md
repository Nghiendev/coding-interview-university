# Checklist implement — Day 3

Code trong `../code/stack.py` và `../code/queue.py`.

---

## A) Stack (array-backed)

- [ ] `push(x)`
- [ ] `pop()` (raise nếu rỗng)
- [ ] `peek()` (raise nếu rỗng)
- [ ] `empty()`
- [ ] `size()`

Test tối thiểu:
- [ ] stack rỗng → pop/peek raise
- [ ] push 1,2,3 → pop ra 3,2,1

---

## B) Queue bằng linked list (tail pointer)

- [ ] `enqueue(x)`
- [ ] `dequeue()` (raise nếu rỗng)
- [ ] `front()` (raise nếu rỗng)
- [ ] `empty()`
- [ ] `size()`

Test tối thiểu:
- [ ] enqueue 1,2,3 → dequeue ra 1,2,3
- [ ] dequeue hết → queue empty, head/tail đúng

---

## C) Queue bằng circular buffer (fixed-size)

Yêu cầu:
- [ ] constructor nhận `capacity`
- [ ] `enqueue(x)` (raise nếu full)
- [ ] `dequeue()` (raise nếu rỗng)
- [ ] `empty()`, `full()`, `size()`

Test tối thiểu:
- [ ] capacity=3 → enqueue 3 phần tử → full
- [ ] dequeue 2 → enqueue 2 → test wrap-around đúng

