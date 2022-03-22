class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        newHead = ListNode(-1)
        newHead.next = head
        p = head
        pre = newHead
        first = last = None 

        while(p.next != None):
            if p.val == p.next.val and pre.val != p.val:
                first = pre
            if pre.val == p.val and p.val != p.next.val:
                last = p
            if first and last:  
                first.next = last.next
                pre = first
                first = last = None
            else:
                pre = p
            p = p.next
    
        if first.next:
            if first.next.val == p.val:
                first.next = None
        return newHead.next

nums = []
if len(nums) == 0:
    head = None
else:
    head = new = ListNode(nums[0])
    for i in range(1,len(nums)):
        new.next = ListNode(nums[i])
        new = new.next

s = Solution()
head = s.deleteDuplicates(head)
while (head != None):
    print(head.val)
    head = head.next