from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def Creat_Tree(self,Root,vals):
        if len(vals) == 0: #终止条件：val用完了
            return Root
        if vals[0] != None: #本层需要干的就是构建Root、Root.lchild、Root.rchild三个节点。
            Root = TreeNode(vals[0])
            vals.pop(0)
            Root.left = self.Creat_Tree(Root.left,vals)
            Root.right = self.Creat_Tree(Root.right,vals)
            return Root  #本次递归要返回给上一次的本层构造好的树的根节点
        else:
            Root = None
            vals.pop(0)
            return Root#本次递归要返回给上一次的本层构造好的树的根节点
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        def inorderTra(root):
            if root == None:
                return 
            inorderTra(root.left)
            res.append(root.val)
            inorderTra(root.right)
        
        inorderTra(root)
        return res
    
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = list()        
        stack = []
        node = root 
        while(node or stack):
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    def inorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        res = list() 
        p1 = root
        
        while p1:
            p2 = p1.left
            if p2:
                while(p2.right and p2.right != p1):
                    p2 = p2.right
                if p2.right == None:
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    p2.right = None
            res.append(p1.val)
            p1 = p1.right
        return res
               
if __name__ == '__main__':
    s = Solution()
    c = TreeNode()
    Root = None
    vals = []
    Roots=c.Creat_Tree(Root,vals)#Roots就是我们要的二叉树的根节点。
    print(s.inorderTraversal(Roots))
    print(s.inorderTraversal2(Roots))
    print(s.inorderTraversal3(Roots))