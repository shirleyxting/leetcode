# Last updated: 8/21/2026, 8:53:21 PM
1class Solution:
2    def combinationSum4(self, nums: List[int], target: int) -> int:
3        # order counts in results
4        # dp[j]: for entire nums, how many combinations with any order, satifying sum = j
5        # dp[j] = sum(dp[j - num] for num in nums)
6        # for current target-j, we can pick any num in nums, n1, n2, n3, ...
7
8        n = len(nums)
9        dp = [0] * (target + 1)
10        dp[0] = 1   # empty set can satify sum = 0
11
12        for j in range(1, target + 1):
13            dp[j] = sum(dp[j - num] for num in nums if j - num >= 0)
14
15        return dp[target]