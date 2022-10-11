## 螺旋矩阵II （中等）

### 题目

给你一个正整数 `n` ，生成一个包含 `1` 到 `n2` 所有元素，且元素按顺时针顺序螺旋排列的 `n x n` 正方形矩阵 `matrix` 。

**提示：**

- `1 <= n <= 20`

链接：https://leetcode.cn/problems/spiral-matrix-ii/

### 思路

相反于【螺旋矩阵I】中将数组螺旋输出的要求，本题是要求将有序数据按照螺旋方式生成矩阵。但做法可以借鉴。

第一种做法：确定辅助数组来确定当前位置是否已经填充过，以及转向数组以确定方向以及下标来确定当前在哪个方向。首先确定当前位置 curRow 和 curCol，然后确定循环次数（当前值小于n*n），在循环内，首先在 matrix当前位置赋值同时将辅助数组中当前位置的元素改变，表明该位置已经改变了。然后根据转向下标来确定下一个元素的位置：            `nextRow = curRow + directions[direacitonIndex][0]`以及` nextCol = curCol + directions[direacitonIndex][1]`。然后先判断下一个位置的坐标是否超出范围（坐标与数组边界判断）或者是否已经被改过（通过辅助数组），如果符合条件，则调整转向下标。最终再确定转向下标后将下一坐标赋给当前坐标即可。

```python
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        # 辅助数组以及转向数组以及下标
        visited = [[False for _ in range(n)] for _ in range(n)]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        direacitonIndex  = 0
        # 初始化最终形成的数组
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        curRow = 0
        curCol = 0 
        # 遍历
        for i in range(n*n):
            matrix[curRow][curCol] = i+1
            visited[curRow][curCol] = True
            # 确定下一坐标
            nextRow = curRow + directions[direacitonIndex][0]
            nextCol = curCol + directions[direacitonIndex][1]
            # 判断下一坐标是否在范围之内
            if nextRow < 0 or nextRow >= n or nextCol < 0 or nextCol >= n or visited[nextRow][nextCol]:
                direacitonIndex = (direacitonIndex + 1) % 4
            # 将下一坐标赋予当前坐标，以形成下一次的位置
            curRow = curRow + directions[direacitonIndex][0]
            curCol = curCol + directions[direacitonIndex][1]

        return matrix
```

第二种方式：直接按照螺旋的方式对数组赋值。首先确定数组的下标范围：l，r，t，b = 0， n-1，0，n-1，以及初始值 num = 1，只要数值小于等于 n*n，就遍历matrx 进行赋值。按照顺时针方向：首先在`[l,r-1]`内，matrix只需要移动列标，行标不动，进行赋值，同时 num++；在一行赋值完毕后，下一次在这个方向就要从第二行开始了，因此 t+1；然后在`[t,b+1]`内，matrix只需要移动行标，列标不动，进行赋值，同时 num++；在一列赋值完毕后，下一次在这个方向就要从倒数第二列开始，因此r-1；再在`[r,l-1]`内，matrix只需要移动列标，行标不动，进行赋值，同时 num++；在一行赋值完毕后，下一次在这个方向就要从倒数二行开始了，因此b-1；最后在`[b,t-1]`内，matrix只需要移动行标，列标不动，进行赋值，同时 num++；在一列赋值完毕后，下一次在这个方向就要从第二列开始，即 l+1。

```python
def generateMatrix2(self, n: int) -> List[List[int]]:
        # 定义边界
        l = 0
        r = n - 1
        t = 0
        b = n - 1
        # 初始化返回数组
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        num = 1
        # 按顺时针遍历
        while(num <= n*n):
            for i in range(l,r+1):
                matrix[t][i] = num
                num += 1
            t += 1
            for i in range(t,b+1):
                matrix[i][r] = num
                num += 1
            r -= 1
            for i in range(r,l-1,-1):
                matrix[b][i] = num
                num += 1
            b -= 1
            for i in range(b,t-1,-1):
                matrix[i][l] = num
                num += 1
            l += 1  
        return matrix       

```

