from random import *
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_index = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[max_index]:
                max_index = i
        return max_index
    
    def findPeakElement2(self, nums: List[int]) -> int:
        res = 0
        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            if nums[1] > nums[0]:
                return 1
            else:
                return 0
        
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                res = i
            elif nums[i] < nums[i+1]:
                res = i+1
        return res

    def findPeakElement3(self, nums: List[int]) -> int:
        n = len(nums)
        idx = randint(0,n-1)
        
        def get(i:int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]
        
        while(not (get(idx - 1) < get(idx) > get(idx + 1))):
            if get(idx) < get(idx - 1):
                idx = idx - 1
            else:
                idx = idx + 1
            
        return idx        
    
    def findPeakElement4(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while(l < r):
            mid = (l+r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        
        return l
    
s = Solution()
nums = [1,2]
print(s.findPeakElement3(nums))