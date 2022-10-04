## 二叉树的所有路径（简单）

### 题目

给你一个二叉树的根节点 `root` ，按 **任意顺序** ，返回所有从根节点到叶子节点的路径。

**叶子节点** 是指没有子节点的节点。

**提示：**

- 树中节点的数目在范围 `[1, 100]` 内
- `-100 <= Node.val <= 100`

### 思路

题目要求是要找到根节点到叶子节点的路径，即【自顶向下】的遍历树的顺序，记录路径上的节点，并维护更新路径。因此考虑深度优先的递归方式和层次优先的非递归方式。

在深度优先的递归方式中，考虑递归中的两大必要条件：终止条件以及重复条件。终止条件是到叶子节点的情况，此时只需要将到该叶子节点的path加入到路径结果集中；对于重复条件，是每到一个节点，将根节点加入路径，再递归左子树，最后递归右子树。

```python
def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
  if root == None:
    return 
  
  res = []
  
  def dfs(root, path):
    if root:
      path += str(root.val)
      if root.left == None and root.right == None:
        res.append(path)
      else:
        path += "->"
        dfs(root.left, path)
        dfs(root.right, path)
  
  dfs(root,"")
  return res
```

另一种是基于层次的非递归方式。此时借用两个栈来存储走过的节点以及节点所对应的路径。在初始化中，利用一个栈存储根节点，另一个栈存储根节点的值。只要存储节点的栈不为空，就弹出两个栈的栈顶。然后判断弹出节点是否为叶子节点。如果是叶子结点，直接将另一个栈弹出的结果加入到结果集中；如果是非叶子结点，先入栈右节点（右节点和加入该节点元素的路径），然后在入栈左节点（左节点和加入该节点的路径）。由于是栈（先进后出），因此先入右边再入左边。

```python
def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
  if root == None:
    return 
  res = []
  stack1 = [root]
  stack2 = [root.val]
  
  while(stack1):
    node = stack1.pop()
    path = stack2.pop()
    if root.left == None and root.right == None:
      res.append(path)
    if root.right:
      path += '->'
      stack1.append(root.right)
      stack2.append(path + "->"+ str(root.right.val))
    if root.left:
      path += '->'
      stack1.append(root.left)
      stack2.append(path + "->"+ str(root.left.val))
      
  return res
     
```