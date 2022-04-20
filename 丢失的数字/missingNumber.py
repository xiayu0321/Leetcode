from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(0,l+1):
            if i not in nums:
                return i
    
    def missingNumber2(self, nums: List[int]) -> int:
        sorted(nums)
        for i,num in enumerate(nums):
            if i != num:
                return i
        return len(nums)
     
s = Solution()
nums = [0]
print(s.missingNumber2(nums))
        
        
        