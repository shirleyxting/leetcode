// Last updated: 8/16/2026, 9:52:06 PM
class Solution {
    // brute force - TLE
    // public boolean wordBreak(String s, List<String> wordDict) {
    //     Set<String> set = new HashSet<>(wordDict);;
    //     return helper(s, set);
    // }

    // // if s can be successfuly word break by 'set'
    // private boolean helper(String s, Set<String> set) {
    //     int n = s.length();
    //     if (n == 0) return true;
    //     for (int i = 1; i <= n; i ++) {
    //         if (set.contains(s.substring(0, i)) && helper(s.substring(i), set))
    //             return true;
    //     }
    //     return false;
    // }

    // Method 2 - DP
    // for s, iterate i, if find any word 'w', 
    // wordBreak(s) = wordBreak(s - 'w') (since 'w' is already find)
    // add MEMO
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        boolean[] dp = new boolean[n+1];
        // init
        dp[0] = true;

        for(int i = 1; i <= n; i ++) {
            for(String w: wordDict) {
                int wLen = w.length();
                if (i - wLen >= 0 && s.substring(i - wLen, i).equals(w)) {
                    dp[i] = dp[i - wLen];
                }
                if (dp[i]) break;
            }
        }
        return dp[n];
    }



}