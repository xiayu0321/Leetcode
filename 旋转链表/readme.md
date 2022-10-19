## 旋转链表（中等）

### 题目

给你一个链表的头节点 `head` ，旋转链表，将链表每个节点向右移动 `k` 个位置。

**提示：**

- 链表中节点的数目在范围 `[0, 500]` 内
- `-100 <= Node.val <= 100`
- $0 <= k <= 2 * 10^9$

链接：https://leetcode.cn/problems/rotate-list/

### 思路

旋转链表也就是将链表截断，将后半部分链表插入到前半部分链表前。对于是从哪里截断，可以比较 k 与链表长度来计算。例如 head=[1,2,3,4,5]，k=2的情况，应该是从3后截断，因此考虑【链表长度-k】来确定，但要考虑 k 值等于以及大于链表长度，若 k 为链表长度，则无需变化，若超出，则需要k 对链表长度取余，只需要在余数部分进行截断。在确定了截断位置后，就需要将两部分链表进行重新链接。需要将后半部分链表的第一个元素作为新链表头部，并将前半链表的末尾元素.next 设置为 None，最后将后半部分的链表末尾链接到前半链表头部即可。此时还要考虑几种特殊情况：head 为空、k=0以及head.next == None，在这三种情况下，直接可以返回原链表。

```python
def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
  # 三类特殊情况
  if head == None or k == 0 or head.next == None:
    return head
  
  newHead  = ListNode(-1,head)
  p = tail = newHead.next  # p为遍历指针要找到前半部分的最后一个元素，tail 指向旧链表的最后元素
  n = 0 # 链表长度
  
  while(tail.next):  # 由于遍历到了倒数第一个元素，并没有遍历完，因此链表长度实质为 n+1
    n += 1
    tail = tail.next
  
  if k % (n+1) == 0: # 此时为旋转次数正好为链表长度的倍数情况，此时完全可以不用变
    return head
  
  t = （n+1）- k%(n+1)  #计算旧链表的截断位置
  
  for _ in range(t-1): #找到前半部分链表的末尾元素:
    p = p.next
  
  # 将两段链表链接
  res = p.next
  p.next = None
  tail.next = newHead.next
  
  return res
```

另一种方式是构建循环链表以及快慢指针。在循环链表中，fast 指针永远比 slow 指针快k 步，然后快慢指针同时出发，当快指针到终点时，慢指针正好指向要反转的链表的前一个节点。然后以快指针所在位置将链表分割，交换两个链表位置再链接即可。

```python
def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
  # 三类特殊情况
  if head == None or k == 0 or head.next == None:
    return head
  
  cur = head
  size = 0  #链表长度
  
  while(cur):
    size += 1
    cur = cur.next
  
  epoch = k % size
  
  #旋转次数正好为链表长度的倍数情况，此时无需旋转
  if epoch == 0:
    return head
  
  slow = head
  fast = head
  
  # 快指针比慢指针快 k 步
  for _ in range(epoch):
    fast = fast.next
 
  # 直到快指针到原链表末尾元素
  while(fast.next):
    fast = fast.next
    slow = slow.next
  
  node = slow.next  #此时是原链表的后半部分的头元素，即新链表的头部
  temp = node
  slow.next = None  #原链表的前半部分的最后元素赋值为 None
  
  for _ in range(epoch-1): #找到后半链表的最后一个元素
    temp = temp.next
  temp.next = head # 将后半链表与前半链表链接
  return node  
```