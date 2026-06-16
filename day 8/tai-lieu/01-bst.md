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

