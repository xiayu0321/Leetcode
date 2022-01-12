## 合并两个有序数组（简单）

### 题目

给你两个按 **非递减顺序** 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

提示：

* `nums1.length == m + n`
* `nums2.length == n`
* `0 <= m, n <= 200`
* `1 <= m + n <= 200`
* `-109 <= nums1[i], nums2[j] <= 109`

链接：https://leetcode-cn.com/problems/merge-sorted-array

### 思路

由于需要在`num1`中进行原地排序，同时 num1已经包含了 num2的长度，因此考虑先将`num2`中的元素放到 `num1`中，然后进行整体排序。在排序中，选择了快速排序算法。由此得到第一种算法。

```python
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(0,n):
            nums1[i+m] = nums2[i]
        self.quickSort(nums1,0, m+n-1)
        
    def quickSort(self, nums,l,r):
        if l >= r:
            return
        left = l
        right = r
        key = nums[l]

        while(left < right):
            while(left < right and nums[right] >= key):
                right -= 1
            if(left < right):
                nums[left] = nums[right]
                left += 1
            while(left < right and nums[left] < key):
                left += 1
            if(left < right):
                nums[right] = nums[left]
                right -= 1 
        nums[left] = key
        self.quickSort(nums,l,left-1)
        self.quickSort(nums,left+1,r)
```

在第二版算法中，由于两个数组都是非递减顺序排列的数组，所以可以考虑双指针算法 。两指针`n1`和`n2`分别指向两个数组，两个数组指向的元素进行比较，哪个比较小，就把哪个元素放到新数组中，并且相应的指针向后移动。只要有一个数组遍历完后，另一个数组后续的元素全部加入到新数组中。直至所有元素都加入到新数组中。最后，将新数组赋值给`num1`。

注意：在这版算法中，一定要注意比较的顺序。如果指针位置的比较放到后面，会导致前面读取元素时出现“指针超出 list 范围”的错误。此外，注意最后的赋值方式，不是通过`num = newList`（这种方式 num1还是原数组），而是通过` nums1[:] = newList`。

```python
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n1 = n2 = 0
        newList = []
        while n1 < m or n2 < n:
            if n1 == m:
                newList.append(nums2[n2])
                n2 += 1
            elif n2 == n:
                newList.append(nums1[n1])
                n1 += 1
            elif nums1[n1] < nums2[n2]:
                newList.append(nums1[n1])
                n1 += 1
            elif nums1[n1] >= nums2[n2]:
                newList.append(nums2[n2])
                n2 += 1
        nums1[:] = newList
```



