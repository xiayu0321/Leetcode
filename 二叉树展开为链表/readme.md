## 二叉树展开为链表（中等）

### 题目

给你二叉树的根结点 root ，请你将它展开为一个单链表：

* 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
* 展开后的单链表应该与二叉树 先序遍历 顺序相同。

**提示：**

- 树中结点数在范围 `[0, 2000]` 内
- `-100 <= Node.val <= 100`

链接：https://leetcode.cn/problems/flatten-binary-tree-to-linked-list

### 思路

题目本质上是将原二叉树按照前序遍历的顺序生成一棵只有右子树的二叉树，同时要求 root 不变，即函数无需返回值。因此，首先考虑将原二叉树进行前序遍历，将其节点按照前序遍历的顺序存储在列表中，然后遍历列表，初始时pre 和 cur 指向列表第一个节点，将 cur 节点赋给 pre 的右节点，pre 的左节点为 None。然后二者同时移动，直到列表遍历完即可。

```python
    def flatten(self, root: Optional[TreeNode]) -> None:
        res = []
       ### 用递归方式进行前序遍历
        def preOrder(root):
            if root == None:
                return 
            res.append(root)
            preOrder(root.left)
            preOrder(root.right)
        
        preOrder(root)
        
        ### 用迭代方式进行前序遍历
        # preorderList = list()
        # stack = list()  # 存储当前节点，便于后续回溯
        # node = root

        # while node or stack:
        #     while node:
        #         preorderList.append(node)
        #         stack.append(node)
        #         node = node.left
        #     node = stack.pop()
        #     node = node.right
             
        if len(res) == 0:
            root = None
        else:
            for i in range(1,len(res)):
                pre, curr = res[i-1] , res[i]
                pre.left = None
                pre.right = curr
```

第二种方式是将遍历与展开同时进行。由于遍历与展开同时进行，会导致在前序遍历在经过左子树时失去右子树的信息，导致后续无法遍历。因此考虑在展开时先将右子树的信息保存下来即可。因此，在前序遍历的栈方式实现过程中，用 pre 指向当前节点的前序节点（初始时，pre 为 None）。在从栈中每弹出一个节点就作为当前节点去遍历二叉树，只要pre 节点存在，就将pre 的左节点赋值为 None，其右节点赋值为当前节点。同时如果当前节点有左节点或右节点，将其加入栈中。（由于栈的特性，需要先加入右节点，再加入左节点）。最后将 cur 赋值给 pre，进入下一个节点的访问，直至遍历结束。

```python
def flatten2(self, root: Optional[TreeNode]) -> None:
	if root == None:
    return
  
  stack = [root]
  pre = None
  
  while(stack):
    cur = stack.pop()
    if pre:
      pre.left = None
      pre.right = cur
      
    if cur.right:
      stack.append(cur.right)
    if cur.left:
      stack.append(cur.left)
    pre = cur
```

最后一种方式是无需额外空间存储前序遍历结果。通过寻找当前节点的右子树的前驱节点（即：当前节点的左子树中访问的最后一个节点，即左子树中的最右一个节点）。找到该节点后，将当前节点的右子树连接到该前驱节点的右子树上，然后将该前驱结点变换到当前节点的右子树上,并将当前节点的左子树赋值为 None。对当前节点处理结束后，继续处理链表中的下一个节点，直到所有节点都处理结束。

```python
def flatten2(self, root: Optional[TreeNode]) -> None:
	pre = root
  
  while(cur):
    if cur.left:
      pre = nxt = cur.left
      while pre.right:
        pre = pre.right
      pre.right = cur.right
      cur.left = None
      cur.right = nxt
    cur = cur.right
  
```

