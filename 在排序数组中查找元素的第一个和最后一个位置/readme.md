## 在排序数组中查找元素的第一个和最后一个位置（中等）

### 题目

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

- 你可以设计并实现时间复杂度为 `O(log n)` 的算法解决此问题吗？

提示：

* 0 <= nums.length <= $10^5$
* $-10^9$ <= nums[i] <= $10^9$
* `nums` 是一个非递减数组
* $-10^9$ <= target <=  $10^9$

链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

### 思路

由于题目要求是在**非递增数组**中找到一个数字**第一次出现**的位置和**最后一次出现**的位置，并且要设计时间复杂度为`O(log n)` 的算法，因此首先考虑使用双指针算法，找到**左指针**第一次指向 target的位置和**右指针**第一次指向 target 的位置即可。

由于`nums`是**非递增数组**，左指针在遍历数组时是按照数字非递减顺序，因此，找到最后一个小于` target` 的元素，再判断`num[left+1]`是否等于`target`，如果`num[left+1]==target`，那么此时`left+1`就是`pos`中的第一个值。

同理，右指针遍历数组时按照数字非递增顺序，因此，找到最后一个大于` target` 的元素，再判断`num[right-1]`是否等于`target`，则如果`num[right-1]==target`，此时`right-1`就是`pos`中的第二个值。

如果当前左右指针都没有找到 target，则继续遍历数组，即`left+=1`和`right-=1`。

此外 ，要考虑特殊情况：（1）`target` 在` nums`只出现了一次，并且出现在`nums` 的头或尾；（2）`nums`中只有一个元素，并且元素值等于`target`。

针对第一种情况，无论target 出现在头或者尾，此时都会出现`left==right`，区别就是等于0还是等于`len(nums)-1`。在判断此时两指针指向的值是否为 target，如果是，则此时 `pos=[left，left]`或者` pos=[right,right]`。否则就是不存在。

针对第二种情况，出现`left==right`，并且同时等于 target，此时`pos=[left，right]`。

```python
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = [-1,-1]
        l = len(nums)
        left = 0
        right = l - 1

        while(left < right):
           # 特殊情况二：nums 只有一个元素，且正好等于 target
            if nums[left] == nums[right] == target:
                pos = [left,right]
                break
           #  找到target第一次出现的下标
            if nums[left] < target:
                if nums[left + 1] == target:
                    pos[0] = left + 1
                left += 1
           # 找到 target 最后一次出现的下标
            elif nums[right] > target:
                if nums[right - 1] == target:
                    pos[1] = right - 1
                right -= 1
           # 左右指针移动
            else:
                left += 1
                right -= 1            
				# 特殊情况一：target 只出现一次，同时只在首尾出现
        if left == right == 0 and nums[left] == target:
             pos = [left,left]
        elif  left == right == l - 1 and nums[left] == target:
            pos = [right,right]
        return pos
```

由于数组是非递减数组，因此通过**二分查找**加速查找元素过程。题目要找target在nums 第一次出现和最后一次出现的位置，即找到数组中「第一个等于`target `的位置」（`leftIdx`）和「第一个大于`target `的位置减一」（记为` rightIdx`）。

由于都是找下标位置，因此可以将二分查找过程单独提出为一个函数。但**注意**：寻找 `leftIdx `即为在数组中寻找第一个大于等于`target` 的下标，寻找`rightIdx `即为在数组中寻找第一个大于`target `的下标，然后将下标减一。两者的判断条件不同，因此在二分查找函数中设置一个标志位`lower`， 如果`lower `为` true`，则查找第一个大于等于 `target` 的下标，否则查找第一个大于 `target `的下标。

最后，因为`target` 可能不存在数组中，因此需要重新校验得到的两个下标`leftIdx` 和 `rightIdx`，看是否符合条件，如果符合条件就返回`[leftIdx,rightIdx]`，不符合就返回 `[-1,-1]`。

```python
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = [-1,-1]
        leftIdx = self.binarySearch(nums,target,1)
        rightIdx = self.binarySearch(nums,target,0) - 1
        if (leftIdx <= rightIdx and rightIdx < len(nums) and nums[leftIdx] == target and nums[rightIdx] == target):
            pos = [leftIdx,rightIdx]
        return pos
    
    def binarySearch(self, nums: List[int], target: int, lower: int) -> int :
        ans = len(nums)
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = math.floor((left + right) / 2)
            if (nums[mid] > target or ((lower) and nums[mid] >= target)) :
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans
```

