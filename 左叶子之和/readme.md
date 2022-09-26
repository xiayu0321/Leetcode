## 左叶子之和（简单）

### 题目

给定二叉树的根节点 `root` ，返回所有左叶子之和。

**提示:**

- 节点数在 `[1, 1000]` 范围内
- `-1000 <= Node.val <= 1000`

### 思路

题目要求返回所有左叶子之和，有两个限定条件：左节点和叶子结点。所以在添加到最后结果中，要有三个判断条件：node.left(以确定是左节点)以及 node.left.left == None and node.left.right == None(以确定是子节点)。

首先考虑深度优先方法（递归）。当根节点为 None 时，说明树不存在，所以直接返回 0。当根节点存在时，分别递归其左子树和右子树，然后再借助三个判断条件进行判别，如果三个条件同时为 True，则node.left 是左叶子节点，就把当前节点的 val 加入 res，否则，说明该节点非左叶子节点，则 res+0。

```python
def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
  if root == None:
    return 0
  
  res = 0
  
  lLeft = self.sumOfLeftLeaves(root.left)
  rRight = self.sumOfLeftLeaves(root.right)
  
  # 判断该节点是否为左叶子节点
  if node.left and node.left.left == None and node.left.right == None:
    return Lleft + rRight + node.left.val
  
  return Lleft + rRight

```

另一种方式是广度优先方法。同样的，当根节点为 None 时，说明树不存在，所以直接返回 0。然后基于层次遍历的形式，先将根节点存储到队列中，再遍历队列。在遍历队列时，从队列中弹出队头元素，然后先判断其左节点，若该左节点是叶子结点，就将其结果加入 res，否则就将该左节点加入到队列中；然后再判断其右节点，直接将其加入到队列中。最后返回 res 即可。

```python
def sumOfLeftLeaves2(self, root: Optional[TreeNode]) -> int:
  if root == None:
    return 0
  
  que = [root]
  res = []
  
  while(que):
    node = que.pop(0)
    if node.left:
      if node.left.left == None and node.left.right == None:
        res += node.left.val
      else:
        que.append(node.left)
    else:
      que.append(node.right)
      
  return res

```