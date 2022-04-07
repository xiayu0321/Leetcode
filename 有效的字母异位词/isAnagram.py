class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sres = {}
        tres = {}
        for i in range(len(s)):
            if s[i] not in sres.keys():
                sres[s[i]] = 1
            else:
                sres[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in tres.keys():
                tres[t[j]] = 1
            else:
                tres[t[j]] += 1   
        return sres == tres 

        # for m in sres.keys():
        #     if m not in tres.keys():
        #         return False
        #     if sres[m] != tres[m]:
        #         return False
        # return True
    
    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

s = Solution()
m = "anagram"
n = "nagaram"
print(s.isAnagram(m,n))