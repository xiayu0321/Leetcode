
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        return self.fib(n-1)+self.fib(n-2)
    
    
    def fib2(self, n: int) -> int:
        if n < 2:
            return n    

        p = 0
        q = 0
        r = 1 
        for i in range(2,n+1):
            p,q = q,r 
            r = p + q
        return r

s =  Solution()
n = 10
print(s.fib2(n))