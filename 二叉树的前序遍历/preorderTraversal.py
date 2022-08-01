from tkinter.messagebox import NO
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
    ## 递归方式，先序遍历：先遍历根节点，在遍历左节点（此时左节点又作为新的根节点，直至所有左节点读完），在遍历右节点。
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        def preorder(root):
            if root == None:
                return 
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res
    
    ## 栈的迭代方式，将递归中维护的栈显式表示，注意判断node 为空时需要先 pop，在移动
    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        if root == None:
            return res
        
        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)  # 栈存储根节点，在后续节点遍历完之后要返回到当前层的根节点上
                node = node.left
            node = stack.pop()  # pop 出来就是上一层根节点
            node = node.right
        return res
    
    # Morris 方法：借助树的空闲指针将树链表化
    def preorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        if root == None:
            return root
        
        p1 = root
        while(p1):
            p2 = p1.left
            
            if p2: # 存在左子树
                while(p2.right and p2.right != p1):  # 这个循环找到root左子树中的最右元素，那么原root的右子树就一定在该元素之后
                    p2 = p2.right
                
                if p2.right == None:   # 当前子树的右子树的叶子结点
                    res.append(p2.val)
                    p2.right = p1    # 回到根节点
                    p1 = p1.left     # 到下一个节点
                    continue
                else:
                    p2.right = None        
            else:     # 不存在左子树
                res.append(p1.val)
            p1 = p1.right  # 在所有左子树遍历完成以后还是遍历右子树
            
        return res     
    
         

if __name__ == '__main__':
    s = Solution()
    c = TreeNode()
    Root = None
    vals = [1,None,2,None,4,5]
    Roots=c.Creat_Tree(Root,vals)#Roots就是我们要的二叉树的根节点。
    print(s.preorderTraversal(Roots))
    print(s.preorderTraversal2(Roots))
    print(s.preorderTraversal3(Roots))

        