## 单词拆分（中等）

### 题目

给你一个字符串`s `和一个字符串列表`wordDict`作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

提示：

* `1 <= s.length <= 300`
* `1 <= wordDict.length <= 1000`
* `1 <= wordDict[i].length <= 20`
* `s` 和 `wordDict[i]` 仅有小写英文字母组成
* `wordDict` 中的所有字符串 **互不相同**

链接：https://leetcode-cn.com/problems/word-break

### 思路

初始分析题目时，我认为是将字符串`s`按字符拆解，再按`s`字符串本身顺序增加字符形成新子串与`wordDict`中的字符进行对比。首先，确定新子串的起始下标`start`为0，再逐一遍历字符串`s`以形成新子串。如果`wordDict`中存在新子串，就将当前字符下标存储至`indexs`中，并将下一个新子串的起始下标`start`移动至当前下标。最终，在遍历完字符串`s`后，就可以将字符串`s`中含有`wordDict`中字符串的下标存储下来。最后遍历数组`indexs`，如果他存储的最后一个下标是字符串 `s`的长度，那么说明以数组 `s`最后一个元素结尾的字符串也是 `wordDict` 中的一个字符串，那么就说明字符串`s`可以由 `wordDict` 中的字符串组合形成。

但以上这个想法在 `case：s = 'aaaaaaa'，wordDict=['aaaa','aaa']`中出现问题，由于我们在形成新字符串时会从短到长形成再判断，因此它只会将`s`拆解为`aaa`,`aaa`和`a`。此时就会出错。因此，我们不仅要考虑当前下标前面形成的新字符串是否被包含在 `wordDict `中，还要考虑当前下标后面形成的字符串，因此我在判断 `s[start:i]`的同时也进行了`s[i:]`的判断。

综上形成第一版的代码。

```python
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        indexs = []
        start = 0
        res = s
        for i in range(len(s)+1):
            if s[start:i] in wordDict:
                indexs.append(i)
                res = s[i:]
                start = i
            if res in wordDict:
                res = None
                indexs.append(len(s))
                break
        if indexs[-1] == len(s):
            return True
        return False
```

但以上这个想法在`case: s = 'goalspecial' , wordDict = ['go','goal','goals','special']`中会出错。在判断子串`go`后无法进行回溯再形成新的子串 `goal`。因此，从这个 case 考虑，需要考虑回溯过程，如果有一种字符串形式不能被匹配，是否能考虑重新构成新字符串形式进行匹配，也就是有状态的变化，可以考虑使用动态规划。

在动态规划中，首先需要考虑『每个阶段的状态』、『状态转移过程』以及『边界条件』

因此，首先考虑状态。可以定义`dp[i]`作为字符串`s`中的前`i`个字符组成的新字符串 `s[0:i-1]`能否被拆分成wordDict 中的单词。

然后考虑状态转移过程。在前`i`个字符串中，我们需要枚举包含『位置`i-1`的最后一个字符的所有新字符串』是否在`WordDict`以及除去这部分是否也在`wordDict`中。即： `s[0:i]`中有枚举点`j`，此时将 `s[0:i]`分为两部分：$s_1$（`s[0:j-1]`）和$s_2$(`s[j:i-1]`）。而$s_1$判断的结果就是我们定义的一个状态，即`dp[j]`，而$s_2$就是我们需要进行验证的部分。因此可得到状态转移方程：$dp[i]=dp[j] + check(s[j:i-1])$。

最后考虑边界条件。可定义 ${dp}[0]=true$表示空串且合法。

在确定三大条件，形成了动态规划的思路。

```python
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(n + 1):
            for j in range(i,-1,-1):
                if dp[j] and s[j : i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
```





 





