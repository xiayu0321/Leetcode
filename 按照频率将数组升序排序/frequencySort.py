from re import X
from typing import Counter, List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums = sorted(nums,reverse=True)
        res = []
        num_fre = {}
        for num in nums:
            if num not in num_fre.keys():
                num_fre[num] = 1
            else:
                num_fre[num] += 1
                
        num_fre = sorted(num_fre.items(),key=lambda x:x[1],reverse=False)

        for n in num_fre:
            for i in range(n[1]):
                res.append(n[0])
                
        return res
    
    def frequencySort2(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        nums.sort(key=lambda x: (cnt[x], -x))
        return nums


if __name__ == "__main__":
    s = Solution()
    #nums = [8,-8,2,-8,-5,-3]
    nums = [-8,7,-1,3,5,7,-8,-8,0]


    print(s.frequencySort2(nums))