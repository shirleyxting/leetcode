// Last updated: 8/16/2026, 9:50:33 PM
class Solution {
    // public int coinChange(int[] coins, int amount) {
    //     // DP
    //     // dp[n] = min(dp[n - coins_i]) + 1, if the min=-1 return -1
    //     return helper(coins, amount, new int[amount + 1]);
    // }

    // private int helper(int[] coins, int amount, int[] dp) {
    //     if(amount == 0) return 0;
    //     if(amount < 0) return -1;
    //     // if the amount is calculated before
    //     if(dp[amount] != 0) return dp[amount];
        
    //     int minCnt = Integer.MAX_VALUE;
    //     for(int coin: coins) {
    //         int temp = helper(coins, amount - coin, dp);
    //         // only update minCnt if temp != -1
    //         if (temp > -1) minCnt = Math.min(minCnt, temp);
    //     }
    //     if (minCnt == Integer.MAX_VALUE) {
    //         dp[amount] = -1;
    //     } else {
    //         dp[amount] = minCnt + 1;
    //     }
    //     return dp[amount];
    // }

    // method 2 - iterative version
    // time: O(amount * len(coins))
    // space: O(amount)
    public int coinChange(int[] coins, int amount) {
        // dp[amt] = the smallest coinCnt to achieve 'amt'
        int[] dp = new int[amount + 1];
        // initilize dp with max value, the coinCount could not exceed amount, so set initial value to 'amount+1'
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int i = 1; i < amount + 1; i ++) {
            for (int coin: coins) {
                if (i - coin >= 0) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        if (dp[amount] == amount + 1) return -1;
        return dp[amount];
    }
}