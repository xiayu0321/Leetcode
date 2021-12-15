#!/usr/bin/env python
# coding:utf-8
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        index = 0
        for i in range(1,n):
            if nums[i] != nums[index]:
                nums[index+1] = nums[i]
                index += 1
        return index+1

s = Solution()
nums = [1,2,3]
res = s.removeDuplicates(nums)
print(nums[:res])
