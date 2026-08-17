# Last updated: 8/16/2026, 9:51:54 PM
class MinStack:
    # main a shadow stack, saves the current min
    # when stack pops, shadow_stack pops
    # when stacj pushs a new val, shadow_stack push curr min
    def __init__(self):
        self.stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        new_min = value if not self.min_stack else min(value, self.min_stack[-1])
        self.min_stack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()