# Last updated: 8/31/2026, 10:31:16 PM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        # O(nlogn)
4        # for each x, wrost case, has logx '1's -< logn
5        res = [0] * (n + 1)
6
7        for i in range(n + 1):
8            x = i
9            while x != 0:
10                x &= x - 1
11                res[i] += 1
12        
13        return res
14             