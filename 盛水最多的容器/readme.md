## 盛水最多的容器（中等）

### 题目

给你`n `个非负整数 `a1，a2，...，an`，每个数代表坐标中的一个点` (i, ai)` 。在坐标内画 `n` 条垂直线，垂直线`i` 的两个端点分别为` (i, ai)` 和 `(i, 0)` 。找出其中的两条线，使得它们与` x` 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

提示：

- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 104`

链接：https://leetcode-cn.com/problems/container-with-most-water

### 思路

分析题目可得，找到盛水最多的容器其实是找到两个数值中较小值和他们下标差值的乘积，通过比较乘积值得到结果。

因此，我想到最基础的方法，通过两重循环，得到数组中的任意两个数`height[i]`和`height[j]`，比较得到两者之间的较小值`max(height[i],height[j])`和下标差值`abs(j-i)`，进行乘积运算得到当前面积值`area`，再与最大面积值`maxArea`比较。如果当前面积值与最大面积值大，就将最大面积值更新。在遍历结束后，得到的最大面积值就是盛水最多的容器。但这种方法由于需要两重循环，时间复杂度高，易造成出现超出时间限制情况。

```python
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        for i in range(len(height)):
            for j in range(i,len(height)):
                w =  j - i
                h = min(height[i],height[j])
                area = w * h
                if area > maxArea:
                    maxArea = area
        return maxArea
```

由于第一版算法时间复杂度高，因此考虑如何能够降低循环次数。由于分析题目还是需要找数组中的最大值，并且要尽可能的寻找下标差值最大的情况，因此，可以考虑使用双指针算法。首先，对数组`height`设定左右指针`left`和`right`，根据左右指针和他们对应的元素就可计算出当前面积值`area`，然后与最大面积值`maxArea`进行比较，如果当前值比最大面积值大，就更新最大面积值`maxArea`。如果比最大面积值小，则需要调整指针走向。在调整指针走向时，需要考虑是左指针往右移动还是右指针向左移动。根据题目分析需要寻找元素值较大的那个，因此，哪个指针所指向的元素值小就移动哪个指针。

```python
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while(left  < right):
            area = (right - left) * min(height[left],height[right])
            if area > maxArea:
                maxArea = area
            else:
                if height[right] < height[left]:
                    right -= 1
                else:
                    left += 1
        return maxArea

```

