## 搜索旋转排序数组（中等）

整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标` k（0 <= k < nums.length）`上进行了 旋转，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

提示：

* $1 <= nums.length <= 5000$
* $-10^4 <= nums[i] <= 10^4$
* nums 中的每个值都 独一无二
* 题目数据保证 nums 在预先未知的某个下标上进行了旋转
* $-10^4 <= target <= 10^4$

链接：https://leetcode.cn/problems/search-in-rotated-sorted-array

### 思路

首先确定旋转数组的概念，即：将一个升序数组从某一节点截断然后将两端有序数组交换并形成新的数组，此时该数组可以看成是两个升序数组的组合，同时新数组的起始元素一定大于末尾元素。因此在有序数组形式下搜索元素下标并考虑时间复杂度，可以考虑二分查找。

但与基础二分查找不同的是：需要在移动 left 和 right 时要多一次判断，是需要判断nums[mid]到底是在左边有序数组内还是右边有序数组内。因此，先通过nums[mid]与nums[0]进行比较，然后再根据nums[mid]、target 、nums[left]（nums[right]）三者之间大小关系来移动 left 和 right。

```python
def search(self, nums: List[int], target: int) -> int:
  if len(nums) == 0:
    return -1
  
  left = 0
  right = len(nums - 1)
  
  while(left <= right):  # 基本二分法
    mid = (left + right) // 2
    if nums[mid] == target:
      return mid
    
    if nums[mid] >= nums[0]:  # 在nums[mid]在左边有序数组
      if nums[left] <= target < nums[mid]:  # 判断target与nums[mid]的大小
        right = mid - 1
      else:
        left = mid + 1
    else:                  # 在nums[mid]在右边有序数组
      if nums[mid] < target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1
        
  return -1
    
    
```









