## 下一个更大元素 I（简单）

### 题目

nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。

给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。

对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。

返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。

提示：

* 1 <= nums1.length <= nums2.length <= 1000
* 0 <= nums1[i], nums2[i] <= $10^4$
* nums1和nums2中所有整数 互不相同
* nums1 中的所有整数同样出现在 nums2 中

链接：https://leetcode.cn/problems/next-greater-element-i

### 思路

题目要求将 nums1中的元素在 num2找到对应位置后，再从对应位置后判断是否有大于该位置元素的元素。因此，我首先考虑暴力解法：首先将 num1中的元素在 num2中找到定位，然后再从该定位遍历 num2，找到是否存在元素大于该定位元素。

```python
        l = len(nums1)
        res = [-1 for _ in range(l)]
        
        for i in range(l):
          # 在 num2中定位当前元素下标
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    break
          # 遍历num2中剩下元素，寻找比当前元素大的元素  
            for k in range(j,len(nums2)):
                if nums2[k] > nums1[i]:
                    res[i] = nums2[k]
                    break
        return res
```

以上方法时间复杂度和空间复杂度较高。因此考虑使用单调栈+哈希表的方法。题目要求可大致分为两步：首先在 num2中找到每个元素所对应的右侧第一个大于原元素的值；然后再存储该元素以及所对应的右侧第一个大于原元素的值。因此，考虑倒序遍历nums2，用栈寻找每个元素所对应的右侧第一个大于原元素的值。即每移动到新的位置 i，就把栈中小于当前元素的所有元素弹出，以保证栈顶元素为当前位置右边的第一个更大的元素。如果栈为空则说明当前位置右边没有更大的元素。此时用哈希表存储当前元素以及栈顶元素的对应关系，最后将当前元素入栈，以进行下一轮。

```python
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
  res = {}
  stack = []
  
  for num in reversed(nums2):
    while(stack and stack[-1] <= num):
      stack.pop()
    res[num] = stack[-1] if stack else -1
    stack.append(num)
  return [res[num] for num in nums1]
```

