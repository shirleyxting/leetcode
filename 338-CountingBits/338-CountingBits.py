# Last updated: 8/31/2026, 10:34:23 PM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        # # O(nlogn)
4        # # for each x, wrost case, has logx '1's -< logn
5        # res = [0] * (n + 1)
6
7        # for i in range(n + 1):
8        #     x = i
9        #     while x != 0:
10        #         x &= x - 1
11        #         res[i] += 1
12        
13        # return res
14
15        # O(n)
16        # DP: dp[i] = dp[i >> 1] + i's last digit (0 or 1)
17        # get the last digit of x => x & 1
18        # dp[i] = dp[ i >> 1] + (i & 1)
19
20        dp = [0] * (n + 1)
21        
22        for i in range(1, n + 1):
23            dp[i] = dp[i >> 1] + (i & 1)
24        
25        return dp
26
27             