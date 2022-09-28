from platform import node
from typing import Optional

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
               if node:
                   que.append(node)
               fill_left = False
           else:
               que[0].right = node
               que.pop(0)
               if node:
                   que.append(node)
               fill_left = True
        return root 
    
    def show(self, root):
        if root == None:
            return []

        que = [root]
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
                temp.append(node.val)
            res.append(temp)
        return res
                
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        return self.isSymmetricNode(root.left,root.right)
        
    def isSymmetricNode(self,root1,root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        return self.isSymmetricNode(root1.left,root2.right) and self.isSymmetricNode(root1.right,root2.left)     
    
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right == None:
            return False
        
        que = [root.left,root.right]
        
        while(que):
            node1 = que.pop(0)
            node2 = que.pop(0)
            
            if node1 == None and node2 == None:
                continue
            
            if (node1 == None or node2 == None) or (node1.val != node2.val) :
                return False
            
            que.append(node1.left)
            que.append(node2.right)     
            que.append(node1.right)
            que.append(node2.left)
        return True               

if __name__ == "__main__":
    t = TreeNode()
    vals = [1,2,2,None,3,None,3]
    vals = [1,2,2,3,4,4,3]
    root = t.create_tree(vals=vals)
    print(t.show(root))
    
    s = Solution()
    print(s.isSymmetric2(root))
        
        