from random import triangular
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangular = []
        triangular.append([1])
        triangular.append([1,1])

        if rowIndex < 2:
            return triangular[rowIndex] 
        
        for i in range(2,rowIndex+1):
            temp = []
            temp.append(1)
            for j in range(len(triangular[i-1]) - 1):
                temp.append(triangular[i-1][j]+triangular[i-1][j+1])
            temp.append(1)
            triangular.append(temp)
            
        return triangular[rowIndex]

s = Solution()

print(s.getRow(10))
