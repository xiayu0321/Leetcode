## 两数之和（简单）

### 题目

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target  的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

链接：https://leetcode-cn.com/problems/two-sum

### 思路

对于数组，首先想到遍历数组，在遍历时，再通过 『target-当前值』得到第二个数值，再通过遍历余下数组判断第二个数值在数组中的位置。在判断第二个数值的位置时，可以从第一个数值的位置到数组最后遍历判断，无需遍历整个数组。因此，得到第一版解法。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        for i,num in enumerate(nums):
            j = i + 1
            for k,v in enumerate(nums[j:]):
                if(v == target - num):
                    index.append(i)
                    index.append(k+j)
                    return index
        return index
```

在第二版解法中，想使用双指针算法，下标同时从左和从右向中间遍历。首先预设指针左指针 i=0和右指针 j = len(nums) -  1，在同时遍历时，终止条件是 i > j。首先判断两个指针所对应的数值之和是否为 target，如果是，直接返回两个指针，如果不是，则需要将右指针向左移动，移动一次判断一次，直到移动到左指针的位置。如果到左指针位置时，还没找到，则需要将左指针向右移动一个，继续遍历寻找。

```python
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        i = 0
        j = len(nums) - 1

        while (i <= j):
            if(nums[i] + nums[j] == target):
                index.append(i)
                index.append(j)
                return index
            else:
                j = j - 1
                if (j == i):
                    i = i + 1
                    j = len(nums) - 1

        return index
```

