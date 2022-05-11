from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        linkMapping = {}
        p = head
        while(p):
            if p not in linkMapping.keys():
                linkMapping[p] = 1
            else:
                return True
            p = p.next
        return False
    
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    
s = Solution()
nums = [1,2]
if len(nums) == 0:
    head = None
else:
    head = p = ListNode(nums[0])
    for i in range(1,len(nums)):
        p.next = ListNode(nums[i])
        p = p.next

# 用来添加链表中的环
# pos = 0
# p.next = head
print(s.hasCycle2(head))