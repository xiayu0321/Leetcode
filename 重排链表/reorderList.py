from curses import noecho
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        count = 1
        p = head
        nums = []
        while(p):
            nums.append(p.val)
            p = p.next
            
        nums1 = nums[:math.ceil(len(nums)/2)]
        nums2 = nums[math.ceil(len(nums)/2):]
        
        p = head
        while(p):
            if count % 2 == 1:
                p.val = nums1[0]
                del nums1[0]
            else:
                p.val = nums2[-1]
                del nums2[-1] 
            p = p.next
            count += 1
    
    def reorderList2(self, head: ListNode) -> None:
        if head == None:
            return
        
        elements = []
        p = head
        while(p):
            elements.append(p)
            p= p.next
        i = 0
        j = len(elements) - 1
        while(i < j):
            elements[i].next = elements[j]
            i += 1
            if i == j:
                break
            elements[j].next = elements[i]
            j -= 1
        elements[i].next = None
    def reorderList3(self, head: ListNode) -> None:
        if head == None:
            return
        
        # 快慢指针先找到链表中点
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        
        l1 = head
        # 将后半链表进行倒序
        l2 = slow.next
        slow.next = None
        prev = None
        curr = l2
        while(curr):
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
            
        # 将链表两端合并
        l2 = prev
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp
    
s = Solution()
nums = [1,2,3,4,5]
if len(nums) < 1:
    head = None
else:
    head = p = ListNode(nums[0]) 
    for i in range(1,len(nums)):
        p.next = ListNode(nums[i])
        p = p.next
s.reorderList3(head)
p = head
while(p):
    print(p.val) 
    p = p.next       
     
