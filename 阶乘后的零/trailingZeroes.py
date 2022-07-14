class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 1
        while(n > 0):
            res = res * n
            n = n - 1
        
        res = str(res)
        l = len(res)
        count = 0
        for i in range(l-1,-1,-1):
            if res[i] == '0':
                count +=1
            else:
                break
        return count
    
    def trailingZeroes2(self, n: int) -> int:
        count = 0
        for i in range(5,n+1,5):
            while(i % 5 == 0):
                count += 1
                i //= 5
        return count
    
    
s = Solution()
print(s.trailingZeroes2(5))