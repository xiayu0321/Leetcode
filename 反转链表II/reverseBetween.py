
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        p = head
        stack = []
        indexCount = 1
        
        while(p):
            if indexCount >= left and indexCount <= right:
                stack.append(p.val)  
            p = p.next
            indexCount += 1  
        p = head
        indexCount = 1
        while(p):
            if indexCount >= left and indexCount <= right:
                p.val = stack.pop()
            p = p.next
            indexCount += 1  
        return head
    
    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        newHead = ListNode(-1,head)
        pre = newHead
        
        for _ in range(left - 1):
            pre = pre.next
        left_pre_node = pre
        left_node = pre.next
        for _ in range(left,right+1):
            pre = pre.next
        right_node = pre
        right_node_succ = right_node.next
        
        left_pre_node.next = None
        right_node.next = None
        
        pr = None
        cur = left_node
        while(cur):
            next = cur.next
            cur.next = pr
            pr = cur
            cur = next

        left_pre_node.next = right_node
        left_node.next = right_node_succ
        
        return newHead.next
        
    def reverseBetween3(self, head: ListNode, left: int, right: int) -> ListNode:
        newHead = ListNode(-1,head)
        pre = newHead
        cur = head
        
        for _ in range(1,left):
            pre = pre.next    
        cur = pre.next
    
        for _ in range(left,right):
            nexxt = cur.next
            cur.next = nexxt.next
            nexxt.next = pre.next
            pre.next = nexxt

        return newHead.next
        
nums = [1,2,3,4,5]
head = None
if nums == None:
    head = None
else:
    head = p = ListNode(nums[0])
    for i in range(1,len(nums)):
        temp = ListNode(nums[i])
        p.next = temp
        p = p.next
s = Solution()
newHead = s.reverseBetween3(head,2,4)
while(newHead):
    print(newHead.val)
    newHead = newHead.next
    
    