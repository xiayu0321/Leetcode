from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn < 0 or turnedOn > 8:
            return []
        res = []
        for i in range(12):
            for j in range(60):
                if bin(i).count("1") + bin(j).count("1") == turnedOn:
                    res.append(f"{i}:{j:02d}")
        return res
        
s = Solution()
turnedOn = 1
print(s.readBinaryWatch(turnedOn))