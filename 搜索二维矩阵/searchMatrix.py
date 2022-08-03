from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for  j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
    
        return False
    
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        # print(len(matrix))  # 行数
        # print(len(matrix[0]))  # 列数
        
        for i in range(len(matrix)):
            if matrix[i][len(matrix[0])-1] >= target:
                break
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return True
        return False
        
    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows * cols - 1
        while low <= high:
            mid = (low + high) // 2
            x = matrix[mid // cols][mid % cols]
            if x < target:
                low = mid + 1
            elif x > target:
                high = mid - 1
            else:
                return True
        return False
            
    def searchMatrix4(self, matrix: List[List[int]], target: int) -> bool:
        # 按列进行二分查找
        low = 0
        high = len(matrix)  - 1

        while(low < high):  # 终止条件是 low == high 时，刚好就是同一行
            mid =  (low + high + 1) // 2
            if matrix[mid][0]  < target:
                low = mid 
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                return True
        # 已经确定当前行，现在就是在该行进行二分查找
        left = 0
        right = len(matrix[low]) - 1  # right 为数组中最后一个元素
        while(left <= right):   # 终止条件是 left == right + 1时，此时是标准的二分查找
            mid = (left + right) // 2
            if matrix[low][mid] < target:
                left = mid + 1
            elif matrix[low][mid] > target:
                right = mid - 1
            else:
                return True
        return False
                
    
if __name__ == '__main__':
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    # print(s.searchMatrix(matrix,target))
    # print(s.searchMatrix2(matrix,target))
    print(s.searchMatrix4(matrix,target))
    
    