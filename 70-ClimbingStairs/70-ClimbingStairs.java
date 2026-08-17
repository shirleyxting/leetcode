// Last updated: 8/16/2026, 9:52:58 PM
class Solution {
    public int climbStairs(int n) {
        // fins all solution COUNT -> NOT DFS
        if (n == 0 || n == 1 || n == 2) return n;
        // climb(n) = climb(n-1) + 1 step
        //          = climb(n-2) + 2 steps
        // count(n) = count(n-1) + count(n-2)
        // record results in int[n] to quickly fetch it, avoid re-compute
        int[] res = new int[n + 1];
        res[0] = 0;
        res[1] = 1;
        res[2] = 2;

        for(int i = 3; i <= n; i ++) {
            res[i] = res[i-1] + res[i-2];
        }

        return res[n];
    }
}

// n=5 -> f(4) + f(3) 
// = (f(3) + f(2)) + (f(2) + f(1))
// = (f(2)+f(1)) + 2 + 2 + 1
// = 2+1+2+2+1 = 8