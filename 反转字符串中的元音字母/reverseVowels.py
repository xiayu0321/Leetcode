from operator import le
from re import I


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        Vowels = {'a','e','i','o','u','A','E','I','O','U'}
        right = len(s) - 1

        while(left < right):
            while left < len(s) and s[left] not in Vowels:
                left += 1
            while right > 0 and s[right] not in Vowels:
                right -= 1
            if left < right:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
        return "".join(s)
        
s = Solution()
st = "hello"
print(s.reverseVowels(st))