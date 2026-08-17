# Last updated: 8/16/2026, 9:50:28 PM
class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # DFS (try every coin, recurse) would find the right answer but
    #     # recomputes the same remaining amounts many times (overlapping
    #     # subproblems) -> use DP (bottom-up) to compute each amount once
    #     # dp[i] = fewest coins to make amount i
    #     #       = min(dp[i - c] + 1) over every coin c <= i
    #     # Time: O(amount * len(coins))   Space: O(amount)

    #     dp = [math.inf] * (amount + 1)
    #     dp[0] = 0  # base case: 0 coins needed to make amount 0

    #     for i in range(amount + 1):
    #         for c in coins:
    #             if i >= c:
    #                 # take coin c now (+1), plus however many coins
    #                 # were needed for the remaining amount (i - c)
    #                 dp[i] = min(dp[i - c] + 1, dp[i])

    #     # still inf => no combination of coins can make up amount
    #     if dp[amount] == math.inf:
    #         return -1
    #     return dp[amount]

    # DFS, recursion
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        
        def dfs(dp: List[int], curr: int) -> int:
            # dfs exit
            if curr == 0:
                return 0
            if curr < 0:
                return -1
            
            # to avoid overlapping calculations
            if dp[curr] != math.inf:
                return dp[curr]
            
            for c in coins:
                temp = dfs(dp, curr - c)
                if temp != -1:
                    dp[curr] = min(dp[curr], temp + 1)

            if dp[curr] == math.inf:
                dp[curr] = -1

            return dp[curr]

        return dfs(dp, amount)

        


            
        