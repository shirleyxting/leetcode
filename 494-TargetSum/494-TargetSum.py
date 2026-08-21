# Last updated: 8/21/2026, 1:39:56 PM
1class Solution:
2    def findTargetSumWays(self, nums: List[int], target: int) -> int:
3        # Positive sum: P, Negative sum: N
4        # P + N = total, P - N = target
5        # 2P = total + target -> P = (total + target)/2
6
7        total = sum(nums)
8        # nums is positive, so P must > 0 and be int
9        if (total + target) % 2 == 1 or (total + target) < 0:
10            return 0
11
12        P = (total + target) // 2
13        # find subset sum = P
14        # dp[i][j]: for nums[:i], how many subsets can reach sum = j
15        #         = dp[i-1][j] --not pick num-i + dp[i-1][j-nums[i]] ---pick num-i
16        #         only relies on dp[i-1], convert 2D to 1D
17        #  dp[j], dp[j - num]
18        #  iterate j DESC in [num, P]
19        #  DESC: ensure dp[j-num] is still from prev row, when process dp[i]
20
21        dp = [0] * (P + 1)
22
23        dp[0] = 1 # for dp[0][0], dp[1][0], dp[2][0], ...: empty set can always satisfy sum=0, so its 0
24
25        for num in nums:
26            for j in range(P, num-1, -1):
27                dp[j] = dp[j] + dp[j - num]
28
29        return dp[P]