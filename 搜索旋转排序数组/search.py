from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while(left <= right):
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[0]:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left  = mid + 1
            
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                      
        return -1
    
                    
            
if __name__  == '__main__':
    s = Solution()
    nums = [3,1]
    target = 1
    print(s.search(nums,target))