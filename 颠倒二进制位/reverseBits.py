class Solution:
    def reverseBits(self, n: int) -> int:
        sum  = 0
        for i in range(32):
            sum <<= 1
            if n & 1 == 1:
                sum += 1
            n >>= 1
              
        return sum
    

if __name__ == '__main__':
    s = Solution()
    n = 43261596
    print(s.reverseBits(n))