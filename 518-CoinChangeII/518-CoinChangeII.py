# Last updated: 8/21/2026, 2:20:49 PM
1class Solution:
2    def change(self, amount: int, coins: List[int]) -> int:
3        # dp[i][j]: for coins[:i], the cnt of ways to reach sum=j
4        #        = dp[i-1][j] + dp[i][j-coins[i]]
5        # convert to 1D: dp[j], dp[j-coin]
6        # iterate j ASC in [coin, amount]
7
8        dp = [0] * (amount + 1)
9        dp[0] = 1 # dp[0][0], dp[1][0], dp[2][0] ... always=1, as do not pick any coin will get sum=0
10
11        for coin in coins:
12            for j in range(coin, amount + 1):
13                dp[j] = dp[j] + dp[j - coin]
14        
15        return dp[amount]