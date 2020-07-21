class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.l1 = []
        

    def push(self, x: int) -> None:
        if not self.min or self.min[-1] >= x:
            self.min.append(x)
        self.l1.append(x)

    def pop(self) -> None:
        if len(self.min) == 0 or self.l1[-1] == self.min[-1]:
            self.min.pop(-1)
        return self.l1.pop(-1)

    def top(self) -> int:
        return self.l1[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()