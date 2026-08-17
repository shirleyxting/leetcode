// Last updated: 8/16/2026, 9:49:03 PM
class Solution {
    public int orangesRotting(int[][] grid) {
        // BFS
        if (grid.length == 0) return 0;

        int m = grid.length, n = grid[0].length;
        int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int res = 0;

        int cntFresh = 0;
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < m; i ++) {
            for (int j = 0; j < n; j ++) {
                if (grid[i][j] == 1) cntFresh ++;
                // add all rotten to queue, rotten also means visited mark
                if (grid[i][j] == 2) queue.offer(new int[]{i, j});
            }
        }

        if (cntFresh == 0) return 0;

        // BFS starts from initially rotten oranges
        while (!queue.isEmpty()) {
            int qSize = queue.size();
            // System.out.println(queue.size());
            for (int p = 0; p < qSize; p ++) {
                int[] curr = queue.poll();
                // System.out.println(Arrays.toString(curr));
                int status = grid[curr[0]][curr[1]];
                
                for (int[] dir: dirs) {
                    int dx = curr[0] + dir[0];
                    int dy = curr[1] + dir[1];
                    if (dx < 0 || dx >= m || dy < 0 || dy >= n) continue;
                    if (grid[dx][dy] != 1) continue;
                    queue.offer(new int[]{dx, dy});
                    grid[dx][dy] = 2; // 2 means visited/rotten
                    cntFresh --; // update current fresh count
                }             
            }
            res++;
        }
        // System.out.println(Arrays.deepToString(grid));
        return (cntFresh == 0) ? res - 1 : -1;
    }
}