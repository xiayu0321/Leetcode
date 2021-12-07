#!/usr/bin/env python
# coding:utf-8
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        flag = True
        if len(s) < 2:
            return False
        else:
            for i in s:
                if i in ('(','{','['):
                    stack.append(i)
                else:
                    if len(stack) == 0:
                        return False
                    else:
                        tmp = stack.pop()
                        if i == '}' and tmp == '{':
                            flag = True
                        elif i == ']' and tmp == '[':
                            flag = True
                        elif i == ')' and tmp == '(':
                            flag = True
                        else:
                            flag = False
                    if flag == False:
                        return flag

            if len(stack) != 0:
                return False
            else:
                return True

s = Solution()
print(s.isValid(s = '({}}}()())'))
