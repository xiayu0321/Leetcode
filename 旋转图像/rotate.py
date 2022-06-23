from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        temp =  [[0] * n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                temp[col][n - row - 1] = matrix[row][col]
        matrix[:] = temp  
        print(matrix)    
        
    def rotate2(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
       
        # 水平翻转
        for i in range(n // 2):
            temp = matrix[n - i - 1]
            matrix[n - i - 1] = matrix[i]
            matrix[i] = temp
        print(matrix)   
        # 按对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        print(matrix)
                      
s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(s.rotate(matrix))
s.rotate2(matrix)