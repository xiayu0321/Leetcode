#!/usr/bin/env python
# coding:utf-8
class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        l = list(s)
        r = 0

        for i in range(len(l)):
            if(i < len(l) - 1 and m[l[i]] < m[l[i+1]]):
                r = r - m[l[i]]
            else:
                r = r + m[l[i]]
        return r

m = Solution()
print(m.romanToInt("MCMXCIV"))
