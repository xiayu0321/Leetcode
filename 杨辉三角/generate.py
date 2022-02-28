from typing import List

from numpy import append


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        if numRows == 2:
            res.append([1,1])
            return res
        
        res.append([1,1])
        for m in range(2,numRows):
            t = [1]
            for i in range(len(res[m - 1]) - 1):
                t.append(res[m - 1][i]+res[m - 1][i+1])
            t.append(1)
            res.append(t)

        return res

s = Solution()
print(s.generate(2))

        