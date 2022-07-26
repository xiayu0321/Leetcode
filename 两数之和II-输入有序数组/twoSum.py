from operator import le
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while(left < right):
            temp = target - numbers[left]
            if numbers[right] > temp:
                right -= 1
            elif numbers[right] == temp:
                return [left+1,right+1]
            else:
                left += 1   
        return [-1,-1]    
    
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left = i + 1
            right = len(numbers) - 1
            while(left <= right):
                mid = (left + right) // 2
            
                if numbers[mid] == target - numbers[i]:
                    return [i+1,mid+1]
                elif numbers[mid] < target - numbers[i]:
                    left = mid + 1
                else:
                    right = mid - 1
        return [-1,-1]
                
s = Solution()
numbers = [-1,0]
target = -1
print(s.twoSum2(numbers,target))