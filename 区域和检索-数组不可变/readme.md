## 区域和检索（简单）

### 题目

给定一个整数数组  nums，处理以下类型的多个查询:

计算索引 left 和 right （包含` left `和` right`）之间的 `nums `元素的 和 ，其中 `left <= right`
实现 `NumArray` 类：

`NumArray(int[] nums) `使用数组 nums 初始化对象`int sumRange(int i, int j) `返回数组 `nums` 中索引 `left `和` right `之间的元素的 总和 ，包含` left `和` right` 两点（也就是 `nums[left] + nums[left + 1] + ... + nums[right]`)

 提示：

* $1 <= nums.length <= 10^4$

* $-10^5 <= nums[i] <= 10^5$
* 0 <= i <= j < nums.length
* 最多调用 $10^4 $次 sumRange 方法

链接：https://leetcode.cn/problems/range-sum-query-immutable

### 思路

题目中要求创建一个类，通过 init 方法将传入数组 nums 初始化对象，然后sumRange方法是计算nums 中下标 i 和 j 之间的元素之和。因此，首先考虑将nums 先初始化，再调用sumRange 时，从 i 到 j 下标遍历 nums即可。

```python
class NumArray:
    def __init__(self, nums: List[int]):
        self.res = [nums]

    def sumRange(self, i: int, j: int) -> int:
        sum  = 0
        for k in range(i, j+1):
            sum +=  self.res[0][k]
        return sum
```

这种方式的时间复杂度与根据 sumRange 的次数和下标范围相关，由于提示中表明可能最多调用 $10^4 $次 sumRange 方法，因此其时间复杂度大大升高。因此，考虑降低sumRange中本身的复杂度，因此将索引 `left `和` right `之间的元素的总和转化为【索引 right+1之前所有元素之和】减去【索引left之前所有元素之和】，因此，在初始化时就创建nums 每个下标所对应的下标前缀元素之和，而在调用sumRange时就直接调用下标，执行减法操作即可，大大降低调用sumRange的时间复杂度。

```python
class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [0]
        SumpreArray = self.sums
        
        for num in nums:
          SumpreArray.append(SumpreArray[-1]+num)

    def sumRange(self, i: int, j: int) -> int:
      SumpreArray = self.sums
      return SumpreArray[j+1] -  SumpreArray[i]
```

