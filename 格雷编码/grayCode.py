import math
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0 for x in range(0,int(math.pow(2,n)))]

        for i in range(len(res)):
            res[i] = (i >> 1) ^ i
        return res
        # mapping = {}
        # for i in range(len(res)):
        #     mapping[i] = int(bin(i)[2:].zfill(n))  # 转二进制并且高位补0
        # res[0] = 0
        
        # for i in range(len(res)):
        #     for j in range(i+1,len(res)):
        #         if j not in res:
        #             temp = str(mapping[j] ^ mapping[i])
        #             if len(temp.split('1')) == 2 and res[i] == 0:
        #                 res[i+1] = j
        #             elif len(temp.split('1')) == 2 and res[-1-i] == 0:
        #                 res[- i - 1] = j
        
        # return res


s = Solution()
res = s.grayCode(3)
for i in res:
    print(str(i) +":"+bin(i))