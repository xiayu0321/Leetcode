#!/usr/bin/env python
# coding:utf-8
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l = len(nums)
        nums.sort()
        minDvalue = abs(nums[-1]+nums[-2]+nums[-3] - target)
        minres = 0

        for first in range(l):
            twoSum = target - nums[first]

            for second in range(first+1,l):
                third = l - 1
                while(second < third):
                    # 比较两数之和与目标值的差值
                    Dvalue = twoSum - nums[second] - nums[third]
                    absDvalue = abs(Dvalue)
                    if absDvalue <= minDvalue:
                        minDvalue = absDvalue
                        minres = nums[first] + nums[second] + nums[third]
                    third -= 1
        return minres

s = Solution()
print(s.threeSumClosest([0,2,1,-3],1))
print(s.threeSumClosest([0,0,0,0],1))
print(s.threeSumClosest([-4,2,1,-1],1))








