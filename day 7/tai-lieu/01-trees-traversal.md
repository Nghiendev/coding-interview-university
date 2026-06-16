# Trees + Traversals — Ghi chú Day 7

## 1) Tư duy (mental model)

Tree là cấu trúc “**đệ quy**”: mỗi node là gốc của một cây con.

Khi giải bài tree, bạn gần như luôn viết theo khung:
- Định nghĩa hàm `dfs(node)` trả về gì?
- Base case: `node is None`
- Kết quả của node = kết hợp kết quả của `left/right`

Đây là cách nghĩ quan trọng hơn việc thuộc traversal.

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

## 6) Ứng dụng thực tế

- **File system**: thư mục là tree (duyệt DFS/BFS)
- **DOM** trong web: tree traversal
- **Org chart**: cây quản lý
- **AST** (compiler): parse tree / syntax tree, postorder cho evaluation

