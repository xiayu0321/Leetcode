## 删除链表中的节点（简单）

### 题目

请编写一个函数，用于 **删除单链表中某个特定节点** 。在设计函数时需要注意，你无法访问链表的头节点 head ，只能直接访问 要被删除的节点 。

题目数据保证需要删除的节点**不是末尾节点**。

提示：

* 链表中节点的数目范围是 [2, 1000]
* -1000 <= Node.val <= 1000
* 链表中每个节点的值都是 唯一 的
* 需要删除的节点 node 是 链表中的节点 ，且 不是末尾节点

链接：https://leetcode-cn.com/problems/delete-node-in-a-linked-list

### 思路

由于无法访问链表的头结点，只能访问要被删除的节点，而删除特定节点时需要知道删除节点的前驱节点，此时由于不知道链表的头节点，因此无法访问到删除节点的前驱节点。因此可以考虑交换当前节点和它下一个节点的值，此时下一个节点才是要被删除的节点，当前节点是删除节点的前驱节点，因此删除下一个节点即可。