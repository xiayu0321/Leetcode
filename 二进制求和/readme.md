## 二进制求和（简单）

### 题目

给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 **非空** 字符串且只包含数字 `1` 和 `0`。

提示：

- 每个字符串仅由字符 `'0'` 或 `'1'` 组成。
- `1 <= a.length, b.length <= 10^4`
- 字符串如果不是 `"0"`，就都不含前导零。

链接：https://leetcode-cn.com/problems/add-binary/

### 思路

考虑直接将字符串转为二进制数，然后直接进行二进制加法，在通过 bin()函数将 int 类型数据转为字符串。此时注意：如果不要0b 表示，则从下标2开始取。

```python
    def addBinary(self, a: str, b: str) -> str:
        x = int(a,2)
        y = int(b,2)
        res = bin(x + y)
        return res[2:]
```



