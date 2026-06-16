# Tree traversal drills — Day 7

Vẽ cây sau rồi ghi thứ tự duyệt:

```
        1
      /   \
     2     3
    / \     \
   4   5     6
```

1) Preorder  
2) Inorder  
3) Postorder  
4) BFS (level-order)

---

## Bonus drills (tự làm thêm)

Cho cây:

```
    A
   /
  B
 /
C
```

5) DFS recursion space (h) là bao nhiêu?  
6) BFS space worst-case là bao nhiêu?

---

## Đáp án

<details>
<summary>Mở đáp án</summary>

1) Preorder: 1,2,4,5,3,6  
2) Inorder: 4,2,5,1,3,6  
3) Postorder: 4,5,2,6,3,1  
4) BFS: 1,2,3,4,5,6  

5) h = 3 → O(h)  
6) worst-case O(n)

</details>

