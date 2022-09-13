## 二叉树的最小深度（简单）

### 题目

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

**说明：**叶子节点是指没有子节点的节点。

**提示：**

- 树中节点数的范围在 $[0, 10^5]$ 内
- `-1000 <= Node.val <= 1000`

### 思路

类似二叉树的最大深度，二叉树的最小深度也可以使用【深度优先搜索】和【广度优先搜索】两种方式进行。

第一种：深度优先搜索

深度优先搜索对于每一个非叶子节点，、只需要分别计算其左右子树的最小叶子节点深度即可，可以转换为一个递归方式。

首先判断 root 是否存在，若不存在则二叉树不存在，此时二叉树的最小深度为0；其次分为三种情况：（1）root 的左右子树都不存在，（2）只存在左或右一个子树；（3）左右子树都存在。

在情况（1）中，此时二叉树的最小深度就为1；

在情况（2）中，此时二叉树的最小深度需要继续遍历子树的深度

在情况（3）中，此时二叉树的最小深度需要判断两边子树的最小深度，进行递归。

```python
def minDepth(self, root: TreeNode) -> int:
  if root == None:
    return 0
  # 情况（1）
  if root.left == None and root.right == None:
    return 1
  left_dep = minDepth(root.left)
  right_dep = minDepth(root.right)
  # 情况（2）
  if root.left == None or root.right == None:
    if root.left:
      return left_dep += 1
    else:
      return right_dep += 1
  # 情况（3）
  return min(left_dep,right_dep) + 1

```

第二种方式：广度优先搜索，借助于层次遍历

在广度优先搜索时，第一个找到其左右子树不存在的节点，其深度就是二叉树的最小深度。因此借助于层次遍历。

在层次遍历中，取出每个节点时先判断当前节点的左右子树是否存在，如果不存在即可返回当前dep，否则将该节点的左右子树加入到队列中。在每完成一层的遍历后，二叉树的深度都要添加一层。

```python
def minDepth2(self, root: Optional[TreeNode]) -> int:
  if root == None:
    return 0
  
  que = [root]
  dep = 1
  
  while(que):
    currentSize = len(que)
    for i in range(currentSize):
    	node = que.pop(0)
      if node.left == None and node.right == None:
        return dep
      if node.left:
        que.append(node.left)
      if node.right:
        que.append(node.right)
    dep += 1
  return dep
```



