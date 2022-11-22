## 有序链表转换二叉搜索树（中等）

### 题目

给定一个单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差不超过 1。

**提示:**

- `head` 中的节点数在$[0, 2 * 10^4]$范围内
- $-10^5 <= Node.val <= 10^5$

链接：https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree

### 思路

题目是要求将有序链表转化为高度相同的二叉搜索树，也就是将链表划分为长度尽量相同的两部分，逐一分配到树根节点的左右两边；然后在链表的两部分再寻找中点作为左右子树的根节点，依次迭代就可形成一棵高度相同的二叉搜索树。因此，考虑要多次迭代找到链表的中点（此时是节点），可通过快慢指针来寻找链表中点，并将中点值作为树的根节点，然后递归(left，mid)以及（mid.next，right）寻找链表中点，构建树的节点。最终返回root即可。

```python
def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
  def getMedian(left, right):
    fast = slow = left
    while(fast != right and fast.next != right):
      slow = slow.next
      fast = fast.next.next
    return slow
  
  def buildTree(left, right):
    if left == right:
      return None
    
    mid = getMedian(left, right)
    root = TreeNode(mid.val)
    root.left =  TreeNode(left, mid)
    root.right = TreeNode(mid.next, right)
    return root
  
  return buildTree(head, None)

```

另一种方式是观察生成的二叉搜索树，其中序遍历的结果就是原链表。因此，考虑结合中序遍历减少时间复杂度。在分治的过程中，无需先考虑链表的中位数节点，可以先用占位符，然后在中序遍历时再对该节点填充即可。在中序遍历时，可通过计算下标范围（此时构造链表的下标范围）进行计算中点：(left + right + 1)//2，左右子树所对应的链表范围应为：[left, mid-1]和[mid+1, right]。在 left>right 的情况下，此时遍历到要么一个空节点要么就是二叉搜索树中的一个节点。

```python
def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
  def getListLenght(head):
    c = 0
    while(head):
      c += 1
      head = head.next
    return c
  
  def buildTree(left, right):
    if left > right:
      return None
    mid = (left + right + 1) // 2
    root = TreeNode()
    root.left = buildTree(left, mid - 1)
    nonlocal head
    root.val = head.val
    head = head.next
    root.right = buildTree(mid+1, right)
    return root
  
  return buildTree(0, getListLenght(head) - 1)
    
```

