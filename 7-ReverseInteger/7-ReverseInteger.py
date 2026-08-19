# Last updated: 8/18/2026, 9:47:44 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3        INT_MIN = -2**31
4        INT_MAX = 2**31 - 1
5
6        sign = -1 if x < 0 else 1
7        x = abs(x)
8        
9        res = 0
10        while x > 0:
11            digit = x % 10
12            x //= 10
13            res = res * 10 + digit
14        
15        res = res * sign
16
17        if res < INT_MIN or res > INT_MAX:
18            return 0
19        
20        return res