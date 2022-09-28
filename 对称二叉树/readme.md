## 对称二叉树（简单）

给你一个二叉树的根节点 `root` ， 检查它是否轴对称。

**提示：**

- 树中节点数目在范围 `[1, 1000]` 内
- `-100 <= Node.val <= 100`

链接：https://leetcode.cn/problems/symmetric-tree/

### 思路

检查一棵树是否为轴对称，可以将其作为两棵树，然后在两棵树上同时遍历，比较其中一个树的左（右）节点元素值和另一棵树的右（左）节点元素值是否相同。所有节点遍历完即可返回 True。但在两个节点元素不相同以及两棵树的左右节点存在不相同的话都会返回False。

综上，考虑使用递归方法。若根节点存在一个元素，该树呈对称，返回 True。若存在多个节点情况下，递归其左右子树，以形成两棵树进行比较。若两棵树的根节点都没有存在，则直接返回 True；若两棵树的根节点只有一个存在或者两个根节点的 val 不相同，则返回 False；否则就返回递归 一棵树的左节点和另一棵树的右节点  以及 递归一棵树的右节点和另一棵树的左节点的结果。

```python
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
  if root.left == None and root.right == None:  #只存在根节点
    return True
  return self.isSymmetricNode(root.left,root.right)
def isSymmetricNode(self,root1,roo2):
  if root1 == None and root2 == None:
    return True
  if root1 == None or root2 == None:
    return False
  if root1.val != root2.val:
    return False
  return self.isSymmetricNode(root1.left,root2.right) and self.isSymmetricNode(root1.right,root2.left)
```

另一种考虑迭代的方式，基于层次的方法。利用队列存储两棵树的节点（即一棵树的左（右）节点和另一棵树的右（左）节点），保证队列中连续两个元素存储了两棵树的对应元素。若队列连续两个元素值不相等，即可返回 False。直到队列为空时，返回 True。

```python
def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
  # 先判断根节点的情况
  if root.left == None and root.right == None:
    return True
  if root.left == None or root.right == None:
    return False
  
  que = [root,root]
  
  while(que):
    node1 = que.pop(0)
    node2 = que.pop(0)
    
    if node1 == None and node2 == None:
      continue
    if (node1 == None or node2 == None) or (node1.val != node2.val):
      return False
    
    que.append(node1.left)
    que.append(node2.right)
    que.append(node1.right)
    que.append(node2.left)
  
  return True
```

