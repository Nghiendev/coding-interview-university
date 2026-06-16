# BST — Ghi chú Day 8

## 1) Tư duy (mental model) & invariant

BST invariant:
- Mọi node:
  - tất cả node trong `left` có value **< node.value**
  - tất cả node trong `right` có value **> node.value**

Vì vậy:
- search/insert/delete chạy theo “đường đi” giống binary search trên cây

Complexity:
- Average: O(log n) nếu cây “khá cân”
- Worst: O(n) nếu cây lệch như linked list

### Mô phỏng: BST sau insert [5,3,7,2,4,6,8]

```
          5
        /   \
       3     7
      / \   / \
     2  4  6  8

Inorder (L,N,R): 2,3,4,5,6,7,8  ← luôn tăng dần
Search(6): 5→7→6  (3 bước)
```

### Mô phỏng: BST lệch (worst case)

```
Insert 1,2,3,4,5 theo thứ tự:

1
 \
  2
   \
    3     → giống linked list, search O(n)
     \
      4
       \
        5
```

### Mô phỏng: delete 3 case

```
Case 1 — leaf:     xóa node 2 (không con)
Case 2 — 1 con:    xóa node 4, nối con lên
Case 3 — 2 con:    xóa node 5
                   → thay bằng successor (min của right = 6)
                   → xóa successor ở vị trí cũ
```

### Mô phỏng: validate BST (range)

```
        10
       /  \
      5    15
         /    \
        12    20

Node 12: phải trong (10, 15) ✓
Node 20: phải > 15 ✓
Nếu có node 3 ở right của 15 → FAIL (3 < 15)
```

---

## 2) Operations cốt lõi

### Search
- So sánh rồi đi trái/phải.

### Insert
- Insert như search, gắn node vào vị trí `None`.

### Min/Max
- Min: đi trái đến cùng.
- Max: đi phải đến cùng.

### Validate BST

Không chỉ check “con trái < node < con phải”.  
Phải đảm bảo **range** theo tổ tiên:
- node phải nằm trong (low, high)

### Delete (3 case)

1. Node là leaf → xóa luôn.
2. Node có 1 con → nối con lên.
3. Node có 2 con → thay bằng **inorder successor** (min của right subtree) rồi xóa successor.

---

## 3) Pitfalls

- Validate sai (chỉ check 1 level).
- Delete case 2 con xử lý nhầm successor/predecessor.
- Duplicate values: quyết định policy (cấm/cho phép) và phải nhất quán.

---

## 4) Ứng dụng thực tế

- **Index / ordered map**: cần truy vấn theo thứ tự (range query). (Trong thực tế hay dùng balanced tree: red-black/B-tree.)
- **In-memory set/map** có thứ tự: hỗ trợ predecessor/successor.
- **Event scheduling**: lưu theo timestamp để lấy min/max nhanh (thường dùng heap hoặc balanced tree).

