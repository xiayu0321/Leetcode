from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        
        for num in nums:
            if num == 1:
                count += 1
            elif num == 0:
                if count > maxCount:
                    maxCount = count
                count = 0
        if count > maxCount:
            maxCount = count
                
        return maxCount
    
    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:
        left = right = 0
        res = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                right += 1
                res = max(right-left, res)
                
            if nums[i] == 0:
                right += 1
                left = right          
                      
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [1,1,0,1,1,1,1,1,1,0,1,1,1,1]
    print(s.findMaxConsecutiveOnes2(nums=nums))
            
            