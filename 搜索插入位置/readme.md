## 搜索插入位置（简单）

### 题目

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 `O(log n)` 的算法。

提示：

* 1 <= nums.length <= 104

* -104 <= nums[i] <= 104

* nums 为无重复元素的升序排列数组
* -104 <= target <= 104

链接：https://leetcode-cn.com/problems/search-insert-position

### 思路

在数组寻找目标值时，首先想到遍历数组后与 target 进行比较。如果与target 相等，则直接恩返回下标值，如果不等，只要找到第一个比target 大的数值，此时它的下标就是需要插入的下标。如果遍历完没有找到合适的位置，则证明 target 是数组中最大的元素，因此只需要插入到数组最后，即返回数组长度。由以上思想得到第一版解法。

```python
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if target < nums[i]:
                return i
        return i+1
```

对于在数组中寻找目标值，还可以使用二分查找的方法。分别设置左右指针 left 和 right，只要左指针小于右指针，就一直进行遍历。然后在遍历过程中设置中间的位置mid，即：(left+right)/2的位置就是左右指针指向的数组中间的位置。如果 nums[mid]大于等于 target，此时说明 mid 的位置可能就是最终插入位置，同时插入位置不可能在 mid 的右边，因此需要调整右指针的位置到 mid-1。同理，如果 nums[mid]小于 target，则说明插入位置不会出现在 mid 的左边，因此需要调整左指针位置到 mid+1。在遍历完后，得到的结果就是最终的插入位置结果。

```python
    def searchInsert1(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        res = len(nums)

        while(left <= right):
            mid = (left + right) >> 1
            if (nums[mid] >= target):
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res
```

