from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        res = []
        for i  in digits:
            num += str(i)
        num = str(int(num) + 1)
        for i in list(num):
            res.append(int(i))
        return res
    
    def plusOne1(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i+1,len(digits)):
                    digits[j] = 0
                return digits
    
        return [1] + [0] * len(digits)

s = Solution()
digits = [0]
print(s.plusOne1(digits))
