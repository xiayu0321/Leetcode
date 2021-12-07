#!/usr/bin/env python
# coding:utf-8
from typing import List


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


s = Solution2()
print(s.twoSum([2,7,11,15],9))
print(s.twoSum([3,3],6))
print(s.twoSum([3,2,4],6))
