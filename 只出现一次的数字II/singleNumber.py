from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = {}
        for i  in nums:
            if i not in mapping.keys():
                mapping[i] = 1
            else:
                 mapping[i] += 1
        for key in mapping.keys():
            if mapping[key] == 1:
                return key
    
    def singleNumber2(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums
        nums = sorted(nums)
        if nums[0] != nums[1]:
            return nums[0]

        for i in range(1,len(nums) - 1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]
                
            

s =  Solution()
nums = [1]
print(s.singleNumber2(nums))