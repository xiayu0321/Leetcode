class Solution:
    def firstUniqChar(self, s: str) -> int:
        charsCount = {}
        
        for i in range(len(s)):
            if s[i] not in charsCount.keys():
                charsCount[s[i]] = 1
            else:
                charsCount[s[i]] += 1

        for i in range(len(s)):
            if charsCount[s[i]] == 1:
                return i
        return -1

    def firstUniqChar2(self, s: str) -> int:
        charsCount = {}
        
        # 字典中存储的字符出现的下标
        for i in range(len(s)):
            if s[i] not in charsCount.keys():
                charsCount[s[i]] = i
            else:
                charsCount[s[i]] = -1
        print(charsCount)
        first = len(s)
        # 遍历字典找到第一个出现非-1并且最小的字符下标
        for v in charsCount.values():
            if v != -1 and v < len(s):
                first = v
        if first == len(s):
            return -1
        return first        
                
S = Solution()
s = "loveleetcode"
print(S.firstUniqChar2(s))