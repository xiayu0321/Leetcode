##  颠倒二进制位（简单）

### 题目

颠倒给定的 32 位无符号整数的二进制位。

提示：

请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在 示例 2 中，输入表示有符号整数 -3，输出表示有符号整数 -1073741825。

**提示：**

- 输入是一个长度为 `32` 的二进制字符串

链接：https://leetcode.cn/problems/reverse-bits

### 思路

刚开始，由于题目中提示表明输入是长度为32的二进制字符串，我考虑直接反转字符串，然后按照二进制转十进制的方式，遍历32位字符串转换即可。

然后发现测试样例中，输入并不是32的二进制字符串，而是其所对应的十进制整数。因此要考虑反转二进制后得到的十进制 res 和原十进制数n的关系。会发现，n 转成二进制后每取末尾一位，将其加入到 res二进制的末尾。即每一轮循环先将 res 左移一位，然后取出 n 的末尾一位加入到 res 中，最后将 n 右移一位即可。因此，可以通过位运算进行。

```python
def reverseBits(self, n: int) -> int:
  res  = 0
  
  for i in range(32):
    # res 先左移一位，等到取出 n 的末尾一位
    res <<= 1
    # 判断n 的末尾位是1还是0，如果是1，直接 res+1，否则左移时已经加0了
    if n & 1 == 1:
      res += 1
    # 最后将 n 右移一位 
    n >>= 1
  return res
    

```











