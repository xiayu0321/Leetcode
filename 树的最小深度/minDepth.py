from locale import currency
from signal import valid_signals
from textwrap import fill
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def create_tree(self, vals):
        if len(vals) == 0:
            return None
        
        stack = []
        fill_left = True
        
        for val in vals:
            if val == None:
                node = None
            else:
                node = TreeNode(val)
            
            if len(stack) == 0:
                root = node
                stack.append(node)
            
            elif fill_left == True:
                stack[0].left = node
                fill_left = False
                if node != None:
                    stack.append(node)
            else:
                stack[0].right = node
                stack.pop(0)
                if node != None:
                    stack.append(node)
                fill_left = True
        return root
                
class Solution:
    # 深度优先搜索
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 树不存在的情况
        if root ==  None:
            return 0
        # 左子树和右子树都不存在的情况
        if root.left == None and root.right == None:
            return 1
        
        minDepth1 = self.minDepth(root.left)
        minDepth2 = self.minDepth(root.right)
        
        # 此时左子树和右子树只存在一边（也就是minDepth1和minDepth2其中一个肯定为0），返回不为空的那边子树节点值
        if root.left == None or root.right == None:
            if root.left:
                return minDepth1 + 1
            else:
                return minDepth2 + 1
        
        # 此时左右子树都存在，则返回左右孩子较小深度的节点值
        return min(minDepth1,minDepth2)+1
    
    # 广度优先搜索
    def minDepth2(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        que= [root]
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
                
if __name__ == '__main__':
    t = TreeNode()
    vals = [3,9,20,None,None,15,7]
    root = t.create_tree(vals=vals)
    
    s =  Solution()
    print(s.minDepth2(root=root))
    
    