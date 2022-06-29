class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimum_stack) == 0:
            self.minimum_stack.append(val)
        else:
            self.minimum_stack.append(min(self.minimum_stack[-1], val))
        return

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minimum_stack.pop(-1)

    def top(self) -> int:
        return(self.stack[-1])

    def getMin(self) -> int:
        return(self.minimum_stack[-1])


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
