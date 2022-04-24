from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if len(nums) < 1:
            return []
        
        first = nums[0]
        last = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]+1:
                last = nums[i-1]
                if first == last:
                    res.append(str(first))
                else:    
                    res.append(str(first)+"->"+str(last))
                first = nums[i]
                last = nums[i]
            else:
                last = nums[i]
        if first >= last:
            res.append(str(first))
        else:    
            res.append(str(first)+"->"+str(last))
        return res

nums = [0,1,2,4,5]
s = Solution()
print(s.summaryRanges(nums))

        
        