from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        cur = head
        smallList = p1 = ListNode(0,None)
        largeList = p2 = ListNode(0,None)

        while(cur):
            if cur.val < x:
                p1.next = cur
                p1 = p1.next
            else:
                p2.next = cur
                p2 = p2.next
            cur = cur.next
        p2.next = None
    
        p1.next = largeList.next
        return smallList.next
    
    def partition2(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        newHead = ListNode(0,head)
        pre1 = newHead
        cur1  = head
        
        while(cur1):
            while(cur1):
                if cur1.val >= x:
                    break    
                cur1 = cur1.next
                pre1 = pre1.next
            if cur1 == None:
                break
            pre2 = cur1
            cur2 = pre2.next
            
            while(cur2):
                if cur2.val < x:
                    break    
                cur2 = cur2.next
                pre2 = pre2.next
            if cur2:
                pre2.next = cur2.next
                pre1.next = cur2
                cur2.next = cur1
                pre1 = pre1.next
            else:
                return newHead.next
        return newHead.next
    
s = Solution()
nums = []
if len(nums) < 1:
    head = None
else:
    head = p = ListNode(nums[0])
    for i in range(1,len(nums)):
        node = ListNode(nums[i])
        p.next = node
        p = p.next
head = s.partition2(head,2)
while(head):
    print(head.val)
    head = head.next