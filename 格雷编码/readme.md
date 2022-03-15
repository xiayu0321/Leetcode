## 格雷编码（中等）

### 题目

n 位格雷码序列 是一个由 $2^n$ 个整数组成的序列，其中：

* 每个整数都在范围 [0, $2^n - 1$] 内（含 0 和 $2^n - 1$）
* 第一个整数是 0
* 一个整数在序列中出现 不超过一次
* 每对 相邻 整数的二进制表示 恰好一位不同 ，且第一个 和 最后一个 整数的二进制表示 恰好一位不同

给你一个整数 n ，返回任一有效的 n 位格雷码序列 。

提示：

- `1 <= n <= 16`

链接：https://leetcode-cn.com/problems/gray-code

### 思路

起初，因为格雷序列是 $2^n$ 个整数，并且需要比较其二进制数，因此考虑使用 mapping 存储其值以及其对应的二进制。同时，由于相邻整数的二进制表示恰好一位不同，因此考虑使用异或运算。再将异或运算的结果通过 `str.split('1')`分割出来的长度计算是否只有一位不同，（如果只有1个`1`，用1分割就只会产生2个 list，否则会多个 list）。同时由于第一位起始值为0，并且第二位和数组的最后一位都和它只有一位不同，因此可以确定第二位和最后一位的值。此外，中间的数据只需要比较当前位和前一位的二进制异或，异或结果只有一位为1，就可以给当前下标赋值。但是我没搞清如果异或结果不为1的时候应该如何处理。

```python
  # 以下方法是有问题的  
  def grayCode(self, n: int) -> List[int]:
        res = [0 for x in range(0,int(math.pow(2,n)))]    
 			  # mapping = {}
        # for i in range(len(res)):
        #     mapping[i] = int(bin(i)[2:].zfill(n))  # 转二进制并且高位补0
        # res[0] = 0
        
        # for i in range(len(res)):
        #     for j in range(i+1,len(res)):
        #         if j not in res:
        #             temp = str(mapping[j] ^ mapping[i])
        #             if len(temp.split('1')) == 2 and res[i] == 0:
        #                 res[i+1] = j
        #             elif len(temp.split('1')) == 2 and res[-1-i] == 0:
        #                 res[- i - 1] = j
        
        # return res

```

参考解答，假设n位二进制数为 b，对应的格雷码为 *g*，转换规则如下：

*g*(*i*)=*b*(*i*+1)⊕*b*(*i*),  0≤*i*<*n*

其中⊕ 是按位异或运算，g*(*i) 和 *b*(*i*) 分别表示 *g* 和 *b* 的第 *i* 位，且b(*n*)=0。

因此直接利用异或运算：

```python
    def grayCode(self, n: int) -> List[int]:
        res = [0 for x in range(0,int(math.pow(2,n)))]
        for i in range(len(res)):
            res[i] = (i >> 1) ^ i
        return res
```

