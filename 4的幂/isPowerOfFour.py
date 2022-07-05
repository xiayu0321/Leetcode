class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        
        while(n > 1):
            if n % 4 != 0:
                return False
            n /= 4
        
        return True
    
    def isPowerOfFour2(self, n: int) -> bool:
        if n < 1:
            return False
        if  n & (n-1) != 0:
            return False
        if n % 3 != 1:
            return False
        return True
    
    def isPowerOfFour3(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0

s = Solution()
nums = 5
print(s.isPowerOfFour2(nums))