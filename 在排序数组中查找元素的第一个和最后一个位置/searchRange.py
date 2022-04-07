
import math
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = [-1,-1]
        leftIdx = self.binarySearch(nums,target,1)
        rightIdx = self.binarySearch(nums,target,0) - 1
        if (leftIdx <= rightIdx and rightIdx < len(nums) and nums[leftIdx] == target and nums[rightIdx] == target):
            pos = [leftIdx,rightIdx]
        return pos
    
    def binarySearch(self, nums: List[int], target: int, lower: int) -> int :
        ans = len(nums)
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = math.floor((left + right) / 2)
            if (nums[mid] > target or ((lower) and nums[mid] >= target)) :
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans


    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        pos = [-1,-1]
        l = len(nums)
        left = 0
        right = l - 1

        while(left < right):
            if nums[left] == nums[right] == target:
                pos = [left,right]
            if nums[left] < target:
                if nums[left + 1] == target:
                    pos[0] = left + 1
                left += 1
            elif nums[right] > target:
                if nums[right - 1] == target:
                    pos[1] = right - 1
                right -= 1
            else:
                left += 1
                right -= 1            

        if left == right == 0 and nums[left] == target:
             pos = [left,left]
        elif  left == right == l - 1 and nums[left] == target:
            pos = [right,right]
        return pos

s = Solution()
nums = [2,2]
target = 2
print(s.searchRange(nums,target))