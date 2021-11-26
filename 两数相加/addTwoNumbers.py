#!/usr/bin/env python
# coding:utf-8

import math
class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1 = self.readLinkNodeValue(l1)
        v2 = self.readLinkNodeValue(l2)
        tmp = str(self.reverseNumber(v1)+self.reverseNumber(v2))[::-1]

        head = ListNode()
        head.val = int(tmp[0])
        tmp = tmp[1:]
        curNode = head
        for i in tmp[:]:
            node = ListNode()
            node.val = int(i)
            curNode.next = node
            curNode = curNode.next
        return head

    def readLinkNodeValue(self,l:ListNode):
        h = l
        value = ""
        while(h != None):
            value = value+str(h.val)
            h = h.next
        return value

    def reverseNumber(self,v:str)-> int:
        r = v[::-1]
        return int(r)

def list2link(List):
    head = ListNode(List[0])
    p = head
    for i in range(1, len(List)):
        p.next = ListNode(List[i])
        p = p.next
    return head

s = Solution()
l1 = list2link([2,4,3])
l2 = list2link([5,6,4])

l = s.addTwoNumbers(l1,l2)
while(l != None):
    print(l.val)
    l = l.next
