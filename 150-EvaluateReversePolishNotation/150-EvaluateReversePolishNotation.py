# Last updated: 9/16/2026, 2:55:05 PM
1class Solution:
2    def evalRPN(self, tokens: list[str]) -> int:
3        # stack to save numbers, [a, b]
4        # when meet an operator, pop twice from stack, b, a -> a operator b
5
6        stack = []
7
8        for t in tokens:
9            if t in "+-*/" :
10                b = stack.pop()
11                a = stack.pop()
12                
13                if t == "+": stack.append(a + b)
14                if t == "-": stack.append(a - b)
15                if t == "*": stack.append(a * b)
16                # int(a/b) -> pick num closing to 0, while a//b, is rounding down
17                if t == "/": stack.append(int(a / b))
18            else:
19                stack.append(int(t))
20        
21        return stack[0]
22        
23