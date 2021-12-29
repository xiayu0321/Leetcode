#!/usr/bin/env python
# coding:utf-8
from typing import List
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
class Solution2:
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

s = Solution2()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))