## 反转链表 II（中等）

### 题目

给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

**提示：**

- 链表中节点数目为 `n`
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

链接：https://leetcode-cn.com/problems/reverse-linked-list-ii

### 思路

首先，鉴于反转链表的思路，不用改变链表的链接，而是在第一遍遍历时将要反转部分的 val 保存到栈中，第二次再遍历链表时，把节点的值改为栈中弹出的值即可。

这种方法没有从根本上改变链表的链接情况。第二种考虑改变链接情况。由于仅反转 left 和 right 之间的链表，因此大体思路可以划分为：将 left至 right 的链表单独取出来，将其反转，最后将反转的结果重新放回链表中。从该过程中发现，需要保存 left 的前驱节点、left 节点和 right 节点以及其后序节点，以保证可以将不反转部分和反转部分分开操作。综上，应先遍历链表，遍历到 left 位置处，保留 left_pre 和 left_node 节点，再遍历到 right 处，保存 right 节点以及后序right_succ 节点。然后通过`left_pre.next = None,right_node.next = None`将 left_node和 right_node之间的链表取出。此时就可以对这一段链表单独进行反转操作。**反转操作是重点**。在反转操作中，要牵扯三个节点，当前节点和其前后节点。反转中首先要保留当前节点的 next，然后将当前节点的next 指向 pre。最后在移动指针，pre = cur，cur=之前保留的当前节点的 next。在经历反转之后，在将该部分链表返回到原链表中。通过`left_pre.next = right_node,left_node.next =right_succ`实现。

```python
  #！！！！反转链表的基本步骤重点
  			cur = head
  			pre = None
  			while(cur):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
```

以上方法时间复杂度较高，可以考虑只遍历一次链表的情况。反转链表可以表示为在遍历时取出当前节点插入到链表头部。在实现头插法时，需要牵扯到插入的位置，插入的节点，和当前节点的后续节点。整体过程大概如下：先找到 left_node 以及其 pre，此时 pre 将不会变化，作为头插法的插入位置；然后进入到反转节点的部分，此时遍历每个节点时，将其头插到 left_node 的节点处，直到 right_node 处即可。

