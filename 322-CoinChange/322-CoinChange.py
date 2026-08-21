# Last updated: 8/21/2026, 2:00:28 PM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        # knapsack complete, item can be selected multiple times
4        # dp[i][j]: for coins[:i], the min item combination, with sum = j
5        #         = min(dp[i-1][j], dp[i][j-coins[i]] + 1)  (not use coin-i, use coin-i multiple times)
6        # dp[i][j] only replies on dp[i-1] -> 2D to 1D
7        #  dp[j], dp[j-coin]
8        #  iterate j ASC in [coin, amount]
9        #  ASC ensures when process dp[j], dp[j-coin] is already computed with curr row
10        #   -> dp[i][j] = dp[i][j-coin]
11
12        dp = [float('inf')] * (amount + 1)
13        dp[0] = 0  # dp[0][0], dp[1][0], dp[2][0], .. always = 0, do not pick any coin -> will reach sum=0
14
15        for coin in coins:
16            for j in range(coin, amount + 1):
17                dp[j] = min(dp[j], dp[j - coin] + 1)
18        
19        return dp[amount] if dp[amount] != float('inf') else -1