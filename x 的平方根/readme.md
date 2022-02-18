## X的平方根（简单）

### 题目

给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

**提示：**

- `0 <= x <= 231 - 1`

链接：https://leetcode-cn.com/problems/sqrtx

### 思路

首先，考虑是求`x`的算术平方根，实际是找$k^2<x$中 `k` 的最大值，因此  `k` 的最大值不会超过 `x` 的一半。即 $k^2<=x$，同时$(k+1)^2>x$。此时`k`就是最终得到的结果。

```python
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        for i in range(int(x / 2) + 1):
            if i * i <= x and (i+1) * (i+1) > x:
                return i
```

该方法耗费时间长，因此考虑第二种方法——二分查找。

首先分别设置上界和下界为 `x` 和`0`。只要下界小于上界，比较 $mid * mid$ 与$x$ 的大小关系，通过结果调整上下界的范围。

```python
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = -1
        while(l <= r):
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
```







