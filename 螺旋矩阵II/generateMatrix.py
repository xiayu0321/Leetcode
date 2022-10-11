from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        
        visited = [[False for _ in range(n)] for _ in range(n)]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        direacitonIndex  = 0
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        curRow = 0
        curCol = 0 
        
        for i in range(n*n):
            matrix[curRow][curCol] = i+1
            visited[curRow][curCol] = True
            
            nextRow = curRow + directions[direacitonIndex][0]
            nextCol = curCol + directions[direacitonIndex][1]
            
            if nextRow < 0 or nextRow >= n or nextCol < 0 or nextCol >= n or visited[nextRow][nextCol]:
                direacitonIndex = (direacitonIndex + 1) % 4
            
            curRow = curRow + directions[direacitonIndex][0]
            curCol = curCol + directions[direacitonIndex][1]

        return matrix
    
    def generateMatrix2(self, n: int) -> List[List[int]]:
        # 定义边界
        l = 0
        r = n - 1
        t = 0
        b = n - 1
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        num = 1
        
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

if __name__ == "__main__":
    s = Solution()
    print(s.generateMatrix2(3))