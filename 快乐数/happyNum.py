import math

class Solution:
    def isHappy(self, n: int) -> bool:
        res = 0
        count = 0
        while(res != 1):
            temp = []
            while(n != 0):
                temp.insert(0,n % 10)
                n = math.floor(n / 10)
            res = 0
            for i in temp:
                res += i * i  
            if res < 10:
                count += 1
                if count >= 2:
                    break
            n = res
        return res == 1

    def isHappy2(self, n: int) -> bool:
        seen = set()
        while n != 1  and n not in seen:
            seen.add(n)
            temp = []
            while(n != 0):
                temp.insert(0,n % 10)
                n = math.floor(n / 10)
            res = 0
            for i in temp:
                res += i * i 
            n = res
        return n == 1

s = Solution()
print(s.isHappy2(19))