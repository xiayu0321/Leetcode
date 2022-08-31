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
    # 递归方式（先确定退出条件）
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def postorderTra(node):
            if node == None:
                return
            postorderTra(node.left)
            postorderTra(node.right)
            res.append(node.val)
        postorderTra(root)
        return res
   
    ## 栈方式
    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        if root == None:
            return res
        
        stack = list()
        pre = None
        
        while(root or stack):
            while root:  # 先把所有左子树存储到栈中
                stack.append(root)
                root = root.left
            root = stack.pop() #遇到最左节点时弹出
            if root.right == None or root.right == pre: #此时判断当前根节点是否有右子树 或者是否已经访问过
                res.append(root.val)
                pre = root  # pre 指向下一个读出节点的前一个节点,避免重复访问右子树[记录当前节点便于下一步对比]
                root = None # 避免重复访问左子树[设空节点]
            else:  # 当前节点(右子树存在 && 未访问过)时，先遍历右子树，且当前根节点重新入栈
                stack.append(root)
                root = root.right
        return res

if __name__ == '__main__':
    s = Solution()
    c = TreeNode()
    Root = None
    vals = [1,None,2,3]
    Roots=c.Creat_Tree(Root,vals)#Roots就是我们要的二叉树的根节点。
    print(s.postorderTraversal(Roots))
    print(s.postorderTraversal2(Roots))
    # print(s.postorderTraversal(Roots))