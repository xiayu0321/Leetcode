## 二叉树的锯齿形层序遍历（中等）

### 题目

给你二叉树的根节点 `root` ，返回其节点值的 **锯齿形层序遍历** 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

**提示：**

- 树中节点数目在范围 `[0, 2000]` 内
- `-100 <= Node.val <= 100`

链接：https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/

### 思路

锯齿形层序遍历奇数层（根节点为奇数层）是从左到右排序，在偶数层是从右到左排序。因此可以在层次遍历的基础上，在获得每一层结果时需要额外判断当前层是奇数层还是偶数层，以此来决定是按从左到右的序列添加，还是倒序添加。

```python
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        que = [root]
        res = []
        i = 1  # 层数
        
        while(que):
            curSize = len(que)
            temp = []
            for _ in range(curSize):
                node = que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                temp.append(node.val)
            if i % 2: # 在每一层时注意是顺序还是倒序
                res.append(temp)  
            else:
                res.append(temp[::-1])
            i += 1 # 每一层之后  层数+1
        return res
```

另一种方式是采取双端队列的形式。借助一个 boolean ：isOrderLeft标签以确定是从左到右存储还是从右到左存储。如果isOrderLeft为 True，在 temp 添加时按正常序列添加，否则，倒序添加。

```python
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        que = [root]
        isOrderLeft = True
        res = []
        
        while(que):
            curSize = len(que)
            temp = []
            for _ in range(curSize):
                node = que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if isOrderLeft: # 以boolean 数组确定添加顺序
                    temp.append(node.val)
                else:
                    temp.insert(0,node.val)
            res.append(temp) 
            isOrderLeft = not isOrderLeft  # 每一层取完要转换顺序
        return res 
```

