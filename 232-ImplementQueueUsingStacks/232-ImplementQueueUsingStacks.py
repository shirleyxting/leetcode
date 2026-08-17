# Last updated: 8/16/2026, 9:51:01 PM
class MyQueue:

    def __init__(self):
        self.s1 = deque() # queue
        self.s2 = deque() # used for "push"

    def push(self, x: int) -> None:
        # s1 = 1 2 3
        # we want s1 = 1 2 3 4
        # push all items in s1 to s2, so s2 = 3 2 1, s1 = [], push 4 to s2, s2 = 4 3 2 1
        # push all items in s2 to s1, so s1 = 1 2 3 4, s2 = []
        while self.s1:
            self.s2.append(self.s1.pop())
        
        self.s2.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not bool(self.s1)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()