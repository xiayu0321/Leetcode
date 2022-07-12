from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        mapping = {}
        res = []
        for i in range(len(nums1)):
            if nums1[i] in mapping.keys():
                mapping[nums1[i]] += 1
            else:
                mapping[nums1[i]] = 1
        
        for j in range(len(nums2)):
            if nums2[j] in mapping.keys():
                mapping[nums2[j]] -= 1
                if mapping[nums2[j]] >= 0:
                    res.append(nums2[j])
                
        return res
    
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        res = []
        
        p1 = 0
        p2 = 0
        
        while(p1 < len(nums1) and p2 < len(nums2)):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
                
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        return res
    
s = Solution()
nums1 = [9,4,9,8,4]
nums2 = [4,9,5]
print(s.intersect2(nums1,nums2))