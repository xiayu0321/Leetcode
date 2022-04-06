from turtle import right
from typing import List
from xxlimited import new

from torch import le


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        while(head):
            l.append(head.val)
            head = head.next
        
        left = 0
        right = len(l) - 1
        while(left < right):
            if l[left] == l[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


nums = [1,2]
if not nums:
    head = None
else:
    head = p = ListNode(nums[0])
    for i in range(1,len(nums)):
        node = ListNode(nums[i])
        p.next = node
        p = p.next
s = Solution()
print(s.isPalindrome(head))

    