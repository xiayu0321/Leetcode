from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def create_Btree(self, vals):
        if len(vals) == 0:
            return None
        
        que = []
        fill_left =  True
        
        for val in  vals:
            if val is None:
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
                que.pop(0)
    
                if node:
                    que.append(node)
                fill_left = True
        return root

class Solution:
    #深度优先搜索
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:  # 若两棵树都不存在
            return True
        elif p == None or q == None:  # 若只有一棵树存在(由于上一个 if 中已经包含了该判断中1&&1的情况，因此这个 if 中只存在 一棵树存在的情况)
            return False
        elif p.val !=  q.val:  # 在两棵树都存在的情况下，先判断根元素值是否相同
            return False
        else:  # 最后再判断左子树和右子树的情况
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    
    # 广度优先搜索，借助层次遍历
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        
        elif p == None or q == None:  # 只有一个树的情况
            return False
        
        elif p != None and q != None:
            que1 = [p]
            que2 = [q]
            
            while(que1 and que2):
                node1 = que1.pop(0)
                node2 = que2.pop(0)
                
                if node1.val != node2.val:
                    return False
                
                node1_left = node1.left
                node1_right = node1.right
                node2_left = node2.left
                node2_right = node2.right
                
                # 判断两个树的子节点是否存在
                if (node1_left == None) ^ (node2_left == None):
                    return False
                if (node1_right == None) ^ (node2_right == None):
                    return False
                
                if node1_left:
                    que1.append(node1_left)
                if node1_right:
                    que1.append(node1_right)
                if node2_left:
                    que2.append(node2_left)
                if node2_right:
                    que2.append(node2_right)

            return (len(que1) == 0) and (len(que2) == 0)  
                                
        
if __name__ == '__main__':
    t =  TreeNode()
    p = [1,2,3]
    q = [1,2,3]
    tree1 = t.create_Btree(p)
    tree2 = t.create_Btree(q)
    
    s = Solution()
    print(s.isSameTree(tree1,tree2))
    print(s.isSameTree2(tree1,tree2)) 