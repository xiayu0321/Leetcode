from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = len(nums1)
        res = [-1 for _ in range(l)]
        
        for i in range(l):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    break
            
            for k in range(j,len(nums2)):
                if nums2[k] > nums1[i]:
                    res[i] = nums2[k]
                    break
        return res
    
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {} # 哈希表直接存储当前元素所对应的单调栈的栈顶元素（即每个元素右边的第一个更大的值）
        stack = []
        
        for num in reversed(nums2): # 求单调栈
            while stack and  stack[-1] <= num:
                stack.pop()
            if stack:
                res[num] = stack[-1]
            else:
                res[num] = -1
            stack.append(num)
        return [res[num] for num in nums1]
    
if __name__ == "__main__":
    s = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(s.nextGreaterElement2(nums1=nums1,nums2=nums2))