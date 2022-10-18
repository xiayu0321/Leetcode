## 字符串相加（简单）

### 题目

给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。

提示：

* `1 <= num1.length, num2.length <= 10^4`
* num1 和num2 都只包含数字 0-9
* num1 和num2 都不包含任何前导零

链接：https://leetcode.cn/problems/add-strings

### 思路

字符串相加考虑将两个字符串从后到前将每一位字符取出，并与对应进位相加得到当前位的值，因此可借助一个数组保存当前位的进位。

在以上条件下，可以先考虑两字符串都存在的部分(即：以字符串较短的长度为准)，同时遍历两个字符串，对应位与进位相加，得到的字符串最后一位是当前位，高一位为进位，将其保存在辅助数组里。然后再处理字符串超出最短字符串的部分，此时同样遍历字符串超出的部分，但此时只需要将当前位与进位值相加即可。最后要单独考虑最高位向前进位的情况。如果辅助数组中最后一位不为0，则表明最高一位有进位，所以在结果的基础上要加一位为进位，否则不加。最后倒序返回 res 即可。

```python
    def addStrings(self, num1: str, num2: str) -> str:
        # 找到最长和最短数组
        max_m = len(num1) if len(num1) > len(num2) else len(num2)
        min_n = len(num2) if len(num1) > len(num2) else len(num1)
        arr = [0 for _ in range(max_m+1)]
        
        res = ""
        # 先遍历两字符串都有的部分，即以短为准（两字符串对应位以及进位相加）
        for i in range(min_n):
            temp = int(num1[-1-i]) + int(num2[-1-i]) + int(arr[i])

            res += str(temp)[-1]
            if temp >= 10:
                arr[i+1] = temp // 10
        # 对超出的部分进行计算（仅考虑超出的字符串，因此就是超出字符串的每一位与对应进位相加）
        for i in range(min_n,max_m):
            if len(num1) > len(num2):
                temp = int(num1[-1-i]) + int(arr[i])
            else:
                temp = int(num2[-1-i]) + int(arr[i])
                
            res += str(temp)[-1]
            if temp >= 10:
                arr[i+1] = temp // 10
        # 对最高位的进位进行处理（最高位可能由进位产生）
        if arr[max_m] != 0:
            res += str(arr[max_m])
            
        return res[::-1]
```

另一种方式是按照标准竖式的方式进行相加。通过两个下标指向字符串的最后一位，然后依次向前遍历，每遍历一位，计算当前对应位与进位之和（个位上无进位，因此初始时 add=0），然后计算一位后，取出最后一位为当前位，高位为进位。直至两字符串任一字符串到最高位或者 add 不为0的情况下结束。

```python
def addStrings2(self, num1: str, num2: str) -> str:
  i = len(num1) - 1
  j = len(num2) - 1
  add = 0
  ans = []
  
  while(i >= 0 or j >= 0 or add != 0):
    x = ord(num1[i]) - ord('0') if i >= 0 else 0
    y = ord(num2[j]) - ord('0') if j >= 0 else 0 
    res = x + y + add
    ans.append(res % 10)
    add = res // 10
    i -= 1
    j -= 1
    
  return "".join(str(i) for i in ans[::-1])
    
```

