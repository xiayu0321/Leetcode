## Pow(x,n) （中等）

### 题目

实现 [pow(*x*, *n*)](https://www.cplusplus.com/reference/valarray/pow/) ，即计算 `x` 的整数 `n` 次幂函数（即，$x^n$ ）。

**提示：**

- `-100.0 < x < 100.0`
- $-2^{31} <= n <= 2^{31}-1$
- $-10^4 <= x^n <= 10^4$

### 思路

求 x 的 n 次幂，首先考虑基本的乘法：对于 n == 0 的情况，都为1.0。对于n<0的情况，需要将 x 转换为1/x，并将 n 转换为正数；对于 n>0的情况，就可以直接n 个 x 相乘即可。

```python
def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        sum = 1.0 
        
        if n > 0:
            for i in range(1,n+1):
                sum *= x
        
        else:
            for i in range(1,-n+1):
                sum *= (1/x)      
        return sum
```

但这种方式在【**0.00001 2147483647**】中出现【超出时间限制】的问题。因此考虑其他方法。

第二种方式通过递归实现快速幂，即$x^n$可以进行分治，每次计算直接在上一次的结果上进行平方（$x^{32}-{x^{16}}^2-{{x^8}^2}^2-....$）。但这种情况需要判断 n 为奇偶。如为偶数，则直接平方，如果奇数，则需要在平方的基础上再乘以x。递归退出的条件为n=0的情况。

```python
def myPow(self, x: float, n: int) -> float:
  def quickMul(N):
    if N == 0:
      return 1
    
    y = quickMul(N // 2)
    
    if y % 2 == 0:
      return y * y
    else:
      return y * y * x
  
  if n >= 0:
    return quickMul(n)
  else:
    return 1.0/quickMul(-n)
    
```

第三种方式是将$x^n$划分为多个 $x^i$相成，由于十进制的 n 可以化为二进制，因此$x^n$可以将 n 划分为其二进制所对应的$ x^i$进行相乘，即$x^9=x^{1·1}x^{0·2}x^{0·4}x^{1·8}$,9化为二进制为1001，因此可以考虑循环 x=x^2的操作，每次把幂从 n 降至 n//2 ，直至将幂降为 0。初始res=1，初始状态$ x^n = x^n * res$，在二分时，注意 n是否为奇数，如果是奇数，还需要res 多乘一项 x。即 $x^n=x^0*res=res$

```python
def myPow(self, x: float, n: int) -> float:
  if x == 0:
    return 0.0
  res = 1
  if n < 0:
    n = -n
    x = 1 / x
  
  while(n):
    if n & 1 == 1: # n为奇数时所需要多乘一个 x
      res *= x
    x *= x
    n <<= 1
  return res
```

