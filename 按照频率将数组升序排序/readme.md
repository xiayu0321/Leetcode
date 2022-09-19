## 按照频率将数组升序排序（简单）

### 题目

给你一个整数数组 nums ，请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，请你按照数值本身将它们 降序 排序。 

请你返回排序后的数组。

**提示：**

- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

### 思路

题目中要求对数组进行频率升序排序，同时对于频率相同的元素要进行降序排序。首先考虑使用哈希表记录数组中的频率。但由于哈希表统计时是按照元素在原数组中的顺序进行统计。因此，为了后续数组降序排序，先对整个数组进行降序排序，然后遍历数组用哈希表记录元素以及对应元素出现的频率。由于要按照元素频率进行降序，因此通过使用 sort 函数按照哈希表的 values 进行升序排序，即`num_fre = sorted(num_fre.items(),key=lambda x:x[1],reverse=False)`，此时排序完的结果是 list，list 中每个元素是 tuple，包含了元素以及元素对应的频率。最后在遍历该 list，再按照每个tuple中 value 的个数将 key 加入到 res 中，等遍历完 list 后，直接返回 res。

以上方法的时间复杂度和空间复杂度较好，利用 Counter 和 sort 函数即可。

```python
 def frequencySort2(self, nums: List[int]) -> List[int]:
    cnt =  Counter(nums)
    nums.sort(key = lambda x: (cnt[x],-x))
    return nums

```