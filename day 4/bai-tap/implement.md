# Checklist implement — Day 4 (Hash Table: Linear Probing)

Code trong `../code/hash_table.py`.

Theo CIU, hôm nay bạn implement với mảng dùng **thăm dò tuyến tính**:

- [ ] `hash(k, m)`
- [ ] `add(key, value)` (key tồn tại → update)
- [ ] `exists(key)`
- [ ] `get(key)`
- [ ] `remove(key)`

---

## Test cases tối thiểu

### 1) Basic add/get
- [ ] add(a, 1), add(b, 2)
- [ ] get(a)=1, get(b)=2
- [ ] exists(c)=False

### 2) Update key
- [ ] add(a, 1) rồi add(a, 99)
- [ ] get(a)=99

### 3) Collision + probing
- [ ] Tạo nhiều key để va chạm (gợi ý: dùng key int và capacity nhỏ)
- [ ] Đảm bảo get/exists vẫn đúng

### 4) Remove + tombstone
- [ ] add(k1), add(k2) cùng cluster
- [ ] remove(k1)
- [ ] get(k2) vẫn đúng (không bị stop sớm)

### 5) Resize / rehash
- [ ] add nhiều phần tử vượt load factor → tự resize
- [ ] tất cả get vẫn đúng sau resize

