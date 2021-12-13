#!/usr/bin/env python
# coding:utf-8
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        cur1 = list1
        head = new = ListNode(-1)
        cur2 = list2

        while cur1 != None and cur2 != None:
            if(cur1.val <= cur2.val):
                new.next = cur1
                cur1 = cur1.next
            else:
                new.next = cur2
                cur2 = cur2.next
            new = new.next
        if cur1 != None:
            new.next = cur1
        else:
            new.next = cur2
        return head.next

n11 = ListNode(1)
n12 = ListNode(6)
n13 = ListNode(7)
n14 = ListNode(9)
n15 = ListNode(11)

n11.next = n12
n12.next = n13
n13.next = n14
n14.next = n15

n21 = ListNode(0)
n22 = ListNode(2)
n23 = ListNode(3)
n24 = ListNode(7)
n25 = ListNode(9)
n26 = ListNode(11)
n27 = ListNode(15)
n21.next = n22
n22.next = n23
n23.next = n24
n24.next = n25
n25.next = n26
n26.next = n27

s = Solution()

p = s.mergeTwoLists(n11,n21)
while(p!=None):
    print(p.val)
    p = p.next

