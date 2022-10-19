from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0 or head.next == None:
            return head
        
        newHead  = ListNode(-1,head)
        p = tail = newHead.next
        
        n = 0
        while(tail.next):
            n += 1
            tail = tail.next
            
        if k % (n+1) == 0:
            return head
        
        t = n - (k%(n+1)) + 1

        for i in range(t-1):
            p = p.next
       
        res = p.next
        p.next =  None
        tail.next = newHead.next

        return res
    def rotateRight2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0 or head.next == None:
            return head
        
        n = 0 
        cur = head
        
        while(cur):
            n += 1
            cur = cur.next
            
        epoch = k % n
        if epoch == 0:
            return head
    
        fast = slow = head 
        
        for _ in range(epoch):
            fast = fast.next
        
        while(fast.next):
            slow = slow.next
            fast = fast.next
        
        node = slow.next
        temp = node
        slow.next = None
        for _ in range(epoch-1):
            temp = temp.next
        temp.next = head
        return node        
            
            
            
    
    
if __name__ == '__main__':
    nums = [1,2,3,4,5]
    if len(nums) == 0:
        head = None
    head = p = ListNode(nums[0])
    for i in range(1,len(nums)):
        node = ListNode(nums[i])
        p.next = node
        p = p.next
    
    s = Solution()
    k = 4
    head = s.rotateRight2(head,k)
    print("res")
    while(head):
        print(head.val)
        head = head.next
    
    