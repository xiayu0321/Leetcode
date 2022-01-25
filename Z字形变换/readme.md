## Z字形变换（中等）

### 题目

将一个给定字符串 `s` 根据给定的行数 `numRows` ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 `"PAYPALISHIRING"` 行数为 `3` 时，排列如下：

```web-idl
P   A   H   N
A P L S I I G
Y   I   R
```

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"PAHNAPLSIIGYIR"`。

提示：

- `1 <= s.length <= 1000`
- `s` 由英文字母（小写和大写）、`','` 和 `'.'` 组成
- `1 <= numRows <= 1000`

链接：https://leetcode-cn.com/problems/zigzag-conversion/

### 思路

对字符串进行 Z 字形变换，其实质是找到下标的规律，将元素放到合适的位置上。

首先寻找变换后的元素在原始字符串的下标规律。变换后 Z 字形是一个变长二维数组，在二维数组中，我们需要寻找每一行元素的原索引和$numRows$中的关系。通过观察发现，每经过 $(2 * numRows - 2)$个字符，就进入一个新的 Z 循环。因此可以通过原索引与 $(2 * numRows - 2)$取余进行计算。

对于 N 中的每一竖线部分就是原索引与 $(2 * numRows - 2)$取余得到的前$numRows$个元素；而 N 中的斜线部分就是原索引与 $(2 * numRows - 2)$取余得到的在 $(numRows)$ 和 $(2 * numRows - 2)$ 之间的元素。最后，只要将相同余数的下标放到对应行中，就可得到变换后的二维数组结果，最后遍历变长二维数组就能得到最终排序数据。注意：这里还要考虑到$numRows=1$的情况，此时无需进行变换。

```python
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for e in range(0,numRows)]
        resStr = ''
        n = len(s)
        if numRows == 1:
            return s

        for i in range(n):
            for space in range(numRows,0,-1):
                if i % (2 * numRows - 2) == space - 1:
                    res[space - 1].append(s[i])
                elif i % (2 * numRows - 2) == 2 * numRows - space - 1:
                    res[space - 1].append(s[i])

        for i in res:
            for j in i:
                resStr += j
        return resStr
```

以上这种解法时间复杂度高。考虑直接遍历`s`，通过`当前行`和`转换方向`两个变量确定每个字符所在的行。只有向上移动到最上面的行或向下移动到最下面的行时，当前方向才会发生改变。在遍历字符串时，每经过一个字符，就加入到当前行，如果遇到最上行或最下行，就`转换方向`，调整当前行是向上还是向下，即当前行+1还是-1。

```python
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for e in range(0,numRows)]
        resStr = ''
        n = len(s)

        if numRows == 1:
            return s

        curRow = 0 
        goingDown = False

        for c in s:
            res[curRow].append(c)
            if (curRow == 0 or curRow == numRows - 1):
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        for i in res:
            for j in i:
                resStr += j
        return resStr
```







