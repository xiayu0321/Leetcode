from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(left, right):
            if left > right:
                return None

            mid = (right + left) // 2
          
            root = TreeNode(nums[mid])
            root.left = buildTree(left, mid - 1)
            root.right = buildTree(mid + 1, right)
            return root

        return buildTree(0, len(nums) - 1)

if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    s = Solution()
    root = s.sortedArrayToBST(nums=nums)

    # 读取二叉树
    stack = [root]
    res = []

    while(stack):
        curSize = len(stack)
        temp = []
        for _ in range(curSize):
            node = stack.pop(0)
            temp.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        res.append(temp)
    print(res)





