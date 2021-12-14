## 三数之和（中等）

### 题目

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

**提示：**

- `0 <= nums.length <= 3000`
- `-105 <= nums[i] <= 105`

链接：https://leetcode-cn.com/problems/3sum

### 思路

在我的思路中，首先遍历数组，然后再遍历剩下的数组，根据两重遍历可以确定两个数字，再通过『三数之和为0』的条件，再判断剩下所有元素中是否存在『两数之和的相反数』。如果存在，那么这三个数就是一组三数之和为0的三元组。最后在加入结果集中进行重复性判断，如果结果集中包含了相同的三元组，就无需加入。直至所有元素遍历完毕。但在这种方式下，算法的重复判断和遍历的时间复杂度太高，对于数据量大的情况，会产生时间超出限制的问题。

```python
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ress = []
        res = []

        if len(nums) < 3:
            return ress

        for i in range(len(nums)):
            j = i + 1
            while(j < len(nums)):
                if -(nums[i] + nums[j]) in nums[j+1:]:
                    res.append(nums[i])
                    res.append(nums[j])
                    res.append(-(nums[i] + nums[j]))
                    # 重复性判断
                    res.sort()
                    if res not in ress:
                        ress.append(res)
                    res = []
                j = j + 1

        return ress
```

由于上述思路的时间复杂度太高，需要新的算法降低时间复杂度。此时可以借鉴两数之和的双指针算法，因此，初始时需要将数组进行排序。此外，在判断重复性时，可以减少重复判断的参数。

首先遍历数据进行第一次循环，在第一重循环中，确定了三数中的第一个数，即通过三数之和为0的条件得到剩下两个数的目标值，则剩下的问题就转换为两数之和，在这种情况下，可以使用两数之和中的双指针算法。在余下数组中分为左指针和右指针。左指针代表第二个数，它从小到大进行遍历，右指针代表第三个数，他从大到小进行遍历，如果两数之和大于目标值，则需要右指针左移，直至两数之和等于目标值。如果左右指针相遇，遍历结束。

此外，还需进行重复性判断，则需要在第一个数和第二个数变化时，分别与他们上一次的数值进行相等判断，如果他们与上次的数相等，就直接换到下一个数，如果不相等，就再找第三个数，这样能够减少大量重复计算，从而减少时间复杂度。

```python
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
      	# 排序，为后面双指针算法做铺垫
        nums.sort()
        ans = list()

        # 第一重循环，找第一个数
        for first in range(n):
            # 在第一个数变化时，需要判断与上次数值是否相同，如果相同，就直接变到下一个数；如果不同，再确定第二和第三个数
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # 得到第一个数之后，将问题转化为两数之和
            target = -nums[first]
            # 两数之和的右指针初始位置
            third = n - 1
            
            # 第二重循环，在余下数组中得到第二个数
            for second in range(first + 1, n):
                # 在第二个数变化时，需要判断是否与上一次数相同，直到找到与上次不同的元素
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 在左右指针同时遍历时，需要保证右指针始终在左指针的右边，如果两数之和>target，则第三个数往小的数找，即右指针向左移动
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，在第二个数确定的情况下，第三个数已经遍历结束，第二个数可以改变
                if second == third:
                    break
                # 此时找到了相应的三个数
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans
```

