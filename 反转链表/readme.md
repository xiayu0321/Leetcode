## 反转链表（简单）

### 题目

给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

**提示：**

- 链表中节点的数目范围是 `[0, 5000]`
- `-5000 <= Node.val <= 5000`

 链接：https://leetcode-cn.com/problems/reverse-linked-list/

### 思路

反转链表，即将链表中节点的 `val` 进行反转，因此考虑创建一个新链表作为反转后的链表。通过**栈**结构存储原链表每个节点的值，再通过将栈中的元素弹出，创建新节点，构建新链表。

```python
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
```

该种方法没有在原地进行，因此有较高的空间复杂度，考虑第二种在原地的转换。

在原地反转，也就是需要改当前节点的 `next` 指向，此时需要涉及到三个节点：前一个节点`pre`、当前节点`p`和当前节点的后一个节点`latter`。遍历链表，先保存当前节点的后一个节点，再改当前节点的next指向前一个节点，最后在调整前一个节点`pre`和当前节点`p`的指向。

```python
    def reverseList2(self, head: ListNode) -> ListNode:
        p = head
        pre = None
        
        while(p != None):
            latter = p.next
            p.next = pre
            pre = p
            p = latter
        return pre

```

