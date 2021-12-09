#!/usr/bin/env python
# coding:utf-8

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = ""
        substring = ""

        if len(s) <= 1:
            return len(s)
        else:
            for v in s:
                if v not in substring:
                    substring = substring + v
                else:
                    if(len(substring) > len(longestSubstring)):
                        longestSubstring = substring
                    for k,m in enumerate(substring):
                        if m == v:
                            substring = substring[k+1:] + v
            if(len(substring) >= len(longestSubstring)):
                longestSubstring = substring
            return len(longestSubstring)


s = Solution()
print(s.lengthOfLongestSubstring("fjaifjofsnfakfoa_fjwo"))
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("au"))
print(s.lengthOfLongestSubstring("bbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
