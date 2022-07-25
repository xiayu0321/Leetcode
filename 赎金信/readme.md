## 赎金信（简单）

### 题目

给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。

提示：

* 1 <= ransomNote.length, magazine.length <= 105
* ransomNote 和 magazine 由小写英文字母组成

链接：https://leetcode.cn/problems/ransom-note

### 思路

该题本质是比较两个字符串的各个字符个数是否有小于等于关系，并且magazine 中的每个字符只能在 ransomNote 中使用一次。因此，只要magazine 每个字符的统计字数大于ransomNote每个字符的统计个数即可。

综上，首先先比较两个字符串的长度，如果magazine 的长度小于ransomNote，那么说明magazine 的字母不足以组成ransomNote，因此直接返回 False。然后，通过字典countChar统计ransomNote字符串的所有字符的个数，然后再遍历magazine中的字符，如果该字符在countChar中，就减去1，如果不做就不用操作。在遍历完后，再查看countChar中的字母个数，如果个数有大于1的，说明ransomNote的字母有多余字符，因此，直接返回 False。如果没有则返回 True。

另一种简单方法是使用 python 中的collections.Counter()方法可直接统计各个字符个数，通过==进行比较二者是否相等。

