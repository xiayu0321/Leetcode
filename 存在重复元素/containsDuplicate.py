from typing import List, Mapping


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        for num in nums:
            if num not in mapping.keys():
                mapping[num] = 1
            else:
                return True
        return False

s = Solution()
nums =[1,1,1,3,3,4,3,2,4,2]
print(s.containsDuplicate(nums))