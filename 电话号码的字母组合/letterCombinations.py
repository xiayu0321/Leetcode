#!/usr/bin/env python
# coding:utf-8
import itertools
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        s = []
        res = []
        digitlist = list(digits)
        for items in digitlist:
            s.append(list(mapping[items]))
        for i in itertools.product(*s):
            res.append(''.join(i))
        return res

s = Solution()
print(s.letterCombinations(digits = "2"))