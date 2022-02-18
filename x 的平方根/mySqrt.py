class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        for i in range(int(x / 2) + 1):
            if i * i <= x and (i+1) * (i+1) > x:
                return i
    
    def mySqrt1(self, x: int) -> int:
        l = 0
        r = x
        ans = -1
        while(l <= r):
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

s = Solution()
print(s.mySqrt1(100))