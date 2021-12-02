#!/usr/bin/env python
# coding:utf-8

import math

class Solution1:
    def intToRoman(self, num: int) -> str:

        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        res = ""

        for i in range(len(values)):
            while (num >= values[i]):
                res = res + str(roms[i])
                num = num - values[i]

        return res

class Solution2:
    def intToRoman(self, num: int) -> str:

        m = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        s = str(num)
        l = len(s)
        res = ""

        if l == 4:
            res = res + math.floor(num / 1000) * m[1000]
            num = num % 1000
            l = l - 1
        if l == 3:
            if (num > 500):
                if (math.floor(num / 100) == 9):
                    res = res + "CM"
                else:
                    res = res + "D" + math.floor((num - 500) / 100) * m[100]
            elif num == 500:
                res = res + m[num]
            else:
                if (math.floor(num / 100) == 4):
                    res = res + "CD"
                else:
                    res = res + math.floor(num / 100) * m[100]
            num = num % 100
            l = l - 1
        if l == 2:
            if (num > 50):
                if (math.floor(num / 10) == 9):
                    res = res + "XC"
                else:
                    res = res + "L" + math.floor((num - 50) / 10) * m[10]
            elif num == 50:
                res = res + m[num]
            else:
                if (math.floor(num / 10) == 4):
                    res = res + "XL"
                else:
                    res = res + math.floor(num / 10) * m[10]
            num = num % 10
            l = l - 1

        if l == 1:
            if (num > 5):
                if num == 9:
                    res = res + "IX"
                else:
                    res = res + "V" + (num - 5) * m[1]
            elif num == 5:
                res = res + m[num]
            else:
                if num == 4:
                    res = res + "IV"
                else:
                    res = res + num * m[1]

        return res


s = Solution1()
for i in range(3998):
    print(s.intToRoman(i+1))

s = Solution2()
for i in range(3998):
    print(s.intToRoman(i+1))