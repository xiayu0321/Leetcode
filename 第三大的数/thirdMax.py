from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                count += 1
                if count == 3:
                    return nums[i]
        return nums[0]

    def thirdMax2(self, nums: List[int]) -> int:
        arr = list()

        for i in range(len(nums)):
            if nums[i] not in arr:
                arr.append(nums[i])
                if len(arr) > 3:
                    arr.sort()
                    arr.pop(0)
        arr.sort()
        return arr[0] if len(arr) == 3 else arr[-1]

    def thirdMax3(self, nums: List[int]) -> int:
        a,b,c = float('-inf'), float('-inf'),float('-inf')
        for i in range(len(nums)):
            if nums[i] > a:
                c = b
                b = a
                a = nums[i]

            elif b < nums[i] and nums[i] < a:
                c = b
                b = nums[i]

            elif c < nums[i] and nums[i] < b:
                c = nums[i]

        return a if c == float('inf') else c

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,2,5,3,5]
    print(s.thirdMax3(nums))