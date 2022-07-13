class Solution:
    def guess(self, num : int) -> int:
        pick = 1
        if num < pick:
            return 1
        if num > pick:
            return -1
        if num == pick:
            return 0
            
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        while(left < right):
            mid = (left + right) // 2
            if self.guess(mid) <= 0:
                right = mid
            else:
                left = mid + 1
        return left

s = Solution()
print(s.guessNumber(1))
                
            