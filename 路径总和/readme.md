## 路径总和（简单）

### 题目

给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

叶子节点 是指没有子节点的节点。

提示：

* 树中节点的数目在范围 [0, 5000] 内
* -1000 <= Node.val <= 1000
* -1000 <= targetSum <= 1000

链接：https://leetcode.cn/problems/path-sum

### 思路

路径总和是找到一条根节点到叶子结点的路径，其路径上每个节点值之和为 targetSum。因此，可考虑使用递归方式。对于递归结束条件，是遇到叶子节点，在判断当前值是否为目标值，如果是则返回 True，否则返回 False。对于递归重复条件，则是到下一个节点（左节点或者右节点），此时的目标值则为 targetSum-当前节点的值即可。注意要单独考虑root 为 None 的情况。

```python
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
  if root == None:
    return False
  
  if root.left ==  None and root.right == None:
    if root.val == targetSum:
      return True
    else:
      return False
  
  return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

```

另一种方式采用广度优先搜索。通过两个队列分别保存当前需要遍历的节点 que_node以及到当前节点的路径和队列 que_val，类似层次遍历。从que_node中读出节点，判断该节点是否为叶子节点，然后从que_val取出路径值，判断路径值是否为targetSum。若为返回 True。再判断que_node取出的节点是否有左右节点，若有，则将其节点加入到que_node中，并将其 val 加入到取出路径值，并将其加入到que_val中。另一种方式则是只需要一个队列，将对应的值用二叉树的节点值来保存。

```python
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
  if root == None:
    return False
  
  que_node = [root]
  que_val = [root.val]
  
  while(que_node):
    node = que_node.pop(0)
    temp = que_val.pop(0)
    
    if node.left == None and node.right == None:
      if temp == targetSum:
        return True
      continue
    
    if node.left:
      que_node.append(node.left)
      que_val.append(temp+node.left.val)
    if node.right:
      que_node.append(node.right)
      que_val.append(temp+node.right.val)
  return False

```

```python
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        que = [root]
        
        while(que):
            node = que.pop()
            if node.left == None and node.right == None:
                if node.val == targetSum:
                    return True
            else:
                if node.right:
                    que.append(node.right)
                    node.right.val += node.val
                if node.left:
                    que.append(node.left)
                    node.left.val += node.val
        return False
```

