## 两数相加（中等）

### 题目描述

给你两个**非空**的链表，表示两个非负的整数。它们每位数字都是按照**逆序**的方式存储的，并且每个节点只能存储**一位**数字。请你将两个数相加，并以相同形式返回一个表示和的链表。你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

链接：https://leetcode-cn.com/problems/add-two-numbers

### 思路

首先需要从两个链表参数中读取每一个节点中的值，由于读取两个链表是重复操作，因此把读取链表值单独作为一个方法。

在读取链表节点值方法中，读取节点值是链表的遍历操作，由于后续需要做反转，而利用字符串反转较方便，因此采用 str 存放节点值。

在读取完参数链表的节点值后，需要对两个值进行反转，由于是单独功能并且二者是重复操作，因此把反转单独提取为一个方法，此时由于读取的节点值是以字符串表示，在反转时直接采用字符串反转，就可以达到数据反转的效果。

反转后，再将反转的字符串转成 int 进行数值计算。得到计算结果后进行输出。

在输出时，第一版我是采取直接用 int 类型数值，倒序取出每一位，并对每一位数值创建节点并连接，最后返回头结点。但这种方式在计算超出 int 范围的数就会出现问题，例如：输入两个列表分别是[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]和[5,6,4]，相加时没有问题，但在后续输出时出现问题。

因此，我采用第二版算法，在输出时利用 str 的特点（对于数据长短没有限制），在计算数值后仍采用 str 形式，并将其倒序，然后顺序按位取出每一个字符（注意：在节点赋值时需要转换为 int），为每个元素创建节点，构建链表。

```python
# 第一版
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import math
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1 = self.readLinkNodeValue(l1)
        v2 = self.readLinkNodeValue(l2)
        # 第一版的输出
        tmp = self.reverseNumber(v1)+self.reverseNumber(v2)

        headNode = ListNode()
        headNode.val = tmp%10
        curNode = headNode
        tmp = math.floor(tmp / 10)
        while(tmp != 0):
            node = ListNode()
            node.val = tmp%10
            curNode.next = node
            curNode = curNode.next
            tmp = math.floor(tmp / 10)
        return headNode
      	
         # 第二版的输出
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
```





