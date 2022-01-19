## 只出现一次的数字（简单）

### 题目

给定一个**非空**整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

链接：https://leetcode-cn.com/problems/single-number/

### 思路

由于需要统计元素以及元素出现的次数，首先想到通过字典形式来存储。因此，在遍历数组时，如果该元素在字典的key 中没有出现过，就在字典中增加相应元素的 key，并将其对应的 value（出现的次数）赋值为1；如果该元素在字典的key 中出现过，就直接将该元素所对应的 value 加1。直到数组遍历完。最后，再遍历字典，如果value==1时，该值对应的 key 就是最终元素。

```python
    def singleNumber(self, nums: List[int]) -> int:
        mapping = {}
        for num in nums:
            if num in mapping:
                mapping[num] += 1
            else:
                mapping[num] = 1
        for key in mapping.keys():
            if mapping.get(key) == 1:
                return key
```

但这种方法使用了额外空间mapping。

由于题目中提到『某个元素只出现一次，其余元素均出现了两次』，因此可以使用『异或运算』。异或运算有三大性质：

* 任何数和 0 做异或运算，结果仍然是原来的数；
* 任何数和其自身做异或运算，结果是 0；
* 异或运算满足交换律和结合律。

综上，可以通过遍历数组，使数组元素进行异或运算，出现两次的元素异或为0，最终得到的元素就是只出现了一次的元素。

```python
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num  in nums:
            res ^= num
        return res
```

