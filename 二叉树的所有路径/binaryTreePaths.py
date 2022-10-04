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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root == None:
            return []
        
        res = []
        
        def dfs(root, path):
            if root:
                path += str(root.val)
                # 叶子节点
                if root.left == None and root.right == None:
                    res.append(path)
                else: # 非叶子结点
                    path += "->"
                    dfs(root.left, path)
                    dfs(root.right, path)
        
        dfs(root, "")
        return res
    
    def binaryTreePaths2(self, root: Optional[TreeNode]) -> List[str]:
        if root == None:
            return 
        
        stack1 = [root]
        stack2 = [str(root.val)]
        
        res = []
        
        while(stack1):
            node =  stack1.pop()
            path = stack2.pop()
            
            if node.left == None and node.right == None:
                res.append(path)             
            if node.right:
                stack1.append(node.right)
                stack2.append(path +'->'+str(node.right.val))
            if node.left:
                stack1.append(node.left)
                stack2.append(path +'->'+str(node.left.val))               
    
        return res
          
if __name__ == "__main__":
    t = TreeNode()
    vals = [1,2,3,None,5]
    root = t.create_tree(vals=vals)
    print(t.show(root))
    
    s =  Solution()
    print(s.binaryTreePaths2(root))