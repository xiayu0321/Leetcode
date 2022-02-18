class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a,2)
        y = int(b,2)
        res = bin(x + y)
        return res[2:]

    def addBinary1(self, a: str, b: str) -> str:
        x = int(a,2)
        y = int(b,2)
        while(y):
            answer = x ^ y
            carry = (x & y) << 1
            print("1:"+str(carry))
        return bin(x)[2:]
        
s = Solution()
print(s.addBinary1('11','1'))