## 只出现一次的数字 II（中等）

### 题目

给你一个整数数组 `nums` ，除某个元素仅出现 **一次** 外，其余每个元素都恰出现 **三次 。**请你找出并返回那个只出现了一次的元素。

提示：

* 1 <= nums.length <= 3 * $10^4$
* $-2^{31} <= nums[i] <= 2^{31} - 1$
* nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现三次

链接：https://leetcode-cn.com/problems/single-number-ii

### 思路

首先，由于比较的是元素出现的次数，是可以在遍历数组时，用字典保存元素极其出现的次数（key 为元素，value 为出现的次数）。在遍历完数据后再遍历字典，如果 value 为1，则直接返回当前 key 值即可。

另一种方式是考虑只遍历一次数组。由于数组中元素要么出现一次要么出现三次，那么将数据排序，出现一次的数组与前一个元素和后一个元素都不相同，因此，在排序好元素时，遍历数组判断当前元素与前一个元素和后一个元素是否相同，不相同就返回当前元素。但这种方法需要单独考虑起始和末尾元素是单个元素需另外考虑。此外，还要考虑只有一个元素的情形。

