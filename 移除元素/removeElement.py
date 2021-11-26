#!/usr/bin/env python
# coding:utf-8

class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        left = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[left] = nums[i]
                left = left + 1
        return left

s = Solution()
nums = [3,2,2,3]
m = s.removeElement(nums,2)
print(nums[0:m])










