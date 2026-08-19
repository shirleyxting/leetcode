# Last updated: 8/18/2026, 9:30:43 PM
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        # brute force: O(n)
4        # f(n) = f(n/2) + O(1) [handle even] ==> O(n) -> O(logn)
5        # how to convert f(n) to f(n/2)
6        # x^n = (x^(n/2))^2
7
8        if n < 0:
9            x = 1/x
10            n = -n
11        
12        def helper(x: float, n:int) -> float:
13            if n == 0:
14                return 1
15
16            half = helper(x, n//2)
17
18            if n % 2 == 1:
19                return half * half * x
20            else:
21                return half * half
22
23        return helper(x, n)
24