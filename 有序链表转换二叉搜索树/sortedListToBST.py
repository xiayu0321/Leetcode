from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def getMedian(left, right):
            fast =  slow = left

            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def buildTree(left, right):
            if left == right:
                return None
            mid = getMedian(left,right)
            print(mid.val)

            root = TreeNode(mid.val)
            root.left = buildTree(left,mid)
            root.right = buildTree(mid.next,right)
            return root
        
        return buildTree(head,None)
    
    def sortedListToBST2(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def getListLengh(head):
            c = 0
            while(head):
                c += 1
                head = head.next
            return c
        
        def buildTree(left, right):
            if left > right:
                return None
            
            mid = (left + right  + 1) // 2
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(mid+1, right)
            return root
        
        return buildTree(0, getListLengh(head) - 1)      
        
if __name__ == "__main__":
    vals = [-10,-3,0,5,9]
    head = p = ListNode(vals[0])
    
    for i in range(1,len(vals)):
        node = ListNode(vals[i])
        p.next = node
        p = p.next
    
    # # 验证链表是否创建成功
    # while(head):
    #     print(head.val)
    #     head = head.next
        
    s =  Solution()
    root = s.sortedListToBST2(head=head)
    
    # # 验证是否成功创建二叉搜索树
    stack = [root]
    res = []
    
    while(stack):
        curSize = len(stack)
        temp = []
        for _ in range(curSize):
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            temp.append(node.val)
        res.append(temp)
    print(res)
            
    
    
    
        
    
            
                