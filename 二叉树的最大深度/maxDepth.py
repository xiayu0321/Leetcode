from logging import root
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    # 按给定列表顺序生成二叉树 https://blog.csdn.net/baoxin1100/article/details/108025393
    def generate_tree(self, vals):  
        if len(vals) == 0:
            return None
        
        que = [] # 定义队列
        fill_left = True # 由于无法通过是否为 None 来判断该节点的左儿子是否可以填充，用一个记号判断是否需要填充左节点
        
        for val in vals:
            node = TreeNode(val) if val is not None else None # 非空值返回节点类，否则返回 None
            if len(que) == 0:
                root = node # 队列为空的话，用 root 记录根结点，用来返回
                que.append(node)
                
            elif fill_left:
                que[0].left = node
                fill_left = False # 填充过左儿子后，改变记号状态
                if node: # 非 None 值才进入队列
                    que.append(node)
            
            else:
                que[0].right = node
                if node:
                    que.append(node)
                que.pop(0) # 填充完右儿子，弹出节点
                fill_left = True 
        return root

class Solution:
    # 深度优先搜索
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_dep = self.maxDepth(root.left)
            right_dep = self.maxDepth(root.right)
            return max(left_dep,right_dep)+1
    
    # 广度优先搜索
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        que = [root]
        dep = 0
        while que:
            currentSize = len(que)
            for i in range(currentSize):
                node = que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            dep += 1
        return dep
    
if __name__ == '__main__':
    s = Solution()
    c = TreeNode()
    vals = [3,9,20,None,None,15,7]
    root= c.generate_tree(vals)
    
    print(s.maxDepth(root))
    print(s.maxDepth1(root))

