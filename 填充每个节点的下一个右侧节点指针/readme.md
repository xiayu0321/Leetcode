## 填充每个节点的下一个右侧节点指针（中等）

### 题目

给定一个 **完美二叉树** ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

**提示：**

- 树中节点的数量在 $[0, 2^{12} - 1]$ 范围内
- `-1000 <= node.val <= 1000`

链接：https://leetcode.cn/problems/populating-next-right-pointers-in-each-node
### 思路

题目要求是对**完美二叉树**的每一层节点构建链表。因此，可以考虑在层次遍历的基础上，再读取每一个节点的基础上，将其与下一个节点链接即可。

```python
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root 

        stack = [root]
        res = []
		
        while(stack):
            curSize = len(stack)

            for i in range(curSize):
                node = stack.pop(0)
                # 此时在每一层中将当前节点与下一个节点链接
                if i < curSize - 1:
                    node.next = stack[0]

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return root
```

另一种方式是充分利用完美二叉树的特点，即树中每一层元素都是满的，因此可以利用第N层的链表构建第N+1层的链表。通过遍历左子树，就可以移动到每层，每一层的最左节点就是每一层链表的头节点，由此再遍历的同时链接节点，此时分为两种情况：同一个根节点的左右节点相连和不同根节点的右左节点相连。

```python
    def connect2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root

        start = root
        # 在当前层构造好链表后，再去构建下一层的链表，同时由于是完美二叉树，只要起始节点的左节点存在，那么当前层就存在
        while(start.left): # 第N+1层
            head = start   # 第N层
            while(head): 
                # 根据第N层构建第N+1链表
                head.left.next = head.right  # 这是直接链接的情况

                if head.next:  # 根据第N层构建两个子树（不同根节点）的链接
                    head.right.next = head.next.left 
                head = head.next # 在一层中移动
            start = start.left # 往每一次层移动

        return root
```



