class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while(n > 1):
           if n % 2:
               return False
           n = n / 2
               
        return True
    def isPowerOfTwo2(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0
            
s = Solution()
n = 18
print(s.isPowerOfTwo3(n))