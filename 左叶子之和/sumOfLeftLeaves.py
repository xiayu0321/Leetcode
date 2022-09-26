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
                if node:
                    que.append(node)
                que.pop(0)
                fill_left = True
        return root
    
    def show(self,root):
        if root == None:
            return []
        
        res = []
        que = [root]
        
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        lLeft = self.sumOfLeftLeaves(root.left)
        rRight = self.sumOfLeftLeaves(root.right)
        
        if root.left and root.left.left == None and root.left.right == None: # 判断当前节点是否为叶子节点
            return lLeft + rRight + root.left.val
        
        return lLeft + rRight 
    
    def sumOfLeftLeaves2(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        que = [root]
        res = 0
        
        while(que):
            node = que.pop(0)
            if node.left:
                if node.left.left == None and node.left.right == None:
                    res += node.left.val
                else:
                    que.append(node.left)
            if node.right:
                que.append(node.right)
        return res
            
if __name__ == "__main__":
    
    vals = [3,9,20,None,None,15,7] 
    t = TreeNode()
    root = t.create_tree(vals)
    print(t.show(root))
    
    s = Solution()
    print(s.sumOfLeftLeaves2(root))
    