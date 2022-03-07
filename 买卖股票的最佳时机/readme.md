## 买卖股票的最佳时期（简单）

### 题目

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

提示：

- `1 <= prices.length <= 105`
- `0 <= prices[i] <= 104`

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock

### 思路

从题意上看，目的是为了找到数组中一组差值最大的两个数字，并且前一个数字要比后一个数字小。因此考虑暴力算法。首先第一重遍历数组确定买入时间，然后在第二重遍历时，通过比较当前 price 和买入时间的 price 的差值与 max_profit，寻找差值最大的 max_profit。在第二重循环中，考虑使用了双指针算法。在遍历完成后，就能得到结果。

```python
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        for i in range(len(prices)):
            left = i
            right = len(prices) - 1

            while(left < right):
                if prices[left] < prices[right]:
                    temp = prices[right] - prices[left]
                    if temp > max_price:
                        max_price = temp
                    else:
                        right -= 1
                else:
                    right -= 1

        return max_price
```

但上述算法时间复杂度大，导致在大数量的测试用例中，超出时间限制。因此，考虑第二种算法。

此时我们无需寻找具体的一组差值最大的两个数字，而是直接比较差值（利润值）。在遍历数组时，我们可以得到当前下标之前数组中的最小值，即之前股票的最低价。同时还可以比较当前下标所指向的元素-之前的所有最小值与 max_profit 的大小。此时 max_profit 在每次遍历时保存的就是利润最大值，minPrice 表示的是当前下标之前数组中的最小值，二者同步更新。因此，在遍历完一遍数组后就能得到利润最大的值。

```python
   def maxProfit(self, prices: List[int]) -> int:
  			inf = 1e4
        minPrice = inf
        max_price = 0

        for price in prices:
            max_price = max(max_price, price - minPrice)
            minPrice = min(minPrice,price)
        return max_price
```

