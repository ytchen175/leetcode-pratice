class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif len(self.min_stack) > 0 and self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        last = self.stack[-1]

        # 最小的被 pop 出去了且下面又有值怎辦
        if self.min_stack[-1] == last:
            self.min_stack.pop()

        self.stack.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()