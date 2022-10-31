## Fizz Buzz（简单）

### 题目

给你一个整数 n ，找出从 1 到 n 各个整数的 Fizz Buzz 表示，并用字符串数组 answer（下标从 1 开始）返回结果，其中：

* answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
* answer[i] == "Fizz" 如果 i 是 3 的倍数。
* answer[i] == "Buzz" 如果 i 是 5 的倍数。
* answer[i] == i （以字符串形式）如果上述条件全不满足。

**提示：**

- $1 <= n <= 10^4$

链接：https://leetcode.cn/problems/fizz-buzz

### 思路

本题主要判断1-n 中哪些数字为3和5的倍数、3的倍数、5的倍数。因此，可通过遍历1至 n，通过 if 和取余判断，将其加入到 answer队列中即可。

```python
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer
```