## 存在重复元素 II（简单）

### 题目

给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。

提示：

- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`
- `0 <= k <= 105`

链接：https://leetcode-cn.com/problems/contains-duplicate-ii

### 思路

由于题目中需要找到重复元素的下标，并且比较重复元素下标的值是否小于给定值。因此，考虑使用**字典**，key是重复的元素，value 是一个数组，数组中存储着重复元素的下标。再遍历完数组后，字典中就存储好元素以及元素出现在数组中的下标。

然后遍历**字典**，如果 value 中的长度大于2，说明 key 所对应的元素是重复的。再比较 value 中所存储的下标。遍历 value 中存储的 list，如果有小于给定值 k 的，就直接返回 True。否则，继续遍历。如果最后遍历都没有，则返回 False。

```python
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for i in range(len(nums)):
            if nums[i] not in mapping.keys():
                mapping[nums[i]] = [i]
            else:
                mapping[nums[i]].append(i)
        for m,v in mapping.items():
            if len(v) > 1:
                for i in range(len(v)):
                    for j in range(i+1,len(v)):
                        if abs(v[j]-v[i]) <= k:
                            return True
        return False
```

由于以上方法时间复杂度太高了，所以优化以上过程。

可以考虑在存储下标时就进行判断下标之间的距离是否小于 k。只有在有重复元素的情况下，再进行判断。由于字典 value 中 list 的存储顺序是从小到大的，因此只需要比较当前下标和list 中的最后一个下标即可。综上，只需要在存储重复元素下标时进行与上一个下标比较即可。

```python

    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for i in range(len(nums)):
            if nums[i] not in mapping.keys():
                mapping[nums[i]] = [i]
            else:
                if abs(i - mapping[nums[i]][-1]) <= k:
                    return True
                else:
                    mapping[nums[i]].append(i)
        return False

```



