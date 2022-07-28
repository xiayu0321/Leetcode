from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""
        n = len(nums)
        for i in range(n):
            nums[i] = str(nums[i])
            
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                 if int(nums[i]+ nums[j]) < int(nums[j] + nums[i]):
                        nums[i], nums[j] = nums[j], nums[i]
        
        for num in nums:
            res += num
        if res[0]=='0':
            res='0'
        return res

s = Solution()
nums = [0,0]
print(s.largestNumber(nums))