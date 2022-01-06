#!/usr/bin/env python
# coding:utf-8
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        slist = s.split(' ')
        return len(slist[-1])

    def lengthOfLastWord1(self, s: str) -> int:
        l = 0
        i = len(s) - 1
        while(s[i] == ' '):
            i -= 1
        while(s[i] != ' ' and i >= 0):
            l += 1
            i -= 1
        return l

s = Solution()
res = s.lengthOfLastWord1("   fly me   to   the moon  ")
print(res)
