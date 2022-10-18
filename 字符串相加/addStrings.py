class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_m = len(num1) if len(num1) > len(num2) else len(num2)
        min_n = len(num2) if len(num1) > len(num2) else len(num1)
        arr = [0 for _ in range(max_m+1)]
        
        res = ""
        for i in range(min_n):
            temp = int(num1[-1-i]) + int(num2[-1-i]) + int(arr[i])

            res += str(temp)[-1]
            if temp >= 10:
                arr[i+1] = temp // 10
        
        for i in range(min_n,max_m):
            if len(num1) > len(num2):
                temp = int(num1[-1-i]) + int(arr[i])
            else:
                temp = int(num2[-1-i]) + int(arr[i])
                
            res += str(temp)[-1]
            if temp >= 10:
                arr[i+1] = temp // 10
        
        if arr[max_m] != 0:
            res += str(arr[max_m])
            
        return res[::-1]
    
    def addStrings2(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        add = 0 
        ans = []
        
        while(i >= 0 or j >= 0 or add != 0):
            x = ord(num1[i]) - ord('0') if i >= 0 else 0 
            y = ord(num2[j]) - ord('0')  if j >= 0 else 0 
            res = x + y + add
            ans.append(res % 10)
            add = res // 10
            i -= 1
            j -= 1
            
        return "".join(str(i) for i in ans[::-1])

if __name__ == "__main__":
    s = Solution()
    num1 = "11" 
    num2 = "123"
    print(s.addStrings2(num1,num2))