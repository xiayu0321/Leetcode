# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        while(head != None):
            stack.append(head.val)
            head = head.next

        newhead = p = ListNode(-1)
        while(stack):
            node = ListNode(stack.pop())
            p.next = node 
            p = p.next
        return newhead.next

    def reverseList2(self, head: ListNode) -> ListNode:
        p = head
        pre = None
        
        while(p != None):
            latter = p.next
            p.next = pre
            pre = p
            p = latter
        return pre

nodes = [1,2,3,4,5]
if len(nodes) == 0:
    head = None
else:
    head = ListNode(nodes[0])

cur = head
for i in range(1,len(nodes)):
    cur.next = ListNode(nodes[i])
    cur = cur.next

s = Solution()
newhead = s.reverseList(head)
res = []
while(newhead!= None):
    res.append(newhead.val)
    newhead = newhead.next
print(res)
