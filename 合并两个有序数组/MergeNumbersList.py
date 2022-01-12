from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(0,n):
            nums1[i+m] = nums2[i]
        self.quickSort(nums1,0, m+n-1)
        
    def quickSort(self, nums,l,r):
        if l >= r:
            return
        left = l
        right = r
        key = nums[l]

        while(left < right):
            while(left < right and nums[right] >= key):
                right -= 1
            if(left < right):
                nums[left] = nums[right]
                left += 1
            while(left < right and nums[left] < key):
                left += 1
            if(left < right):
                nums[right] = nums[left]
                right -= 1 
        nums[left] = key
        self.quickSort(nums,l,left-1)
        self.quickSort(nums,left+1,r)

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n1 = n2 = 0
        newList = []
        while n1 < m or n2 < n:
            if n1 == m:
                newList.append(nums2[n2])
                n2 += 1
            elif n2 == n:
                newList.append(nums1[n1])
                n1 += 1
            elif nums1[n1] < nums2[n2]:
                newList.append(nums1[n1])
                n1 += 1
            elif nums1[n1] >= nums2[n2]:
                newList.append(nums2[n2])
                n2 += 1
        nums1[:] = newList

s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
s.merge1(nums1, 3, nums2, 3)
print(nums1)