from tkinter.messagebox import NO


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while(head != None):
            if head.val == val:
                head = head.next
            else:
                break
        
        pre = head
        if pre == None or pre.next == None:
            return head
        else:
            p = pre.next
            while(p != None):
                if p.val == val:
                    pre.next = p.next
                else:
                    pre = p
                p = p.next
            return head

    def removeElements2(self, head: ListNode, val: int) -> ListNode:
        emptyLink = ListNode(0)
        emptyLink.next = head
        p = emptyLink
        while(p.next != None):
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return emptyLink.next
            
nums = []
if len(nums) == 0:
    head = None
else:
    head = ListNode(nums[0])
cur = head
for i in range(1, len(nums)):
    cur.next = ListNode(nums[i])
    cur = cur.next

s = Solution()
newHead = s.removeElements(head,2)
res = []
while(newHead):
    res.append(newHead.val)
    newHead = newHead.next
print(res)