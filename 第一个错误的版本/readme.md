## 第一个错误的版本（简单）

### 题目

品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

**提示：**

- `1 <= bad <= n <= 231 - 1`

示例 1：

输入：n = 5, bad = 4
输出：4
解释：
调用 isBadVersion(3) -> false 
调用 isBadVersion(5) -> true 
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。

链接：https://leetcode.cn/problems/first-bad-version

### 思路

由示例看出， 由于错误版本之后的所有版本都是错的，其实是要找到最早isBadVersion为 false的数字。同时题目要求减少调用 API 的次数，因此可以利用二分查找的思想，如果当前版本差错，则继续向前找，如果当前版本正常，则继续向后找，直到汇聚在一个元素上，最后将该元素返回。