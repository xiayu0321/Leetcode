## 整数转罗马数字（中等）

### 题目

罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

| 字符 | 数值 |
| ---- | ---- |
| I    | 1    |
| V    | 5    |
| X    | 10   |
| L    | 50   |
| C    | 100  |
| D    | 500  |
| M    | 1000 |


例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给你一个整数，将其转为罗马数字。

**提示：**

- 1 <= num <= 3999

链接：https://leetcode-cn.com/problems/integer-to-roman

### 思路

第一版思路——最基本的枚举

由于数字和字符有对应关系，因此还是通过字典形式进行存储（由于没有扩展思维，所以只存储基本的对应表，导致后续操作比较麻烦）。再从题目中看出，数字转罗马数字，从高位到到低位要找到『最大的符号值』（不大于本身数字，特殊情况除外），而在不同位数时，所对应的罗马字母不相同，特殊情况对应的字母情况也不相同，因此需要对每一位进行处理。由于提示中表示 nums 的位数最多为4位，因此从高位开始处理。

首先先确定nums 的位数，通过转为 str得到位数，再根据位数处理每一类的情况，四位中包含三位、二位和一位的情况，因此这几位情况是并列关系。

在四位数据（千位）中，不存在特殊情况，因此找到由几个1000构成， 最终结果就加上几个「M」，在得到剩下的位数（三位）

在三位数据（百位）中，主要分为大于500（500+多少个100）、小于500（多少个100）和等于500（直接对应 D），在大于500的情况中，还存在特殊情况900（CM），而在小于500的情况中还存在400（CD）。

在二位数据（十位）中，同样分为三个主要情况：主要分为大于50（50+多少个10）、小于50（多少个10）和等于50（直接对应 L），在大于50的情况中，还存在特殊情况90（XC），而在小于50的情况中还存在40（XL）。

在一位数据（个位）中，也分为三个主要情况：主要分为大于5（5+多少个1）、小于5（多少个1）和等于5（直接对应 V），在大于5的情况中，还存在特殊情况9（XI），而在小于50的情况中还存在4（IV）。

在这种情况下，要注意5，50，500的单独考虑，同时，在计算除法时需要注意取整运算。

```python
import math

class Solution:
    def intToRoman(self, num: int) -> str:
              m = {1:'I', 5: 'V', 10: 'X', 50: 'L',100: 'C',500: 'D', 1000:'M'}
        s = str(num)
        l = len(s)
        res = ""

        if l == 4:
            res = res + math.floor(num / 1000) * m[1000]
            num = num % 1000
            l = l - 1
        if l == 3:
            if(num > 500):
                if (math.floor(num / 100) == 9):
                    res = res + "CM"
                else:
                    res = res + "D"+ math.floor((num-500)/100)*m[100]
            elif num == 500:
                res = res + m[num]
            else:
                if (math.floor(num / 100) == 4):
                    res = res + "CD"
                else:
                    res = res + math.floor(num/100)*m[100]
            num = num % 100
            l = l - 1
        if l == 2:
            if(num > 50):
                if (math.floor(num / 10) == 9):
                    res = res + "XC"
                else:
                    res = res + "L"+math.floor((num-50)/10)*m[10]
            elif num == 50:
                res = res + m[num]
            else:
                if (math.floor(num / 10) == 4):
                    res = res + "XL"
                else:
                    res = res + math.floor(num/10)*m[10]
            num = num % 10
            l = l - 1

        if l == 1:
            if (num > 5):
                if num  == 9:
                    res = res + "IX"
                else:
                    res = res + "V" + (num - 5)  * m[1]
            elif num == 5:
                res = res + m[num]
            else:
                if num  == 4:
                    res = res + "IV"
                else:
                    res = res + num * m[1]

        return res


s = Solution()
for i in range(3998):
    print(s.intToRoman(i+1))
```

第二版思路——贪心

由于特殊情况也是存在对应关系，因此可以直接作为新的数字字符对应关系。

同时由于数字转罗马字符，对于罗马数字从左到右的每一位，选择尽可能大的符号值。因此，可以将数字按照从大到小排序形成数值数组，对应字符按序形成字符数组。

对于整数 num，我们在数值数组（遍历数值数组）中找到不超过 num 的最大数字（由于数值数组本来就是从大到小排序，找到第一个小于 nums 的数字就是不超过 num 的最大数字），然后 res 拼接对应字符，然后再用 num 减去该数字，然后再在字符数组中找不超过 num 的最大数字，然后 res 再拼接对应字符。循环直到 num = 0.

注意：一定要保证数值数组的下标和罗马字符数组的下标一致，这样才能保持对应关系。

```python
class Solution1:
    def intToRoman(self, num: int) -> str:

        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        res = ""

        for i in range(len(values)):
            while (num >= values[i]):
                res = res + str(roms[i])
                num = num - values[i]

        return res
 
s = Solution1()
for i in range(3998):
    print(s.intToRoman(i+1))
```

