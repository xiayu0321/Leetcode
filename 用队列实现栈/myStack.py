import collections


class MyStack2:

    def __init__(self):
        self.queue = collections.deque()


    def push(self, x: int) -> None:
        n = len (self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())


    def pop(self) -> int:
        return self.queue.popleft()


    def top(self) -> int:
        return self.queue[0]


    def empty(self) -> bool:
        return not self.queue

class MyStack:

    def __init__(self):
        self.queueOne = collections.deque()
        self.queueTwo = collections.deque()


    def push(self, x: int) -> None:
        self.queueTwo.append(x)
        while self.queueOne:
            self.queueTwo.append(self.queueOne.popleft())
        self.queueOne,self.queueTwo = self.queueTwo,self.queueOne


    def pop(self) -> int:
        return self.queueOne.popleft()


    def top(self) -> int:
        return self.queueOne[0]


    def empty(self) -> bool:
        return not self.queueOne