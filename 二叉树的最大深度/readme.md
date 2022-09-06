## 二叉树的最大深度（简单）

### 题目

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

**说明:** 叶子节点是指没有子节点的节点。

### 思路

首先，需要根据列表元素创建二叉树。从给出的示例发现，类似层次遍历的方式给出了二叉树的值，即分配左右节点的顺序与列表顺序相同。因此，考虑使用队列存储每个子树的根节点。即首先在队列存储根节点，然后读入新的数据，先将该数据分配给根节点的左节点，再判断新数据是否为 None，如果为 None 就不用入队列（它无需在被赋值为左右节点）；否则将该数据入队列；再读入新数据，这次将数据赋给根节点的右节点，同样根据该值是否为 None 判断是否将其放入队列。此时根节点的左右节点已经完全具备，此时将根节点弹出队列。此时完成一棵子树搭建，继续读入新的值，作为队列中节点的左右子树，直至列表遍历完毕。注意两个判断：是否将数据防御队列以及是否需要填充左节点。

```python
def generate_tree(self, vals):  
  if len(vals) == 0:
    return 0
  
  que = []
  fill_left = True  # 用于判断是否填充左节点
  
  for val in vals:
    if val == None:  # 生成当前节点
      node = None
    else:
      node = TreeNode(val)
      
    if len(que) == 0:  # 生成根节点
      root = node
      que.append(node)
    
    elif fill_left:   # 填充左节点
      que[0].left = node
      fill_left = False
      if node:
        que.append(node)
    
    else:              # 填充右节点
      que[0].right = node
      if node:
        que.append(node)
      fill_left = True
      que.pop(0)
      
   return root
```

深度优先搜索：在求二叉树的最大深度时，需要确定二叉树的深度为1+max{左子树的最大深度，右子树的最大深度}，因此考虑使用递归。考虑返回条件：即到达叶子结点时，此时子树深度为0。然后顺序递归左子树和右子树，最终返回max(left_dep,right_dep)+1。

```python
 def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root == None:
      return 0
    else:
      left_depth = self.maxDepth(root.left)
      right_depth = self.maxDepth(root.right)
      return 1+max(left_depth,right_depth)

```

广度优先搜索：需要在队列中存储每一层节点的值，因此二叉树的高度就是读取每一层所有节点的次数。因此考虑使用队列存储每一层节点。只要队列不为空，得到队列的大小，然后将当前队列的所有元素弹出的同时并将每个元素所对应的左右节点添加到队列中。读取完当前层，dep就+1。直至队列元素为空。

```python
def maxDepth1(self, root: Optional[TreeNode]) -> int:
  if root == None:
    return 0
  que = [root]
  dep = 0
  while(que):
    currentSize = len(que)
    for i in range(currentSize):
      node = que.pop(0)
      if node.left:
        que.append(node.left)
      if node.right:
        que.append(node.right)
    dep += 1
 return dep
```

