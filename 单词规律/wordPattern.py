from __future__ import nested_scopes


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        news = s.split(" ")
        if len(news) != len(pattern):
            return False
        
        aMapping = {}
        bMapping = {}
        for i in range(len(pattern)):
            m = pattern[i]
            n = news[i]
            if ( m in aMapping.keys() and aMapping[m] != n) or (n in bMapping.keys() and bMapping[n] != m):
                return False
            aMapping[m] = n
            bMapping[n] = m
        return True
        
s = Solution()
pattern = "aaaa"
str = "dog cat cat dog"
print(s.wordPattern(pattern,str))