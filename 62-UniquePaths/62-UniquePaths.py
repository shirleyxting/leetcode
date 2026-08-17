# Last updated: 8/16/2026, 9:52:59 PM
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # dp[i,j] = dp[i-1,j] + dp[i,j-1]
        # dp = [[0] * n for _ in range(m)]

        # for r in range(m):
        #     dp[r][0] = 1
        # for c in range(n):
        #     dp[0][c] = 1
        
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # return dp[m-1][n-1]

        # only 2 items are needed, convert 2-dim to 1-dim
        # dp[j] = dp[j] (not computed yet, still shows prev row value, dp[i-1][j]) + dp[j-1]
        # dp[j]: for CURR ROW, dp[j]

        # init: for row-0, dp[j] values = 1
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]
        
        return dp[n-1]
