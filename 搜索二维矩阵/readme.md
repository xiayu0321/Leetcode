## 搜索二维矩阵（中等）

### 题目

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

* 每行中的整数从左到右按升序排列。
* 每行的第一个整数大于前一行的最后一个整数。

提示：

* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 100
* $-10^4 <= matrix[i][j], target <= 10^4$

链接：https://leetcode.cn/problems/search-a-2d-matrix

### 思路

题目中考虑是在二维数组中是否能找到 target 值，因此，不考虑二维矩阵中的特性，就可直接通过遍历二维数组方式进行判断。但这种方式要经过两层循环，时间复杂度较高。因此可以考虑借助二维矩阵的特性，从左至右升序排序，从上到下升序排列，每一行比上一行的最后一个数值大。所以可以考虑通过遍历每一行的最后一个值与 target 比较大小，以此来确定在一行寻找，然后确定行以后再在该行遍历比较，以确定是否存在 target。这种方式将原来的二层循环改为两个一层循环，降低了时间复杂度。

```python
        # 确定行
  			for i in range(len(matrix)):
            if matrix[i][len(matrix[0])-1] >= target:
                break
        # 确定列
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return True
        return False
```

另外，考虑二维数组中的数据以一维数组的形式来看，是递增数组。因此可以考虑在一维数组形式上使用二分查找算法。low 为第一行第一个元素，即 low = 0；而 high 是二维数组最后一行最后一个元素，即 `high = len(matrix) * len(matrix[0]) - 1`，只要 low <= high，就找到中值元素 `x = matrix[mid//cols][mid % cols]`与target进行比较。如果相等，就直接返回 True，否则就移动 high 或者 low 的位置，只到遍历完毕，若遍历完还未找到就返回 False。这种方法的关键是如何找到中值元素，将一维转化为二维。在该方法仅针对数组中每行元素相等的情况。

适用性最强的方法还是套用先确定行再在行中确定元素的路线。首先在二维数组的第一列中通过二分查找方式确定target 可能存在的行，然后在该行再通过二分查找的方式确定该行是否存在 target。这种方式比第二种仅遍历的方式时间复杂度要低。在列中进行二分查找，只需要关注第一列的所有元素，此时 low = 0，high = len(matrix) - 1，只要 low < high，比较 `matrix[(low+high+1)//2][0]`与 target 的大小。 最后返回的 low 就是 target 所在的行坐标。然后就再该行使用二分查找方法，此时 left = 0，right=len(matrix[0]) - 1，只要 left <=right，比较`matrix[low][(left+right)//2]`与 target 大小。如果恰好等于，说明二维数组中存在，则直接返回 True。如果遍历完都没有找到，说明二维数组中不存在 target，返回 False。

* 如需定义左闭右开的「搜索区间」搜索左右边界，只要在 `nums[mid] == target` 时做修改即可，搜索右侧时需要减一。
* 如果将「搜索区间」全都统一成两端都闭，好记，只要稍改 `nums[mid] == target` 条件处的代码和返回的逻辑即可。