class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True

        newStr = "".join(filter(str.isalnum,s)).lower()
        left = 0
        n = len(newStr) 
        right = n - 1

        while(left < right):
            if newStr[left] == newStr[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

s = Solution()
m = "1221"
print(s.isPalindrome(m))