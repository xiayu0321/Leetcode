from pickletools import StackObject
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def create_tree(self, vals):
        if len(vals) == 0:
            return None
        
        que = []
        fill_left = True
        
        for val in vals:
            if val == None:
                node = None
            else:
                node = TreeNode(val)
            
            if len(que) == 0:
                root = node
                que.append(node)
            elif fill_left:
                que[0].left = node
                fill_left = False
                if node:
                    que.append(node)
            else:
                que[0].right = node
                if node:
                    que.append(node)
                que.pop(0)
                fill_left = True                   
        return root 

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root == None:
            return res
        
        stack = []
        que = [root]
        
        while(que):
            currentSize = len(que)
            temp = []

            for i in range(currentSize):
                node = que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                temp.append(node.val)
            stack.append(temp)
        
        while(stack):
            res.append(stack.pop())
    
        return res

if __name__ == '__main__':
    t = TreeNode()
    vals = [3,9,20,None,None,15,7]
    root = t.create_tree(vals)
    s = Solution()
    print(s.levelOrderBottom(root))
    
    