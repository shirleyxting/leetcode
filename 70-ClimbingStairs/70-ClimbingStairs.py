# Last updated: 8/16/2026, 9:52:54 PM
class Solution:
    # 递归→memoization→迭代→滚动变量
    # Recursion → Memoization → Iteration → Rolling Variable

    # 1. recursion
    # def climbStairs(self, n: int) -> int:
    #     if n <= 2:
    #         return n
    #     return self.climbStairs(n-1) + self.climbStairs(n-2)

    # 2. Memoization
    # def climbStairs(self, n: int) -> int:
    #     def helper(n: int, memo: dict) -> int:
    #         if n <= 2:
    #             return n
    #         if n in memo:
    #             return memo[n]
    #         memo[n] = helper(n-1, memo) + helper(n-2, memo)
    #         return memo[n]
        
    #     return helper(n, {})

    # # 3. iteration
    # def climbStairs(self, n: int) -> int:
    #     if n <= 2:
    #         return n
    #     dp = [0] * (n + 1)
    #     dp[1], dp[2] = 1, 2

    #     for i in range(3, n + 1):
    #         dp[i] = dp[i-1] + dp[i-2]
        
    #     return dp[n]

    # 4. rolling variable
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev2, prev1 = 1, 2  # dp[1], dp[2]

        for i in range(3, n+1):
            curr = prev2 + prev1
            prev2, prev1 = prev1, curr
        
        return prev1