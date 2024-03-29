## 只出现一次的数字III（中等）

### 题目

给你一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

你必须设计并实现线性时间复杂度的算法且仅使用常量额外空间来解决此问题。

提示：

* $2 <= nums.length <= 3 * 10^4$
* $-2^{31} <= nums[i] <= 2^{31} - 1$
* 除两个只出现一次的整数外，nums 中的其他数字都出现两次

链接：https://leetcode.cn/problems/single-number-iii

### 思想

首先，我会想到先使用哈希表来统计数组中各个元素以及出现的次数，然后再遍历哈希表，找到次数为1的两个元素返回即可。

再使用哈希表时可以使用Counter包来统计数组中各个元素以及出现的次数。

这种方式的时间和空间复杂度较高，因此考虑另一方式。

由于除了两个出现1次的元素，其余两个元素仅出现两次，因此可以遍历数组，通过**异或**将数组中出现两次的元素全部消掉，最后剩下那两个仅出现1次的元素的异或值。此时要将这两个异或值进行分类。可以考虑使用**x & (-x)**取出x二进制表示中为1的最低位。由于两个数的异或值的这一位是1，因此这两个数在这一位上分别为0和1。因此再遍历数组，将其与（x & (-x)的值）进行相与计算，即可得到这两个数。

```python
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp = 0
        for num in nums:
            temp ^= num

        l = temp & (-temp)  # 得到当前值的最低位的1，此时这位为1，这两个数的这一位必定一个为0，一个为1
        type1 = type2 = 0
        for num in nums:
            if num & l:
                type1 = num
            else:
                type2 = num 
        return [type1,type2]

```





