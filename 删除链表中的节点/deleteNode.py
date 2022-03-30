# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node:ListNode):
         node.val = node.next.val
         node.next = node.next.next
        
s = Solution()
nums =[4,5,1,9]
head = p = ListNode(nums[0])

for i in range(1,len(nums)):
    node = ListNode(nums[i])
    p.next = node
    p = p.next

s.deleteNode(head.next)

while(head!=None):
    print(head.val)
    head = head.next