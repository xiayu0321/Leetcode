## Excel表列序号（简单）

### 题目

给你一个字符串 `columnTitle` ，表示 Excel 表格中的列名称。返回 *该列名称对应的列序号* 。

提示：

* 1 <= columnTitle.length <= 7
* columnTitle 仅由大写英文组成
* columnTitle 在范围 ["A", "FXSHRXW"] 内

链接：https://leetcode.cn/problems/excel-sheet-column-number

### 思路

从字符串找序号，其实也就是找对应关系，从 A 对应1开始，到 Z对应26结束，如果有下一轮就再上加，如果是 AA 就从27开始。因此可理解为26进一位。因此在遍历字符串时，判断字符与’A‘的 ascii 码直接的差值再加1，就可以确定当前字符所代表的数，如果有多位，则需要进位，即乘以26。

