from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:     
        for i in range(1,len(nums)):
            for j in range(len(nums)-i):
                if nums[j+1] < nums[j]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
    
    
    def sortColors2(self, nums: List[int]) -> None:
        pre = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[pre],nums[i] = nums[i],nums[pre]
                pre += 1
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[pre],nums[i] = nums[i],nums[pre]
                pre += 1
                      
s = Solution()
nums = [2,0,2,1,1,0]
s.sortColors2(nums)
print(nums)