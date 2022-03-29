from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        slow = 2
        fast = 2
        
        while(fast < len(nums)):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow
                
s = Solution()
nums = [0,1,1,2,3,3,4,4,4,4,4]
print(nums[:s.removeDuplicates(nums)])