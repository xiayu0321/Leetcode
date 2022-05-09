class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMapping = {}
        tMapping = {}

        for i in range(len(s)):
            m = s[i]
            n = t[i] 
            
            if ( m in sMapping.keys() and sMapping[m] != n) or (n in tMapping.keys() and tMapping[n] != m):
                return False
            sMapping[m] = n
            tMapping[n] = m
        return True  

s = Solution()
a = "paper"
b = "title"
print(s.isIsomorphic(a,b))