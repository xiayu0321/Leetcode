## 排列硬币（简单）

### 题目

你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。

给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。

**提示：**

- $1 <= n <= 2^{31} - 1$


链接：https://leetcode.cn/problems/arranging-coins

### 思路

由于题目中，第一行只有1个硬币，第二行两个，依次排列。因此可以在n的基础上减去每一行的硬币数目，直到硬币为0。但由于返回的是“形成 完整阶梯行 的总行数”，因此要考虑最后一行是否能完整形成，因此在判断返回时是在 n==-1的情况下。

```python
 def arrangeCoins(self, n: int) -> int:
        res = 0
        
        i = 1
        while(n > -1):
            n -= i
            i += 1
            res += 1
        return res - 1
```

这种方式的时间复杂度较高。由于按1，2，3....序列排序，可以考虑等差数列的求和公式。可知$s_n=[k(1+k)]/2$，因此，n 个元素可以形成1-n 之间的行。可借助二分查找来计算。

```python
 def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        
        while(left < right):
            mid = (left + right + 1) // 2  
            if mid * (mid + 1) <= 2 * n:   # 求和公式
                left = mid
            else:
                right = mid - 1
        
        return left
```

