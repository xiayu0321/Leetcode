## 加一（简单）

### 题目

给定一个由 **整数** 组成的 **非空** 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

提示：

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`

链接：https://leetcode-cn.com/problems/plus-one

### 思路

首先，考虑将数组中所表示数字以字符串的形式提取出来，然后转换为数字再进行加一，最后把数字每一位分别取出来放到数组中返回。

```python
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        res = []
        for i  in digits:
            num += str(i)
        num = str(int(num) + 1)
        for i in list(num):
            res.append(int(i))
        return res
```

在这种方式中，用到了很多`字符串`和 `int` 类型的转换。可以考虑仅从数字运算的角度来看。

在加一运算中，主要分为三种情况：1）末位数据小于9，则只需要在最后一位加1；2）末尾连续数据都等于9，则需找到从末尾开始的第一个不为9的元素，将该元素加1，并将其后面所有元素变为0，相当于进一位；3）所有数据全为9，则加一后，需要在前面加一位，赋值为1，其余元素置为0。

```python
    def plusOne1(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i+1,len(digits)):
                    digits[j] = 0
                return digits
    
        return [1] + [0] * len(digits)
```

