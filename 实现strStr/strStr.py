#!/usr/bin/env python
# coding:utf-8
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        if needle == "":
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if(haystack[i:i+l] == needle):
                    return i
        return -1
s = Solution()
print(s.strStr("hello",'ll'))