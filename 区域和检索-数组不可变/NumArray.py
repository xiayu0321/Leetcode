from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.res = [nums]

    def sumRange(self, i: int, j: int) -> int:
        sum  = 0
        for k in range(i, j+1):
            sum +=  self.res[0][k]
        return sum
    
class NumArray1:
    
    def __init__(self, nums: List[int]):
        self.sums = [0]
        _sums = self.sums

        # 每一个下标存储相应下标的前缀和
        for num in nums:
            _sums.append(_sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        # 此时就两个前缀和相减即可
        _sums = self.sums
        return _sums[j + 1] - _sums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)