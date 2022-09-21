from inspect import stack
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def createTree(self,vals):
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
                if node != None:
                    que.append(node)
                fill_left = False
                
            else:
                que[0].right = node
                if node != None:
                    que.append(node)
                que.pop(0)
                fill_left = True
        return root
    
    
class Solution:
    def show(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        que = [root]
        res = []
        
        while(que):
            currentSize = len(que)
            for _ in range(currentSize):    
                node = que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                res.append(node.val)
        return res
                
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        root.left ,root.right = root.right,root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
    # 层次方法实现
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        
        que = [root]
        
        while(que):
            node = que.pop(0)
            temp = node.left
            node.left = node.right
            node.right = temp
            
            if(node.left):
                que.append(node.left)
            if(node.right):
                que.append(node.right)
        return root
       
    # 深度优先遍历         
    def invertTree3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        
        stack = [root]
        
        while(stack):
            current_size = len(stack)
            for i in range(current_size):
                cur = stack.pop(-1)
                temp = cur.left
                cur.left = cur.right
                cur.right = temp
                
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
        return root
 
if __name__ == '__main__':
    t = TreeNode()
    vals = [4,2,7,1,3,6,9]
    root = t.createTree(vals)
    
    s = Solution()
    print(s.show(root))
    print(s.show(s.invertTree3(root)))