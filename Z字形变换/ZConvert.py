class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for e in range(0,numRows)]
        resStr = ''
        n = len(s)
        if numRows == 1:
            return s

        for i in range(n):
            for space in range(numRows,0,-1):
                if i % (2 * numRows - 2) == space - 1:
                    res[space - 1].append(s[i])
                elif i % (2 * numRows - 2) == 2 * numRows - space - 1:
                    res[space - 1].append(s[i])

        for i in res:
            for j in i:
                resStr += j
        return resStr
    
    def convert1(self, s: str, numRows: int) -> str:
        res = [[] for e in range(0,numRows)]
        resStr = ''
        n = len(s)

        if numRows == 1:
            return s

        curRow = 0 
        goingDown = False

        for c in s:
            res[curRow].append(c)
            if (curRow == 0 or curRow == numRows - 1):
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        for i in res:
            for j in i:
                resStr += j
        return resStr

m = Solution()
s = "PAYPALISHIRING"
numRows = 5
print(m.convert(s,numRows))