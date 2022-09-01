import math
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:   
        res = []
        
        l = len(nums)
        for i in range(1 << l):  # 左移代表乘
            temp = []
            for j in range(l):  # 遍历原数组中的每一位
                # (1 << j)为了遍历原数组的每一位,i 作为 mask
                if i & (1 << j): #确定当前位是否被选择（即当前位是否为1）
                    temp.append(nums[j])  
            res.append(temp)        
        return res

s = Solution()
nums = [1,2,3]
print(s.subsets(nums))
