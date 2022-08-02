## 二叉树的中序遍历（简单）

### 题目

给定一个二叉树的根节点 `root` ，返回 *它的 **中序** 遍历* 。

**提示：**

- 树中节点数目在范围 `[0, 100]` 内
- `-100 <= Node.val <= 100`

### 思路

类似前序遍历，中序遍历也分为三类：递归、迭代和 Mirros 算法。在递归中，也就是遍历多个节点，从最后一个节点向上攀升，每个节点上先读取左节点，再读取根节点，最后在读取右节点。与前序遍历中的递归不同的是就是读取节点的顺序不同。

```python
def inorderTra(root):
  if root == None:  # 先确定递归退出条件
    return
  inorderTra(root.left)
  res.append(root.val)
  inorderTra(root.right)
```

在迭代算法中，利用栈来存储根节点，在从根节点往左子树遍历时，将节点存储在栈中，只到遇到左叶子节点时，就从栈中弹出当前元素，读取当前元素的val，然后在遍历这个节点的右节点。

```python
        while(node or stack):
            while node:    # 节点在遍历过程中不停在变化
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)  # 读取当前节点
            node = node.right
```

在 Morros 算法中，还是要注意需要找到左子树的最优节点再去连接到根节点，以保证根节点的右子树永远在左子树之后。

![在这里插入图片描述](https://pic.leetcode-cn.com/143b40666eebb8992b1ed7e6c35d4d5f3b93c6f20ab436e5c9ffa54032c392c0.png)

```python
    def inorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        res = list() 
        p1 = root
        
        # 先确定根节点
        while p1:
            p2 = p1.left  # 记录当前节点的左子树
            if p2:
                while(p2.right and p2.right != p1):# 找到当前左子树的最右侧节点，且这个节点应该在指向根结点之前，否则整个节点又回到了根结点。
                    p2 = p2.right
                if p2.right == None: #//这个时候如果最右侧这个节点的右指针没有指向根结点，创建连接然后往下一个左子树的根结点进行连接操作。
				cur2.right = cur1;
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:  # 当左子树的最右侧节点有指向根结点，此时说明我们已经回到了根结点并重复了之前的操作，同时在回到根结点的时候我们应该已经处理完 左子树的最右侧节点 了，把路断开
                    p2.right = None
            res.append(p1.val)
            p1 = p1.right  # 一直往右边走
        return res
```