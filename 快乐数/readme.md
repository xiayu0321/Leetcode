## 快乐数（简单）

### 题目

编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」 定义为：

* 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
* 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
  如果这个过程 结果为 1，那么这个数就是快乐数。
* 如果` n` 是 快乐数 就返回 `true` ；不是，则返回 `false` 。

提示：

- 1 <= n <= $2^{31}$ - 1

链接：https://leetcode-cn.com/problems/happy-number

### 思路

快乐数是指将 n 按位拆分，然后计算每一位的平方和，再判断该数是否为1，如果不等于1，再继续循环。

因此发现，循环的主要部分主要分为『拆分数字的每一位』以及『计算每一位的平方和』。然后再判断平方和是否为1。如果为1，就可以直接返回 True，否则继续循环。但在循环的情况下，会出现 res 永远不等于1的情况，即无限循环。因此，设置当这个数小于10时，如果res不等于1，这样的情况出现2次就认为它不会有`res=1`的情况。

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        res = 0
        count = 0
        while(res != 1):
            temp = []
            while(n != 0):
                temp.insert(0,n % 10)
                n = math.floor(n / 10)
            res = 0
            for i in temp:
                res += i * i  
            if res < 10:
                count += 1
                if count >= 2:
                    break
            n = res
        return res == 1
```

以上方法没有理解题的真正含义，如果出现无限循环的情况，也就是在未来的某一元素又回到了之前出现的某一元素，即元素转换过程中会出现环。因此可以借助 set()的特征，不存储重复元素，来存储每次元素变化的情况。如果set 中出现重复，在判断当前结果是否等于1。如果等于1就直接返回 True，否则则返回 False。

```python
    def isHappy2(self, n: int) -> bool:
        seen = set()
        while n != 1  and n not in seen:
            seen.add(n)
            temp = []
            while(n != 0):
                temp.insert(0,n % 10)
                n = math.floor(n / 10)
            res = 0
            for i in temp:
                res += i * i 
            n = res
        return n == 1
```

