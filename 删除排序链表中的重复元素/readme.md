## 删除排序链表中的重复元素（简单）

### 题目

存在一个按升序排列的链表，给你这个链表的头节点 `head` ，请你删除所有重复的元素，使每个元素 **只出现一次** 。

返回同样按升序排列的结果链表。

提示：

- 链表中节点数目在范围 `[0, 300]` 内
- `-100 <= Node.val <= 100`
- 题目数据保证链表已经按升序排列

链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/

### 思路

针对有序链表删除重复项，首先想到遍历链表。在遍历过程中，如果当前节点值`cur`与后一个节点值`cur.next`相等，则略过后一个节点值`cur.next`，即：`cur.next = cur.next.next`；如果当前节点值与后一个节点值不相等，那么当前节点`cur`就正常流动到下一个节点。由于需要访问到 `cur.next.next`，因此，判断时用 `cur.next是否为空进行判断。此外，要注意空链表的情况，如果初始链表为空，则直接返回空链表。

```python
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
```

在第二版解法中，在链表遍历过程中删掉重复项，我们需要找到相邻不重复的两个节点连接，即形成一个闭合区间，构成不重复链表。综上，我们要设置两个指针，`pre`指向前一个不重复节点，`cur`指向当前节点。如果当前节点值`cur.val`与前一个不重复节点值`pre.val`相等，那么就直接移动当前节点`cur`，同时也表明前一个不重复节点值`pre`还未遇到下一个不重复节点，所以需要将`pre.next`设置为 None。如果当前节点值`cur.val`与前一个不重复节点值`pre.val`不相等时，这表明前一个不重复节点值`pre`遇到下一个不重复节点了，因此直接将 `pre` 与` cur` 连接（`pre.next=cur	`），形成了一个不重复闭合区间。在完成一个闭合区间的同时要形成新的区间，因此，需要将 `pre` 移动到当前节点值`cur`，`cur` 移动到下一个节点中，重新寻找。此外，要注意空链表的情况。

```python
   def deleteDuplicates(self, head: ListNode) -> ListNode:
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
```











