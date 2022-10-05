from textwrap import fill
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
            node =  TreeNode(val) if val != None else None
            
            if len(que) == 0:
                root = node
                que.append(node)
            elif fill_left:
                que[0].left = node
                if node:
                    que.append(node)
                fill_left =  False
            else:
                que[0].right = node
                if node:
                    que.append(node)
                que.pop(0)
                fill_left =  True
        return root
    
    def show(self, root):
        if not root:
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
    # 在层次遍历下判断到奇偶层，然后确定是否倒序
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        que = [root]
        res = []
        i = 1
        
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
            if i % 2:
                res.append(temp)  
            else:
                res.append(temp[::-1])
            i += 1
        return res
    
    # 利用双端队列
    def zigzagLevelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                if isOrderLeft:
                    temp.append(node.val)
                else:
                    temp.insert(0,node.val)
            res.append(temp) 
            isOrderLeft = not isOrderLeft 
        return res 
    

if __name__ == "__main__":
    t =  TreeNode()
    vals = [1,2,3,4,None,None,5]
    root = t.create_tree(vals)
    print(t.show(root))  # 层次遍历
    s = Solution()
    print(s.zigzagLevelOrder2(root))
    