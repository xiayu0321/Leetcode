class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        res = ""
        for i in range(len(l)):
            res += l[i][::-1]
            res += " "
            
        return res[:-1]


if __name__ == "__main__":
    s = Solution()
    m = "Let's take LeetCode contest"
    print(s.reverseWords(s = m))