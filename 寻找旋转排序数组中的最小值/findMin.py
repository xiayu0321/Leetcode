from syslog import LOG_WARNING
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        standard = nums[0]
        i = 1
        while (i < len(nums) and nums[i] > standard ):
            i += 1
        if i == len(nums):
            return nums[0]
        else:
            return nums[i]

    def findMin2(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while (left < right):
            mid = (left  + right) // 2
        
            if nums[mid] < nums[right]:
                right = mid
        
            elif nums[mid] >= nums[right]:
                left = mid + 1
        return nums[left]
        
s = Solution()
nums = [11,13,15,17]
print(s.findMin(nums))