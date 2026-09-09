# Last updated: 9/8/2026, 10:11:59 PM
1# class MinStack:
2#     # maintain a shadow stack, saves the current min
3#     # when stack pops, shadow_stack pops
4#     # when stacj pushs a new val, shadow_stack push curr min
5#     def __init__(self):
6#         self.stack: list[int] = []
7#         self.min_stack: list[int] = []
8
9#     def push(self, value: int) -> None:
10#         self.stack.append(value)
11#         new_min = value if not self.min_stack else min(value, self.min_stack[-1])
12#         self.min_stack.append(new_min)
13
14#     def pop(self) -> None:
15#         self.stack.pop()
16#         self.min_stack.pop()
17
18#     def top(self) -> int:
19#         return self.stack[-1]
20        
21
22#     def getMin(self) -> int:
23#         return self.min_stack[-1]
24
25
26class MinStack:
27    # tuple (val, curr_min) as stack element
28
29    def __init__(self):
30        self.stack: list[tuple[int, int]] = []
31
32    def push(self, value: int) -> None:
33        if not self.stack:
34            curr_min = value
35        else:
36            curr_min = min(value, self.stack[-1][1])
37        
38        self.stack.append((value, curr_min))
39
40    def pop(self) -> None:
41        self.stack.pop()
42
43    def top(self) -> int:
44        return self.stack[-1][0]
45        
46
47    def getMin(self) -> int:
48        return self.stack[-1][1]
49
50# Your MinStack object will be instantiated and called as such:
51# obj = MinStack()
52# obj.push(value)
53# obj.pop()
54# param_3 = obj.top()
55# param_4 = obj.getMin()