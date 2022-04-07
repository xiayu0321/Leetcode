## 颜色分类（中等）

### 题目

给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库的sort函数的情况下解决这个问题。

**提示：**

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` 为 `0`、`1` 或 `2`

**进阶：**

- 你可以不使用代码库中的排序函数来解决这道题吗？
- 你能想出一个仅使用常数空间的一趟扫描算法吗？

链接：https://leetcode-cn.com/problems/sort-colors

### 思路

首先根据题目可以发现，即对元素只有0，1，2的数组进行从小到大排序，因此想到了最简单的排序算法：冒泡排序，此为第一种算法。

```python
    def sortColors(self, nums: List[int]) -> None:     
        for i in range(1,len(nums)):
            for j in range(len(nums)-i):
                if nums[j+1] < nums[j]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
```

若不采用排序算法，则可以换一种思路，由于元素只有0，1，2三类，因此可以通过多次遍历，将数组中所有0元素放置到数组前端，再将数组中所有1元素放置到0元素之后，那么剩下的元素全是2元素了。综上，可以设置单指针 `pre`，它表示在它之前的所有元素已经按序排好。因此，在第一次遍历时，如果发现数组有0元素，就将0元素放置到 `pre`所指向的位置；在第二次遍历，如果发现数组有1元素，就将0元素放置到 `pre`所指向的位置。再经历过两次遍历时就形成有序数组了。

```python
    def sortColors(self, nums: List[int]) -> None:
        pre = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[pre],nums[i] = nums[i],nums[pre]
                pre += 1
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[pre],nums[i] = nums[i],nums[pre]
                pre += 1
```





