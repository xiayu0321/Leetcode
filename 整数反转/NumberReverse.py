#!/usr/bin/env python
# coding:utf-8

import math
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or  x >= (2 ** 31)-1 or x <= (-(2 ** 31)):
            return 0
        res = int(self.reverseNumber(x))
        if res >= (2 ** 31)-1:
            return 0
        if x < 0:
            res = -int(res)
            return res
        elif x > 0:
            return res

    def reverseNumber(self,x):
        res = ""
        tmp = abs(x)
        while (tmp != 0):
            res = res + str(tmp % 10)
            tmp = math.floor(tmp / 10)
        return res

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(0))
print(s.reverse(1534236469))

