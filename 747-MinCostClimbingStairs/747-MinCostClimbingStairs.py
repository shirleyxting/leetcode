# Last updated: 8/16/2026, 9:49:19 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # optimal substructure + overlapping subproblems -> DP
        # dp[i] = min cost to REACH step i (stand on it, before paying to leave it). 
        # You can reach i from i-1 (pay cost[i-1]) or from i-2 (pay cost[i-2]):
        # dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        n = len(cost)
        # free to start at step 0 or 1
        dp = [-1] * (n + 1)

        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]+cost[i-2])
        
        return dp[n]