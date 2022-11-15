class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        m =  x ^ y
        count = 0
        
        while(m):
            m = m & (m - 1)
            count += 1
            
        return count
    
    def hammingDistance2(self, x: int, y: int) -> int:
        m = x ^ y
        count = 0
        while(m):
            count += m & 1   
            m >>= 1
            
        return count
        
if __name__ == '__main__':
    s = Solution()
    x = 1
    y = 4
    print(s.hammingDistance2(x,y))
        