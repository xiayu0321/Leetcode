from typing import List
from collections import Counter

class Solution:
    # 使用哈希表（时间复杂度和空间复杂度高）
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in counter.keys():
                counter[nums[i]] = 1
            else:
                counter[nums[i]] += 1 

        for k,v in counter.items():
            if v == 1:
                res.append(k)

        return res

    # 另一种调用Counter包的方式
    def singleNumber2(self, nums: List[int]) -> List[int]:
        res = []
        fre = Counter(nums)
        for k,v in fre.items():
            if v == 1:
                res.append(k)
        return res

    # 采用位运算
    def singleNumber3(self, nums: List[int]) -> List[int]:
        temp = 0
        for num in nums:
            temp ^= num

        l = temp & (-temp)  # 得到当前值的最低位的1，此时这位为1，这两个数的这一位必定一个为0，一个为1
        type1 = type2 = 0
        for num in nums:
            if num & l:
                type1 = num
            else:
                type2 = num 
        return [type1,type2]

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,1,3,2,5]
    print(s.singleNumber3(nums=nums))