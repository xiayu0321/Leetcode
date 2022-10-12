class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3 :  # 对于0，1，2阶楼梯分别只有0，1，2种方案
            return n
        
        # 对于其他方式就要构造斐波那契数据列，使用动态规划
        dp = [-1 for _ in range(n)]
        dp[0] = 1  # 一阶楼梯
        dp[1] = 2  # 二阶楼梯
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n-1]
    
if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.climbStairs(n))