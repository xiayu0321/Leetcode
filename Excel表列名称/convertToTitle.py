class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while(columnNumber > 0):
               n = (columnNumber - 1 ) % 26
               res += chr((ord('A') + n))
               columnNumber = (columnNumber - n - 1) // 26
        return res[::-1]

s = Solution()
print(s.convertToTitle(2147483647))


