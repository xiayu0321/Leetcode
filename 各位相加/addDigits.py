class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        
        while num >= 10:
            numStr = str(num)
            sum = 0
            while(len(numStr) > 0):
                sum += int(numStr[-1])
                numStr = numStr[:-1]
            num = sum
        return sum
    
    def addDigits2(self, num: int) -> int:
        if num < 10:
            return num
        else: 
            numStr = str(num)
            sum = 0
            while(len(numStr) > 0):
                sum += int(numStr[-1])
                numStr = numStr[:-1]
        return self.addDigits(sum)
    

s = Solution()
print(s.addDigits(89))