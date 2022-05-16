class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        for i in range(1,num//2+1):
            if i * i == num:
                return True     
        return False

    def isPerfectSquare2(self, num: int) -> bool:
        x = 1
        sq = 1
        # 这种方式判断次数大大减小(因为主要是比较平方值)
        while(sq <= num):
            if sq == num:
                return True
            x += 1
            sq = x * x
        return False
    def isPerfectSquare3(self, num: int) -> bool:
        left = 0
        right = num
        while(left <= right):
            mid = (left+right) // 2
            sq = mid * mid
            if sq > num:
                right = mid - 1
            elif sq < num:
                left = mid + 1
            else:
                return True
        return False
                
s = Solution()
print(s.isPerfectSquare2(2000105819))