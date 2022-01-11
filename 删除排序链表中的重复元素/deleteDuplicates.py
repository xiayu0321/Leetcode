#!/usr/bin/env python
# coding:utf-8

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(head == None):
            return head
        cur = head

        while(cur.next):
           if(cur.val == cur.next.val):
               cur.next = cur.next.next
           else:
               cur = cur.next
        return head
    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        if(head == None):
            return head
        pre = head
        cur = head.next

        while(cur):
            if pre.val == cur.val:
                cur = cur.next
                pre.next = None
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        return head

s = Solution()
nums = [1,1,1,2,2,2,2,2,2,4,4,4,4,4,5,5]
head = new = ListNode(nums[0])
for i in range(1,len(nums)):
    new.next = ListNode(nums[i])
    new = new.next

head = s.deleteDuplicates1(head)

while (head != None):
    print(head.val)
    head = head.next
