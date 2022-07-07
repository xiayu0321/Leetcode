from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        temp = set()

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                temp.add(nums1[i])
        res = list(temp)
        return res
    
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i = 0
        j = 0

        res = []
        
        while(i < len(nums1) and j < len(nums2)):
            print(nums1[i])
            if nums1[i] == nums2[j]:
                if len(res) == 0 or res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
        return res
        
s = Solution()
nums1 = [4,9,5] 
nums2 = [9,4,9,8,4]
print(s.intersection2(nums1,nums2))