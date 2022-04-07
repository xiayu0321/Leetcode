## 有效的字母异位数（简单）

### 题目

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

**提示:**

- `1 <= s.length, t.length <= 5 * 104`
- `s` 和 `t` 仅包含小写字母

链接：https://leetcode-cn.com/problems/valid-anagram

### 思路

字母异位数指的就是两个字符串中的所有字符和字符个数一样，因此，考虑使用字典来存储字符串中的元素以及元素个数。

由于字母异位数中字母个数要一致，因此可以通过两个字符串的长度来判断，如果不同，那肯定不是字母异位数，直接返回 False。如果相同，则需要分别遍历字符串` s` 和 `t`，用字典 `sres` 和 `tres`分别统计 `s` 和` t` 中出现的元素以及对应元素个数。最后比较两个字典是否相同，若相同，则返回 True，否则返回 False。

在最后比较字典时，我想的比较麻烦，怕字典key顺序不同影响判断， 因此考虑遍历一个字典，在判断该字典的key 是否在另一个字典中出现，若没有，则返回 False，若有，再判断两个字典中 key 对应的 value 是否相同。若不相同，则返回 False。遍历完后最后返回 True。但其实，字典直接比较，其 key 顺序不会影响结果。

```python
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sres = {}
        tres = {}
        for i in range(len(s)):
            if s[i] not in sres.keys():
                sres[s[i]] = 1
            else:
                sres[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in tres.keys():
                tres[t[j]] = 1
            else:
                tres[t[j]] += 1   
        return sres == tres 

        # for m in sres.keys():
        #     if m not in tres.keys():
        #         return False
        #     if sres[m] != tres[m]:
        #         return False
        # return True
```

还有更简单的方法，既然字母异位数中字符相同以及字符出现的个数相同，那么直接两个字符串排序后进行比较，若排序后相等，则直接返回 True，否则返回 False。