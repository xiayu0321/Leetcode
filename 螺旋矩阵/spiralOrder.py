from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == None or matrix[0] == None:
            return []
        
        m = len(matrix) # 行
        n = len(matrix[0]) # 列
        visited = [[False for j in range(n)] for i in range(m)]  #记录当前位置的相应元素是否访问过
        directions = [[0,1],[1,0],[0,-1],[-1,0]]  # 螺旋的四个方向
        directionIndex = 0
        res = []
        
        curRow = 0
        curCol = 0
        
        # 遍历矩阵中所有元素
        for _ in range(m * n):
            res.append(matrix[curRow][curCol])
            visited[curRow][curCol] = True
            
            # 确定下一坐标
            nextRow = curRow + directions[directionIndex][0]
            nextCol = curCol + directions[directionIndex][1]
            # 判断下一坐标是否合法
            if nextRow < 0 or nextRow >= m or nextCol < 0 or nextCol >= n or visited[nextRow][nextCol]:
                directionIndex = (directionIndex + 1) % 4
            
            # 然后将下一坐标赋给当前坐标进行遍历 
            curRow = curRow + directions[directionIndex][0]
            curCol = curCol + directions[directionIndex][1]
            
        return res
    
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        if matrix == None or matrix[0] == None:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        # 四个方向
        left = 0
        right = n 
        bottom = 0
        top = m 
        
        cur = 0
        res = []
        
        # 判断每个坐标是否超出范围，如果超出范围则变向
        while(cur < m * n):
            for i in range(left,right):
                res.append(matrix[bottom][i])
                cur += 1
            if bottom == top - 1:
                break
            bottom += 1
            
            for i in range(bottom,top):
                res.append(matrix[i][right - 1])
                cur += 1
            if left == right - 1:
                break
            right -= 1
            
            for i in range(right-1,left-1,-1):
                res.append(matrix[top-1][i])
                cur += 1
            top -= 1        
                
            for i in range(top-1,bottom-1,-1):
                res.append(matrix[i][bottom-1])
                cur += 1
            left += 1 
                   
        return res

    def spiralOrder3(self, matrix: List[List[int]]) -> List[int]:
            res = []
            while matrix:
                # 将第一层先加入
                res += matrix.pop(0)
                # 将剩下的逆时针转九十度，等待下次被削(即转置)
                matrix = list(zip(*matrix))[::-1]
            return res
    
              
if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(s.spiralOrder2(matrix=matrix))