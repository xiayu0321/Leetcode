## 二叉树的前序遍历（简单）

### 题目

给你二叉树的根节点 `root` ，返回它节点值的 **前序** 遍历。

**提示：**

- 树中节点数目在范围 `[0, 100]` 内
- `-100 <= Node.val <= 100`

### 思路

首先，对于二叉树的前序遍历，需要先访问当前节点，然后访问其左节点，最后再访问其右节点。在进入左子树或者右子树时都需要按照这样的方式进行。因此，可以使用递归方式。在递归方式中，需要先确定递归返回的条件：当前节点已不存在时，就直接返回，如果当前节点存在，就先读取当前节点的值，然后再递归其左节点，最后再递归其右节点。

```python
def preorder(root):
  if root == None:   # 递归中最重要先确定递归返回条件
  	return
	res.append(root.val)
  preorder(root.left)
  preorder(root.right)
```

另一种方式是使用迭代方式，即将递归中维护的栈显式表达。即栈中保存的是遍历完子树后需要返回的根节点。因此在遍历节点时，需要先把节点保存在栈中，并将当前节点保存在 res 中，只到遍历完叶子节点，需要返回到根节点，即从栈中 pop，在转向遍历其右节点。

```python
node = root
while stack or node:
  while node:
    res.append(node.val)
    stack.append(node)  # 栈中保存每个层的节点，为了后续遍历完好返回到根节点
    node = node.left
  node = stack.pop()
  node = node.right
  
```

最后一种算法是采用线性时间和常数空间的遍历方法——Morris 算法。该算法是利用树的空闲指针将树链表化，核心思想是对于前序遍历先左后右的情况，对任一节点p1来说，其右子树p1.right所有节点必然在左子树p1.left之后，因此先找到左子树下的最右节点，再将右子树 p1.right接入到该节点后，这样既保证了p1.right在p1.left所有点之后，又不需要再回到p1节点。 即在正常的往下循环的过程中，不断把右半部分剪下来，接到左半部分的最右下。

```python
    def preorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        if root == None:
            return root
        
        p1 = root
        while(p1):
            p2 = p1.left  
            
            if p2: # 存在左子树
                while(p2.right and p2.right != p1):  # 这个循环找到root左子树中的最右元素，那么原root的右子树就一定在该元素之后
                    p2 = p2.right
                
                if p2.right == None:   # 当前子树的右子树的叶子结点
                    res.append(p2.val)
                    p2.right = p1    # 回到根节点
                    p1 = p1.left     # 到下一个节点
                    continue
                else:
                    p2.right = None        
            else:     # 不存在左子树
                res.append(p1.val)
            p1 = p1.right  # 在所有左子树遍历完成以后还是遍历右子树
            
        return res    
```

Morris 算法的另一种思路我更能理解。

```python
def preorderTraversal4(self, root: Optional[TreeNode]) -> List[int]:
  res = list()
  while root:
    # 先添加根节点
    res.append(root.val)
    
    # 存在左子树时，先遍历左子树，遍历前先将左子树在前序遍历的最后一个节点指向根节点的右子树。前序遍历的最后一个节点：1、是叶节点，2、优先右子树，如果没有右子树再找左子树
    if root.left:
      TreeNode precessor = root.left
      while(precessor.right != None || precessor.left != None): # 找到叶节点
        if precessor.right != None: # 优先先找右子树
          precessor = precessor.right
        else:
          precessor = precessor.left
      precessor.right = root.right  # 将左子树的最右节点与右子树连接起来
      root = root.left   # 先遍历左子树
   
    # 不存在左子树时，直接遍历右子树
    else:
      root = root.right
  
  return res
```

