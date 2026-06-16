# Trees + Traversals — Ghi chú Day 7

## 1) Tư duy (mental model)

Tree là cấu trúc “**đệ quy**”: mỗi node là gốc của một cây con.

Khi giải bài tree, bạn gần như luôn viết theo khung:
- Định nghĩa hàm `dfs(node)` trả về gì?
- Base case: `node is None`
- Kết quả của node = kết hợp kết quả của `left/right`

Đây là cách nghĩ quan trọng hơn việc thuộc traversal.

### Mô phỏng: cấu trúc cây mẫu

```
        1
      /   \
     2     3
    / \     \
   4   5     6

Preorder:  1 → 2 → 4 → 5 → 3 → 6   (N trước)
Inorder:   4 → 2 → 5 → 1 → 3 → 6   (N giữa)
Postorder: 4 → 5 → 2 → 6 → 3 → 1   (N sau)
```

### Mô phỏng: BFS (level-order)

```
Queue: [1]
→ dequeue 1, enqueue 2,3     → output level 0: [1]
→ dequeue 2, enqueue 4,5     → output level 1: [2, 3]
→ dequeue 3, enqueue 6       → ...
→ dequeue 4,5,6              → output level 2: [4, 5, 6]

Kết quả: [[1], [2,3], [4,5,6]]
```

### Mô phỏng: DFS recursion (call stack)

```
dfs(1)
  dfs(2)
    dfs(4)  → base
    dfs(5)  → base
  dfs(3)
    dfs(6)  → base

Stack depth ≈ chiều cao cây h
```

---

## 2) Traversals (DFS)

Cho node `N` với `left`, `right`.

- **Preorder**: `N, L, R` (dùng khi cần “process node trước”, serialize)
- **Inorder**: `L, N, R` (BST → ra thứ tự tăng dần)
- **Postorder**: `L, R, N` (dùng khi cần “process children trước”, delete tree)

### Iterative vs Recursive

- Recursive: code ngắn, nhưng có thể stack overflow nếu cây quá sâu.
- Iterative: dùng **stack** để giả lập call stack.

---

## 3) BFS (Level-order)

BFS duyệt theo tầng, dùng **queue**.

### BFS là gì (nói đơn giản)

- BFS = “duyệt **theo khoảng cách** từ gốc”.
- Trên tree, “khoảng cách” = số cạnh từ root → node.
- Queue đảm bảo: node nào vào trước thì ra trước → xử lý hết level hiện tại rồi mới sang level sau.

### BFS từng bước (kèm queue)

Với cây:

```
        1
      /   \
     2     3
    / \     \
   4   5     6
```

Ta làm:

```
queue = [1]
pop 1 → output [1], push 2,3        queue=[2,3]
pop 2 → output [1,2], push 4,5      queue=[3,4,5]
pop 3 → output [1,2,3], push 6      queue=[4,5,6]
pop 4 → ...
```

Nếu muốn **level-order dạng từng tầng**, bạn làm như sau:
- Mỗi vòng lặp lấy `level_size = len(queue)` rồi pop đúng `level_size` node.

Pseudocode:

```
queue = [root]
while queue not empty:
  level_size = len(queue)
  level = []
  repeat level_size times:
    node = queue.popleft()
    level.append(node.val)
    if node.left: queue.append(node.left)
    if node.right: queue.append(node.right)
  result.append(level)
```

Use cases:
- shortest path trên unweighted graph (tree cũng là graph)
- level-order traversal, right side view
- kiểm tra theo tầng (min depth)

---

## 4) Big-O

Giả sử có `n` nodes, height `h`.

- Time traversal: **O(n)** (visit mỗi node 1 lần)
- Space:
  - DFS recursion: O(h)
  - DFS iterative: O(h)
  - BFS queue: O(w) (w = max width), worst O(n)

---

## 5) “Bẫy” hay gặp

- Nhầm thứ tự preorder/inorder/postorder
- Quên xử lý `None`
- BFS: quên push con trái/phải đúng thứ tự
- Recursion depth lớn (cây lệch): Python có thể RecursionError

---

## 5.5) DFS vs BFS — khi nào dùng cái nào?

### DFS (stack/recursion) phù hợp khi:
- Bạn cần đi sâu một nhánh trước: path sum, validate, serialize, backtracking.
- Bạn cần space nhỏ khi cây cân: DFS dùng O(h).
- Bạn muốn viết code gọn bằng recursion.

### BFS (queue) phù hợp khi:
- Bạn cần “gần nhất / ngắn nhất” theo số bước (unweighted).
- Bạn cần theo tầng: level order, min depth, right side view.
- Bạn cần xử lý đồng thời theo level (trải đều).

Mẹo nhớ nhanh:
- **BFS = gần nhất trước**
- **DFS = sâu trước**

---

## 6) Ứng dụng thực tế

- **File system**: thư mục là tree (duyệt DFS/BFS)
- **DOM** trong web: tree traversal
- **Org chart**: cây quản lý
- **AST** (compiler): parse tree / syntax tree, postorder cho evaluation

