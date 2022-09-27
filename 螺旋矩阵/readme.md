## 螺旋矩阵（中等）

### 题目

给你一个 `m` 行 `n` 列的矩阵 `matrix` ，请按照 **顺时针螺旋顺序** ，返回矩阵中的所有元素。

提示：

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 10`
* `-100 <= matrix[i][j] <= 100`

### 思路

题目要求是按顺时针输出矩阵元素，无需修改矩阵本身元素。

第一种方式采用模拟方式，将遍历原矩阵中的元素数量长度（当路径的长度达到矩阵中的元素数量时即为完整路径，将该路径返回）。并用一个相同大小矩阵来记录原矩阵的元素是否被访问过，并且在超出矩阵范围时或者已经到已经访问过的位置时需要调整遍历方向，按照[0,1],[1,0],[0,-1],[-1,0]的方向来控制遍历的方向。因此，先确定当前行列序号，将其对应位置元素加入到 res 中，然后在根据方向得到下一位置坐标，然后判断下一位置坐标是否满足条件，若超出矩阵范围或者到达已访问的元素位置，则变换下一方向，然后将调整后的下一位置赋给当前行列，继续遍历。直至路径的长度达到矩阵中的元素数量时就可以返回。

```python
 def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    if matrix == None or matrix[0] == None:
        return []
    res = []
    m = len(matrix)  # 行
    n = len(matrix[0]) # 列
    visited = [[ 0 for j in range(n)] for i in range(m)] # 辅助矩阵
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    directionIndex = 0  # 初始方向
    curRow = 0 # 初始行坐标
    curCol = 0  # 初始列坐标
    
    while(i < m * n):
      # 将当前位置元素加入到结果中，并将辅助矩阵对应位置置为 True
      res.append(matrix[curRow][curCol])
      visited[curRow][curCol] = True
      i += 1
      # 确定下一坐标
      nextRow = curRow + directions[directionIndex][0]
      nextCol = curCol + directions[directionIndex][1]
      #判断是否符合条件，需要调整方向吗？
      if nextRow < 0 or nextRow >= m or  nextCol < 0 or nextCol > n or visited[nextRow][nextCol]:
        directionIndex = (directionIndex + 1) % 4
      # 变换当前坐标位置
      curRow = curRow + directions[directionIndex][0]
      curRow = curCol + directions[directionIndex][1]
      
  return res

```

以上空间和时间复杂度较高，因此第二种方式采用按层遍历，首先从左到右遍历，列到达最外层时就向下转换方向，向下到达最外层就向左转换方向；向左到达最外层再向上变换方向。注意判断是否到达最外层。

```python
def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
  if matrix == None or matrix[0] == None:
    return []
  m = len(matrix)
  n = len(matrix[0])
  
  cur = 0
  res = []
  # 上下左右的范围
  left = 0
  right = n
  bottom = 0
  top = m
  
  while(cur < m * n):
    for i in range(left,right): # 从左向右移动
      res.append(matrix[bottom][i])
      cur += 1
    if bottom == top - 1: # 判断是否到最下
      break
    bottom += 1
    
    for i in range(bottom,top): # 从上往下移动
      res.append(matrix[i][right - 1])
      cur += 1
    if left == right - 1: # 判断是否到了最右
      break
    right -= 1
    
    for i in range(right-1,left-1,-1): #从右到左移动
      res.append(matrix[top - 1][i])
      cur += 1
    top -= 1
    
    for i in range(top-1,bottom-1,-1): # 从下向上移动
      res.append(matrix[i][bottom - 1])
      cur += 1
    left += 1
    
  return res
```

最后一种方法利用 Python 的特征，在每次遍历一行时进行一次转置。次次遍历每一行。

```python
def spiralOrder3(self, matrix: List[List[int]]) -> List[int]:
  res = []
  
  while matrix:
    res += matrix.pop(0)
 # 将剩下的逆时针转九十度，等待下次被削(即转置)
    matrix = list(zip(*matrix))[::-1]
  return res
```

