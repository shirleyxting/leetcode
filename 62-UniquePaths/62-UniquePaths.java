// Last updated: 8/16/2026, 9:53:03 PM
class Solution {
    public int uniquePaths(int m, int n) {
        // DP: dp[i][j]: # of possible paths from [0,0] to [i,j]
        // dp[i][j] = dp[i-1][j] + down
        //       or = dp[i][j-1] + right
        // dp[i][j] = dp[i-1][j] + dp[i][j-1]

        // edge case:
        if (m == 1 && n == 1) return 1;

        int[][] dp = new int[m][n];
        dp[0][0] = 0;
        for(int i = 1; i < m; i ++) dp[i][0] = 1;
        for(int j = 1; j < n; j ++) dp[0][j] = 1;

        for(int i = 1; i < m; i ++) {
            for(int j = 1; j < n; j ++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
                //System.out.println(dp[i][j]);
            }
        }
        return dp[m-1][n-1];
    }
}