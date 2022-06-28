import collections
from distutils.archive_util import make_archive
from itertools import count
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    # 排序后统计字符出现个数进行比较
        nums = sorted(nums)
        n = len(nums)
        count = 0
                
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                count += 1
                if count >= n//2:
                    return nums[i]
            else:
                count = 0
        return nums[0]
    
    # 排序后利用众数的特点
    def majorityElement2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l = len(nums)
        return nums[l // 2]
    
    # 字典方式
    def majorityElement3(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    # 利用摩尔投票方式
    def majorityElement4(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for i in range(1,len(nums)):
            if count == 0:
                candidate = nums[i]
             
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1       
        return candidate   
           
s = Solution()
nums =  [1,2,1,1,1,2,2,2,2]
print(s.majorityElement4(nums))