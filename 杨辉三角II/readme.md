## 杨辉三角 II（简单）

## 题目

给定一个非负索引 `rowIndex`，返回「杨辉三角」的第 `rowIndex` 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

提示：

- `0 <= rowIndex <= 33`

链接：https://leetcode-cn.com/problems/pascals-triangle-ii/

### 思路

要找到第` rowIndex` 行的元素，就需要先构造出当前行元素，又由于杨辉三角的当前行与前一行的元素有关，因此找到第` rowIndex` 行的元素，也就是先构造` rowIndex` 行的杨辉三角，然后返回最后一行元素即可。

由于杨辉三角的前两行元素固定不变，因此直接初始化。然后从第三行开始构造，每一行的第一个元素和最后一个元素都为1，本行中间的元素根据上一行的元素计算得到，所以遍历上一行元素，通过`temp.append(triangular[i-1][j]+triangular[i-1][j+1])`进行计算。

在构造完` rowIndex` 行的杨辉三角，直接返回`rowIndex`行即可。

