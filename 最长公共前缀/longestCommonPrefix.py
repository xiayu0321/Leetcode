#!/usr/bin/env python
# coding:utf-8
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        minLenghtStr = strs[0]
        for str in strs:
            if (len(str) <= len(minLenghtStr)):
                minLenghtStr = str
        minlen = len(minLenghtStr)

        i = minlen
        while(i > 0):
            flag = []
            for str in strs:
                if minLenghtStr[0:i] in str[0:i]:
                    flag.append(1)
                else:
                    flag.append(0)
            if 0 not in flag:
                return minLenghtStr[0:i]
            i = i - 1
        return ""


instance = Solution()
strs = ["reflower","flow","flight"]
print(instance.longestCommonPrefix(strs))

