## 找到所有数组中消失的数字（简单）

### 题目

给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

**提示：**

- `n == nums.length`
- $1 <= n <= 10^5$
- `1 <= nums[i] <= n`

链接：https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array

### 思路

由题意可得，数组[1，len(nums)]存在 nums 数组中未出现的元素。因此考虑使用哈希表首先存储[1，len(nums)]的值为 key，然后遍历 nums，在哈希表中找到相应元素时，对应 value 就加一，最后再遍历哈希表，找到 value 为0的 key，即为消失的数字。

以上方法时间复杂度和空间复杂度都较高。

因此，考虑在原数组进行，将nums数组的下标作为[1，n]的数组， 并且 nums 中的数字一定在[1，n]范围内，因此遍历 nums，得到每个数在[1，n]的位置，并将该位置上的数字+n，这样出现在 nums 里的数据全部会大于 n，而小于n 的数据所对应的下标就是未出现在的数字。——注意下标和元素的关系，下标作为一个数组，元素是 nums

```python
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
	n = len(nums)
  res = []
  # 遍历nums 数组，找到元素所对应的下标，并将其位置对应数字+n
  for num in nums:
    x = (num - 1) % n
    nums[x] += n
   
  for i,num in enumerate(nums):
    if num < n:
      res.append(i+1)
      
  return res
 
```

