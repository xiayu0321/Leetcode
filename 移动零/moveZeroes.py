from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
        print(nums)
                
s = Solution()
nums = [0,0,1]
print(s.moveZeroes(nums))
        