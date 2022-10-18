## 斐波那契数（简单）

### 题目

斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定 n ，请计算 F(n) 。

**提示：**

- `0 <= n <= 30`

链接：https://leetcode.cn/problems/fibonacci-number

### 思路

斐波那契数初始值F(0) = 0，F(1) = 1，后面的数字为前两个数字之和。因此可以使用递归方式。递归退出条件为：n = 0或 n=1时，否则就一直调用F(n) = F(n - 1) + F(n - 2)。

```python
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        return self.fib(n-1)+self.fib(n-2)
```

另一种方式是使用动态规划。同样的初始值p = 0，q = 0，r = 1，然后遍历到 n，在每一轮遍历时，依次轮转两个数的取值，然后当前数是前两个数之和，求出当前数。直到遍历到 n 时，即可得到当前的斐波那契数。

```python
    def fib(self, n: int) -> int:
        if n < 2: 
            return n
        
        p = 0
        q = 0
        r = 1
        for i in range(2,n+1):
          p,q = q,r
          r = p + q 
          
        return r
```

