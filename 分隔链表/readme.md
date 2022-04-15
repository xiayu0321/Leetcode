## 分隔链表（中等）

### 题目

给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

**提示：**

- 链表中节点的数目在范围 `[0, 200]` 内
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`

链接：https://leetcode-cn.com/problems/partition-list

### 思路

起初考虑在原链表中进行，想借鉴数组中始终保持某一下标前的所有元素是符合要求的想法。由于题目中要求大于 x 的值在右边，小于 x 的值在左边，同时还要保持相对顺序。因此，需要调换节点位置，因此需要有`pre` 和` cur`指针。

在遍历原始链表中，首先找到第一个大于 x的节点`cur1`（同时它的前置节点`pre1`也确定），然后在继续遍历，找到第一个小于 x 的节点`cur2`（同时它的前置节点`pre2`也确定），此时由于需要保持节点的相对位置，因此需要将小于 x 的节点插入到大于 x 的节点前，同时在此处将小于 x 的节点删掉。

即要进行：`pre2.next = cur2.next `,   `pre1.next = cur2 `,`               cur2.next = cur1 `,`               pre1 = pre1.next`等4步。

在进行插入操作完后，要考虑此时 pre1，cur2，pre2在链表中的顺序已经被打乱了，但 cur1还指向大于x 的节点，pre1还是它的前置节点，此时它仍作为插入位置。再继续遍历后续节点，找到第一个小于 x 的节点，再同时进行插入节点和删除节点的操作。直至cur1节点遍历到链表的最后。

但在这种情况下，需要另外考虑head 链表为空、 head 链表中只有一个元素和 head 中没有x 元素的情况，此时都是直接返回 原链表即可。

```python
    def partition(self, head: ListNode, x: int) -> ListNode:
    # head 链表为空、 head 链表中只有一个元素的情况
        if not head or not head.next:
            return head
        newHead = ListNode(0,head)
        pre1 = newHead
        cur1  = head
        
        while(cur1):
            while(cur1):
            # 找到第一个大于x的值，作为插入位置
                if cur1.val >= x:
                    break    
                cur1 = cur1.next
                pre1 = pre1.next
           # head 中没有x元素
            if cur1 == None:
                break
           # 在找到大于 x 的节点后，需要从此处开始遍历找到第一个小于 x 的节点
            pre2 = cur1
            cur2 = pre2.next
            
            while(cur2):
                if cur2.val < x:
                    break    
                cur2 = cur2.next
                pre2 = pre2.next
            # 此时找到小于 x 的节点，要进行插入和删除（此时当然要在该节点存在的情况下）
            if cur2:
                pre2.next = cur2.next
                pre1.next = cur2
                cur2.next = cur1
                pre1 = pre1.next
            else:  # 不存在的时候直接返回
                return newHead.next
        return newHead.next  # head 中没有x元素时直接返回原链表
```

由于上述方法的时间复杂度和空间复杂度较高，因此可以考虑重建两个链表 small 和 large，一个保存小于 x 的节点，另一个 保存大于等于 x 的节点。在遍历原链表时，只要取出相应节点到相应链表中即可。最后将 large 链表赋给 small 链表的末尾即可。



