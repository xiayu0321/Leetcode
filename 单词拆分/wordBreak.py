from typing import List

class Solution:
    # 这个方法在wordDict含有子串及其前缀子串时，会出现问题
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        indexs = []
        start = 0
        res = s
        for i in range(len(s)+1):
            if s[start:i] in wordDict:
                indexs.append(i)
                res = s[i:]
                start = i
            if res in wordDict:
                res = None
                indexs.append(len(s))
                break
        if indexs[-1] == len(s):
            return True
        return False
    
    # 动态规划：1) 确定阶段 2)明确每个阶段的状态 3)从前一个状态转化后一阶段之间的递推关系
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(n + 1):
            for j in range(i,-1,-1):
                if dp[j] and s[j : i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
            
s = Solution()
print(s.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
print(s.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))
print(s.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
print(s.wordBreak(s = "aaaaaaa", wordDict = ["aaaa", "aaa"]))
print(s.wordBreak(s = "goalspecial", wordDict = ["go","goal","goals","special"]))

print(s.wordBreak1(s = "leetcode", wordDict = ["leet", "code"]))
print(s.wordBreak1(s = "applepenapple", wordDict = ["apple", "pen"]))
print(s.wordBreak1(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
print(s.wordBreak1(s = "aaaaaaa", wordDict = ["aaaa", "aaa"]))
print(s.wordBreak1(s = "goalspecial", wordDict = ["go","goal","goals","special"]))
