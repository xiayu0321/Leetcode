from typing import List


class Solution:
    # 重新建立一个哈希表，时间复杂度高
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        
        mapping = {}
        n = len(nums)
        for i in range(1,n+1):
            mapping[i] = 0
            
        for num in nums:
            if num in mapping.keys():
                mapping[num] += 1
        
        for k,v in mapping.items():
            if v == 0:
                res.append(k)
        return res

    # 将原数组作为哈希表
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        # 将原始数组作为哈希表，先找到当前数字所对应的下标
        for num in nums:
            x = (num - 1) % n
            nums[x] += n
        # 遍历数组，找到小于 n 的数字所在的下标，即为缺失元素
        for i, num in enumerate(nums):
           if num < n:
               res.append(i+1)
        return res
        
if __name__ == '__main__':
    nums = [1,1]
    s = Solution()
    print(s.findDisappearedNumbers2(nums))
    
                
            
        
        