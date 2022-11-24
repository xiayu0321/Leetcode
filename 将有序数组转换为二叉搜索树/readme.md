## 将有序数组转换为二叉搜索树（简单）
### 题目
给你一个整数数组nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

**提示**：

* $1 <= nums.length <= 10^4$
* $-10^4 <= nums[i] <= 10^4$
* `nums` 按 严格递增 顺序排列

链接：https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree

### 思路
题目要求将有序的数组转化为左右子树高度相差不能超过1的二叉搜索树。因此需要将有序数组进行等量长度划分，即找到数组中点（通过`（left+right）// 2`计算数组中点），该中点为二叉搜索树的根节点，并且前半部分数组和后半部分数组构成二叉搜索树的左右子树。以此迭代，直至数组中所有的元素都已构成节点。因此，可采用递归方法。

```python
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(left, right):
        	# 确定递归推出条件
            if left > right:
                return None
            # 寻找数组中点
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            # 迭代构建左右子树
            root.left = buildTree(left, mid - 1)
            root.right = buildTree(mid + 1, right)
            return root
        return buildTree(0, len(nums) - 1)
```
