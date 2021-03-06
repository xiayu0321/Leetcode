## 判断子序列（简单）

### 题目

给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

**提示：**

- `0 <= s.length <= 100`
- $0 <= t.length <= 10^4$
- 两个字符串都只由小写字符组成。

链接：https://leetcode.cn/problems/is-subsequence

### 思路

判断 s 是否为 t 的子序列，要关注两点：1.s 的字符都在 t 中；2.s的 字符相对位置在 t 中也是同样的。

因此，需要遍历s，根据s的当前字符，再去 t 中判断是否存在，如果存在，则 s 移动到下个字符，此时该字符在t中判断是否存在需要从上个字符所在 t 中的下标之后开始遍历，如此才能保证字符所在t的相对位置。 如果不存在，则继续遍历 t。最后在判断t 中存在 s 元素的个数，如果该个数跟 s 的长度相等，则s 所有字符都存在于 t 并且相对位置也对，那么直接返回 True，否则返回 False。

另一种算法是使用双指针，两个字符串 s 和 t 分别由指针 i 和 j 所遍历。如果s 当前字符 s[i]与 t[j]相等，说明该字符存在于 t 中，此时 i 和 j 同时移动，如果 字符 s[i]与 t[j] 不相等，则移动 j 继续查找。直至任意字符串被遍历完。最后比较 i 和 s 的长度，如果相等则返回 True，否则返回 False。