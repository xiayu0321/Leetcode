## 相同的树（简单）

给你两棵二叉树的根节点 `p` 和 `q` ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

**提示：**

- 两棵树上的节点数目都在范围 `[0, 100]` 内
- $-10^4 <= Node.val <= 10^4$

## 思路

首先，通过列表创建二叉树，列表中存放的是二叉树的层次遍历形式，因此仍可以借助队列形式进行创建二叉树。先判断列表中的元素长度，若为0说明二叉树不存在，则直接返回 None。否则，借助队列和布尔值 fill_left（用于判断当前节点是否存在左节点，用于后续插入左节点）辅助创建。然后遍历列表元素，先生成 TreeNode，然后根据创建根节点、左节点和右节点的顺序进行。首先是创建根节点，根据队列长度是否为0进行判断，将生成TreeNode赋给 root，并将生成TreeNode加入到队列中。然后说创建左节点，根据 fill_left 来判断，将新生成节点添加到 queue[0].left，同时改变 fill_left 为 False，此外还要判断新生成节点是否为空来判断是否加入到队列中。最后是创建右节点，将新生成节点添加到 queue[0].right，同时改变 fill_left 为 True，此时当前节点的左右节点已完备，就直接从队列中弹出，此外还要判断新生成节点是否为空来判断是否加入到队列中。遍历完成以后返回 root。

在判断两棵树是否相同时，需要判断二叉树的结构以及对应的值是否相同。只要有一样不同，说明两棵树不相同。因此可以采用搜索方式进行。

考虑深度优先搜索。先判断两棵树是否存在，若两棵树都不存在，那两棵树是相同的，然后判断两棵树是否只有一棵树存在（直接用 or 判断，由于两个都不存在的情况已经被考虑了），若只有一棵树存在，则两棵树不同。如果两棵树都存在，则需要判断两棵树根节点的值是否相同，如果不同，那两棵树也不相同，然后通过递归根节点的左子树以及右子树。只有左子树和右子树也同样完全相同时，才能说明两棵树相同。

```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:  # 若两棵树都不存在
            return True
        elif p == None or q == None:  # 若只有一棵树存在(由于上一个 if 中已经包含了该判断中1&&1的情况，因此这个 if 中只存在 一棵树存在的情况)
            return False
        elif p.val !=  q.val:  # 在两棵树都存在的情况下，先判断根元素值是否相同
            return False
        else:  # 最后再判断左子树和右子树的情况
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
```

另一种不采用递归的方式，则使用广度优先搜索。类似层次遍历，借助两个队列存储两棵树的节点，每次从两个队列取出一个节点进行比较判断。同样地，先判断两棵树是否存在和两棵树是否只有一棵树存在的情况。然后在两棵树同时存在的情况下，将两棵树的根节点先分别存储在队列中。只要两个队列都不为空，遍历队列中元素，在遍历时每次从两个队列各取出一个节点，进行比较操作。首先，先遍历两个节点的元素值，如果不相则两个二叉树一定不同；否则，再判断两个节点的子节点是否为空（可采取异或操作），如果只有一个节点的左子节点为空，或者只有一个节点的右子节点为空，则两个二叉树的结构不同，因此两个二叉树一定不同。最后，如果两个节点的子节点的结构相同，则将两个节点的非空子节点分别加入两个队列。最后只有在两个队列都为空的情况下才返回 True

```python
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:  # 若两棵树都不存在
            return True
        elif p == None or q == None:  # 若只有一棵树存在(由于上一个 if 中已经包含了该判断中1&&1的情况，因此这个 if 中只存在 一棵树存在的情况)
            return False
        elif p.val !=  q.val:  # 在两棵树都存在的情况下，先判断根元素值是否相同
            return False
        else:  # 最后再判断左子树和右子树的情况
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    
    # 广度优先搜索，借助层次遍历
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        
        elif p == None or q == None:  # 只有一个树的情况
            return False
        
        elif p != None and q != None:
            que1 = [p]
            que2 = [q]
            
            while(que1 and que2):
                node1 = que1.pop(0)
                node2 = que2.pop(0)
                
                if node1.val != node2.val:
                    return False
                
                node1_left = node1.left
                node1_right = node1.right
                node2_left = node2.left
                node2_right = node2.right
                
                # 判断两个树的子节点是否存在
                if (node1_left == None) ^ (node2_left == None):
                    return False
                if (node1_right == None) ^ (node2_right == None):
                    return False
                
                if node1_left:
                    que1.append(node1_left)
                if node1_right:
                    que1.append(node1_right)
                if node2_left:
                    que2.append(node2_left)
                if node2_right:
                    que2.append(node2_right)

            return (len(que1) == 0) and (len(que2) == 0)  
```

