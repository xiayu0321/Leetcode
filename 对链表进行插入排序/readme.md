## 对链表进行插入排序（中等）

### 题目

给定单个链表的头 head ，使用**插入排序**对链表进行排序，并返回**排序后链表的头** 。

插入排序 算法的步骤:

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。

对链表进行插入排序。

**提示：**

- 列表中的节点数在 `[1, 5000]`范围内
- `-5000 <= Node.val <= 5000`

链接：https://leetcode-cn.com/problems/insertion-sort-list

### 思路

使用插入排序对链表进行排序，则需要确定插入的位置，哪个元素需要插入、插入元素的后续节点。

由于插入位置需要前序节点来确定，因此需要用 dummyNode。

在遍历链表时，首先需要确定哪个元素需要取出来插入，即比较相邻元素值的大小(cur.val 与 cur.next.val)。

如果后面元素值小于前面元素值（cur.val > cur.next.val)），则需要将后面元素插入到前面元素之前。在确定了插入元素后，然后需要寻找插入点。由于元素插入位置不同，因此需要遍历当前元素之前的链表，直到找到大于插入元素值的位置（即 pre.next.val > cur.next.val）。此时进行插入操作。从链表中先取出该元素然后进行插入操作。插入操作后需要将 pre 指针重新移动到链表的最前面，以便下一循环重新寻找插入点。

如果后面元素值大于前面元素值，说明无需排序，继续遍历即可。

注意：由于题目要求链表数大于1，所以无需考虑链表不存在的情况。

```python
    def insertionSortList(self, head: ListNode) -> ListNode:
       # 构造哑节点
        dummpyNode = ListNode(-5001,head)
        pre = dummpyNode
        cur = head

        while(cur.next):
          # 比较相邻元素的大小，寻找哪个元素需要移动
            if cur.val > cur.next.val:
                node = cur.next
                # 确定插入位置
                while(pre.next.val < node.val):
                    pre = pre.next
                # 插入排序操作
                cur.next = node.next
                node.next = pre.next
                pre.next = node
                # 移动 pre，为下一轮寻找插入位置做准备
                pre = dummpyNode      
              
            else:
                cur = cur.next
        return dummpyNode.next
```

