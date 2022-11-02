class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        
        i = 1
        while(n > -1):
            n -= i
            i += 1
            res += 1
        return res - 1
    
    def arrangeCoins2(self, n: int) -> int:
        left = 1
        right = n
        
        while(left < right):
            mid = (left + right + 1) // 2
            if mid * (mid + 1) <= 2 * n:   # 求和公式
                left = mid
            else:
                right = mid - 1
        
        return left
            
    
if __name__ == "__main__":
    s =  Solution()
    n = 8
    print(s.arrangeCoins(n))