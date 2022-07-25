import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        countChar = {}
        for i  in range(len(ransomNote)):
            if ransomNote[i] not in countChar.keys():
                countChar[ransomNote[i]] = 1
            else:
                countChar[ransomNote[i]] += 1        
        for j in range(len(magazine)):
            if magazine[j] in countChar.keys():
                countChar[magazine[j]] -= 1
                
        for k,v in countChar.items():
            if v > 0:
                return False
        return True
    
    # 用库函数更加简略
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

s = Solution()
ransomNote = "aab"
magazine = 'baa'
print(s.canConstruct(ransomNote,magazine))
        
        
