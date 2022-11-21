## 最大连续1的个数（简单）

### 题目

给定一个二进制数组 `nums` ， 计算其中最大连续 `1` 的个数。

**提示：**

- $1 <= nums.length <= 10^5$
- `nums[i]` 不是 `0` 就是 `1`.

### 思路

由于题目中数组中每个元素不是0就是1，因此寻找最大连续1的个数，可以通过遍历原数组，遇到1的时候，1的个数加1，遇到0时先计算此时连续1的个数count，并与最大连续1的个数maxCount进行比较，同时需要将 count=0，以便下一次计数。此外，要考虑最后一次没有0的情况，需要在遍历完数组后，再对最后一次计数 count 与 maxCount 进行比较即可。

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
  count = 0
  maxCount = 0
  
  for num in nums:
    if num == 1:
      count += 1
    elif num == 0:
      if count > maxCount:
        maxCount = count
      count = 0
  if count > maxCount:
    maxCount = count
  return maxCount
```

另一种通过快慢指针进行计算。在遍历数组时，遇到1时，移动右指针，每移动一次右指针，就计算一次此时连续1的个数与之前统计的1的个数结果，在遇到0时，同样移动右指针，同时将左指针移动到右指针位置上，以为下次统计奠定基础。

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
  left = right = 0
  
  for i in range(len(nums)):
    if nums[i] == 1:
      right += 1
      res = max(right-left, res)
    if nums[i] == 0:
      right += 1
      left = right
      
  return res
```

