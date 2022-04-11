## 各位相加（简单）

### 题目

给定一个非负整数 `num`，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

**提示：**

- `0 <= num <= 231 - 1`

链接：https://leetcode-cn.com/problems/add-digits/

### 思路

各位相加需要先遍历整数，取出每一位，相加之后再进行判断是否是个位数，直至满足和为个位数的条件。

因此，可以分为两种情况，第一种是本身`num`为个位数，则可以直接返回，无需再取出每一位。第二种就是`num`是多位数的情况。在这种情况下，需要取出每一位的值，并相加。在这里考虑使用 python 中字符串的形式，利用`s[-1]`的操作可以取出每一位，直至字符串长度为0时，`num`的每一位相加完毕。此时再判断和是否为个位数，是则直接返回，否则就继续遍历。

```python
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        
        while num >= 10:
            numStr = str(num)
            sum = 0
            while(len(numStr) > 0):
                sum += int(numStr[-1])
                numStr = numStr[:-1]
            num = sum
        return sum
```

上述情况还可以使用递归，递推的退出条件是各位之和为个位数，即小于0，否则就取出每一位相加，返回时调用自身再进行判断。

