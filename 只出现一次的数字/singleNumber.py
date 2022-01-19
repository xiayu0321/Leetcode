from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = {}
        for num in nums:
            if num in mapping:
                mapping[num] += 1
            else:
                mapping[num] = 1
        for key in mapping.keys():
            if mapping.get(key) == 1:
                return key
                
    def singleNumber1(self, nums: List[int]) -> int:
        res = 0
        for num  in nums:
            res ^= num
        return res

s = Solution()
print(s.singleNumber1([2,2,1]))
print(s.singleNumber1([4,2,1,2,1]))