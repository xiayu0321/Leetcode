## 二叉树的层次遍历 II（中等）

### 题目

给你二叉树的根节点 `root` ，返回其节点值 **自底向上的层序遍历** 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

**提示：**

- 树中节点数目在范围 `[0, 2000]` 内
- `-1000 <= Node.val <= 1000`

### 思路

本题与【层次遍历】不同的是，整体结果是从底向上，但每一层的数据仍是从左到右，因此，可以在层次遍历的基础上，将最终结果进行倒序输出。

```python
def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
  res = []
  
  if root == None:
    return res
 
  que = [root]
  
  while(que):
    currentSize = len(que)
    temp = []
    for _ in range(currentSize):
      node = que.pop(0)
      if node.left:
        que.append(node.left)
      if node.right:
        que.append(node.right)
      temp.append(node.val)
    res.append(temp)
  return res[::-1]
 
```

