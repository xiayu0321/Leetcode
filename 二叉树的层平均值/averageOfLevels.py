from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def create_tree(self, vals):
        if len(vals) == 0:
            return None

        stack = []
        fill_left = True

        for val in vals:
            node = None if val == None else TreeNode(val)
            print(node.val)

            if len(stack) == 0:
                root = node  
                stack.append(node)
            elif fill_left:
                stack[0].left = node  
                if node:
                    stack.append(node)
                fill_left = False
            else:
                stack[0].right = node 
                if node:
                    stack.append(node)
                stack.pop(0)
                fill_left =  True
        return root

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack = [root]
        res = []

        while(stack):
            curSize = len(stack)
            tempSum = 0

            for _ in range(curSize):
                node = stack.pop(0)
                tempSum += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(tempSum / curSize)
        return res


if __name__ == "__main__":
    t =  TreeNode()
    vals = [3,9,20,15,7]
    root = t.create_tree(vals)
    s = Solution()
    print(s.averageOfLevels(root))



