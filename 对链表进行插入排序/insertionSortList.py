# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummpyNode = ListNode(-5001,head)
        pre = dummpyNode
        cur = head

        while(cur.next):
            if cur.val > cur.next.val:
                node = cur.next
                while(pre.next.val < node.val):
                    pre = pre.next
                cur.next = node.next
                node.next = pre.next
                pre.next = node
                pre = dummpyNode      
              
            else:
                cur = cur.next
        return dummpyNode.next
    

s = Solution()
nums = [1]
if len(nums) < 1:
    head = None
else:
    head = p = ListNode(nums[0])
    for i in range(1,len(nums)):
        p.next = ListNode(nums[i])
        p = p.next

head = s.insertionSortList(head)
while(head):
    print(head.val)
    head = head.next