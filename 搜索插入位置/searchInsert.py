#!/usr/bin/env python
# coding:utf-8
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if target < nums[i]:
                return i
        return i+1

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


s = Solution()
res = s.searchInsert1([1,3,5,6],7)
print(res)
