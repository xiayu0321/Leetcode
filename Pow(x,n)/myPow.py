from symbol import namedexpr_test


class Solution:
    # 超出时间限制
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        sum = 1.0 
        
        if n > 0:
            for i in range(1,n+1):
                sum *= x
        
        else:
            for i in range(1,-n+1):
                sum *= (1/x)      
        return sum
    
    # 通过递归计算快速幂(即先计算 x^2)
    def myPow2(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1
            
            y = quickMul(N // 2)
            if N // 2 == 0:
                return y * y
            else:
                return y * y * x
        
        if n >= 0:
            return quickMul(n)
        else:
            return 1.0 / quickMul(-n)
        
    def myPow3(self, x: float, n: int) -> float:
        if x == 0:
            return 0.0
        
        res = 1.0
        
        if n < 0:
            x = 1/x
            n = -n
        
        while(n):
            if n & 1 == 1:
                res *= x
            x *= x
            n >>= 1
        return res
                    
if __name__ == "__main__":
    s = Solution()
    x = 2.00000
    n = 10
    print(s.myPow(x,n))
    
        