## 最大子数组和

### 题目

给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**子数组** 是数组中的一个连续部分。

提示：

* 1 <= nums.length <= $10^5$
* $-10^4$ <= nums[i] <= $10^4$

链接：https://leetcode-cn.com/problems/maximum-subarray/

### 思路

起初，我考虑的就是找到所有的连续子数组，每一个新子数组与当前最大子数组和进行比较，就能找到最大子数组和。即通过两个循环遍历，首先遍历整个数组，针对每个数字再遍历余下数组，构成不同的子数组，再比较新的子数组和和目前最大的子数组和进行。如果新子数组和大，就把新子数组和赋给最大子数组和，直到两重循环遍历完。特殊要考虑数组只有一个元素时，这时无需比较，只需要返回当前值。

```python
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = -sys.maxsize - 1
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            sum = 0
            for j in nums[i:]:
                sum = sum + j
                if (sum > max):
                    max = sum
        return max
```

但这种方式时间复杂度太高，对于大数据量的数组容易造成超出时间限制问题。因此，需要考虑如何减少循环。

此时需要反向思考，遍历时的每个元素不是作为子数组的第一个元素，而是作为子数组的最后一个元素，如果这个元素之前的子数组和小于0，就直接丢弃之前的数组，从当前数组开始作为新数组，如果这个元素之前的子数组和大于0，就保留之前的数组，并累加上当前元素，最后再比较当前子数组值与最大子数组和，使最大数组和始终保持最大子数组。此时经过一次循环，有效降低了时间复杂度。

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxSum = nums[0]
        pre = 0
        for num in nums:
            pre = max(pre,0)
            pre = pre + num
            maxSum = max(pre,maxSum)
        return maxSum
```

