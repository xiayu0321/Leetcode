class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")[::-1]
        res = ""
        for i in s:
            if i != "":
                res += i
                res += " "         
        return res[:-1]
    
    def reverseWords2(self, s: str) -> str:
        left = right = len(s) - 1
        res = ""
        
        while(left > -1):
            # 先找到单词的右边
            while(left > -1 and left <= right and s[left] == " "):
                right -= 1  
                left -= 1 
            # 再从当前字符找单词左边的值
            while(left > -1 and left <= right and s[left] != " "):
                left -= 1

            if left < right:
                res += s[left+1:right+1]
                res += " "
                right = left
        return res[:-1]

s = Solution()
m = "a good   example"
print(s.reverseWords2(m))