import math
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val,self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

steps = ["MinStack","push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
nums = [[],[2],[0],[3],[0],[],[],[],[],[],[],[]]
res = []
i = 0
while(i < len(steps)):
    if steps[i] == "MinStack":
        obj = MinStack()
        res.append(None)
    elif steps[i] == "push":
        obj.push(nums[i][0])
        res.append(None)
    elif steps[i] == "pop":
        obj.pop()
        res.append(None)
    elif steps[i] == "top":
        res.append(obj.top())
    elif steps[i] == "getMin":
        res.append(obj.getMin())
    i += 1

print(res)
 
