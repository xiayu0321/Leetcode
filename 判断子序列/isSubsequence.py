class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idxs = []
        idx = 0
        for i in s:
            while(idx < len(t)):
                if t[idx] == i:
                    idxs.append(idx)
                    idx = idx + 1
                    break
                else:
                    idx += 1
        return True if len(idxs) == len(s) else False

    def isSubsequence2(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        
        while(i < len(s) and j < len(t)):
            if s[i] == t[j]:
                i += 1  
            j += 1    
        return i == len(s) 

m = Solution()
s = "axc"
t = "ahbgdc"
print(m.isSubsequence2(s,t))