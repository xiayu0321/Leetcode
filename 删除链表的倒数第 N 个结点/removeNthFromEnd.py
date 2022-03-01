from inspect import stack
from platform import node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        l = 1
        newHead = ListNode(0,head)

        while(p.next):
            l += 1
            p = p.next
        position = l - n - 1

        if position ==  -1:
            newHead.next = newHead.next.next
            
        else:
            p = head
            
            for i in range(position):
                p = p.next
            p.next = p.next.next

        return newHead.next

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        newHead = ListNode(0,head)
        stack = []
        cur = newHead
        while(cur):
            stack.append(cur)
            cur = cur.next
        
        for i in range(n):
            stack.pop()
        
        pre = stack[-1]
        pre.next = pre.next.next
        return newHead.next


nodes = [1]
if len(nodes) == 0:
    head = None
else:
    head = ListNode(nodes[0])

cur = head
for i in range(1,len(nodes)):
    cur.next = ListNode(nodes[i])
    cur = cur.next

s = Solution()
head = s.removeNthFromEnd2(head,1)
res = []
while(head):
    res.append(head.val)
    head = head.next
print(res)