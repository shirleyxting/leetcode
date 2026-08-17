// Last updated: 8/16/2026, 9:50:08 PM
class Solution {
    // public int[][] updateMatrix(int[][] mat) {
    //     /* BFS: 0 is layer-0, 1 near 0 is layer-1, the 1 near 'layer-1' is layer-2, etc...*/
    //     int m = mat.length, n = mat[0].length; 
    //     int[][] res = new int[m][n];
        
    //     Queue<int[]> queue = new LinkedList<>();
        
    //     // add all 0s to queue (layer-0)
    //     for(int i = 0; i < m; i ++) {
    //         for(int j = 0; j < n; j ++) {
    //             if(mat[i][j] == 0) {
    //                 queue.offer(new int[]{i, j});
    //                 res[i][j] = 0;
    //             } else {
    //                 res[i][j] = -1; // -1 means not visited
    //             }
    //         }
    //     }
        
    //     int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
    //     while( !queue.isEmpty() ) {
    //         int[] curr = queue.poll();
    //         int x = curr[0], y = curr[1];

    //         // check left, right, top, down neighbors of current layer nodes
    //         for(int[] dir: dirs) {
    //             int dx = x + dir[0], dy = y + dir[1];
    //             // check if [i,j] is legitible and not visited before
    //             if(dx < 0 || dx >= m || dy < 0 || dy >= n || res[dx][dy] != -1) continue;
    //             res[dx][dy] = res[x][y] + 1;
    //             queue.offer(new int[]{dx, dy});
    //         }
    //     }
    //     return res;
    // }

    // method 2 - DP
    /** DP: we can only use previous value if they are computed.
    however, the min-dist to 0-cell = MIN(4 neighbors min-dist to 0) + 1;
    we cannot get 4 neighbors value simutaneously
    - 1.top-down, to compute the dist for left and top directions
    - 2.botton-up,                        right and down
     */
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int maxDist = m + n;
        int[][] dp = new int[m][n];

        // step-1 top-down
        for(int i = 0; i < m; i ++) {
            for(int j = 0; j < n; j ++) {
                if(mat[i][j] == 0) {
                    dp[i][j] = 0;
                } else {
                    int top = maxDist, left = maxDist;
                    if(i - 1 >= 0) top = dp[i-1][j];
                    if(j - 1 >= 0) left = dp[i][j-1];
                    dp[i][j] = Math.min(top, left) + 1;
                }
            }
        }

        // step-2 bottom-up
        for(int i = m-1; i >= 0; i --) {
            for(int j = n-1; j >= 0; j --) {
                if(mat[i][j] == 0) {
                    dp[i][j] = 0;
                } else {
                    int down = maxDist, right = maxDist;
                    if(i + 1 < m) down = dp[i+1][j];
                    if(j + 1 < n) right = dp[i][j+1];
                    dp[i][j] = Math.min(Math.min(down, right) + 1, dp[i][j]);
                }
            }
        }
        return dp;
    }
}