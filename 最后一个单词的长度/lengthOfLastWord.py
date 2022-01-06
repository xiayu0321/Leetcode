#!/usr/bin/env python
# coding:utf-8
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        slist = s.split(' ')
        return len(slist[-1])

s = Solution()
res = s.lengthOfLastWord("luffy is still joyboy")
print(res)
