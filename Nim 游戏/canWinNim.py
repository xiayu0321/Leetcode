class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        
        if (n - (n % 4)) % 4 == 0:
            return True
        
    def canWinNim2(self, n: int) -> bool:
        return n % 4 != 0
    
        

if __name__ == '__main__':
    s =  Solution()
    n = 4
    print(s.canWinNim2(n=n))
    