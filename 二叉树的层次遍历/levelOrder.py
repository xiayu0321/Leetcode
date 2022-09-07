from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def create_tree(self,vals):
        if len(vals) == 0:
            return None
        
        que = []
        fill_left =  True
        
        for val in vals:
            if val != None:
                node = TreeNode(val)
            else:
                node = None
            
            if len(que) == 0:
                root = node
                que.append(node)
                
            elif fill_left:
                que[0].left = node
                fill_left = False
                if node:
                    que.append(node)
                
            else:
                que[0].right= node
                if node:
                    que.append(node)
                que.pop(0)
                fill_left = True
        return root
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        que = [root]
        res = []
        
        while(que):
            current_size = len(que)
            temp = []
            for i in range(current_size):
                node = que.pop(0)  
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                temp.append(node.val)
            res.append(temp)
        return res

if __name__ == '__main__':
    s = Solution()
    c = TreeNode()
    vals = []
    root= c.create_tree(vals)
    print(s.levelOrder(root))
                
                
            
        