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
            node = TreeNode(val) if val else None
            
            if len(que) == 0:
                head = node
                que.append(node)
            elif fill_left:
                que[0].left = node
                fill_left = False
                if node != None:
                    que.append(node)
            else:
                que[0].right = node
                que.pop(0)
                fill_left = True
                if node != None:
                    que.append(node)
        return head
    
    def show(self, head):
        if head == None:
            return []
        
        que = [head]
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            if targetSum == root.val:
                return True
            else:
                return False
            
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    # 用两个队列分别存储遍历的节点以及到当前节点的路径值
    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        que_node = [head]
        que_val = [head.val]
        
        while(que_node):
            node = que_node.pop(0)
            temp = que_val.pop(0)
            
            if node.left == None and node.right == None:
                if temp == targetSum:
                    return True
                continue
            if node.left:
                que_node.append(node.left)
                que_val.append(temp+node.left.val)
            if node.right:
                que_node.append(node.right)
                que_val.append(temp + node.right.val)
        return False
    
    # 用一个栈分别存储遍历的节点，到当前节点由该节点的值来直接保存
    def hasPathSum3(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        que = [root]
        
        while(que):
            node = que.pop()
            if node.left == None and node.right == None:
                if node.val == targetSum:
                    return True
            else:
                if node.right:
                    que.append(node.right)
                    node.right.val += node.val
                if node.left:
                    que.append(node.left)
                    node.left.val += node.val
        return False
                    
        
if __name__ == '__main__':
    t = TreeNode()
    vals = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    head = t.create_tree(vals)
    print(t.show(head))
    s = Solution()
    print(s.hasPathSum3(head,22))