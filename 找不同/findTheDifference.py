class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mapping = {}
        for i in s:
            if i not in mapping.keys():
                mapping[i] = 1
            else:
                mapping[i] += 1
        for i in t:
            if i not in mapping.keys() or mapping[i] == 0 :
                return i
            else:
                mapping[i] -= 1        
    
        return ""
    
    def findTheDifference2(self, s: str, t: str) -> str:
        temp = 0 
        for i in s:
            temp += ord(i)
        for i in t:
            temp -= ord(i)
    
        return chr(abs(temp))
    
    def findTheDifference3(self, s: str, t: str) -> str:
        res = 0
        for i in s+t:
            res ^= ord(i)
        
        return chr(res)
    
m = Solution()
s = "abcd"
t = "abcde"
print(m.findTheDifference3(s,t))