
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = head
        temp = 0

        if p == None or p.next == None:
            return p

        while(p != None):
            temp = p.val
            p.val = p.next.val
            p.next.val = temp
            if p.next.next and p.next.next.next:
                p = p.next.next
            else:
                p = None
        return head

nums = [5,4,6,7,8]
if len(nums) == 0:
    head = None
else:
    head = ListNode(nums[0])
cur = head
for i in range(1, len(nums)):
    cur.next = ListNode(nums[i])
    cur = cur.next

s = Solution()
newHead = s.swapPairs(head)
res = []
while(newHead):
    res.append(newHead.val)
    newHead = newHead.next
print(res)
