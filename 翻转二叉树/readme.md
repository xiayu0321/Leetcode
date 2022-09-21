## 翻转二叉树（简单）

### 题目

给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

提示： 

* 树中节点数目范围在 `[0, 100]` 内 
* `-100 <= Node.val <= 100`

### 思路

同样为了建立整个过程，需要先建立辅助函数 create_tree 和 level_order 以方便查看结果。

对于翻转二叉树，需要将每个子树的左右节点进行互换。因此考虑可以使用递归方法。

首先将根节点的左右节点互换，然后在递归左子树以及右子树。最后返回 root 即可。

```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
  # 递归终止条件
  if root == None:
    return root
  # 首先对于根节点进行互换子节点
  temp = root.left
  root.left = root.right
  root.right = temp
  # 进行递归
  self.invertTree(root.left)
  self.invertTree(root.right)
  
  return root
```

另一种方式基于层次方法。利用队列存储一层节点，对于当层的每一个节点，进行左右节点互换，然后将其子节点加入到队列中。

```python
 def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        # 第一层放入根节点
        que = [root]
        
        while(que):
            # 迭代每一个节点，并交换其子节点
            node = que.pop(0)
            temp = node.left
            node.left = node.right
            node.right = temp
            # 添加下一层节点
            if(node.left):
                que.append(node.left)
            if(node.right):
                que.append(node.right)
        return root
```

