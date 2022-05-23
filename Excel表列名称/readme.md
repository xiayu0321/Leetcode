## Excel表列名称（简单）

### 题目

给你一个整数 `columnNumber` ，返回它在 Excel 表中相对应的列名称。

**提示：**

- $1 <= columnNumber <= 2^{31} - 1$

链接：https://leetcode.cn/problems/excel-sheet-column-title/

### 思路

由于题目要求根据数据转化为对应的字符串，而字母是26个字母一循环，因此我们可以与26取余，得到与字符'A'的 ascii 码的距离，由此就可以得到当前字符。此外，由于数据量较大，可能会导致有多个字符，因此需要将当前字符所代表的数字减掉，再除以26以进行下一次循环，直到数据小于0时完成循环。注意，这样形成的字符串从高位到低位是从个位算的，因此返回时需要返回相反字符串。

```python
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while(columnNumber > 0):
               n = (columnNumber - 1 ) % 26
               res += chr((ord('A') + n))
               columnNumber = (columnNumber - n - 1) // 26
        return res[::-1]
```

