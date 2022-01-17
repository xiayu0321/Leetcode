class Solution:
    def hammingWeight(self, n: int) -> int:
        m = 0
        for i in range(32):
            if (n & (1 << i)) :
                m += 1
        return m

s = Solution()
res = s.hammingWeight(10000000000000000000000000001011)
print(res) 