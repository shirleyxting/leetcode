// Last updated: 8/16/2026, 9:51:28 PM
class Solution {
    public int numIslands(char[][] grid) {
        // BFS, county #of trees, each node can have up to 4 neighbors
        if (grid.length == 0) return 0;

        int res = 0;
        int m = grid.length, n = grid[0].length;
        int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // for visited node, mark them as value '2'
        for (int i = 0; i < m; i ++) {
            for (int j = 0; j < n; j ++) {
                // skip if visited before, skip if its 0
                if (grid[i][j] == '0' || grid[i][j] == '2') continue;

                Queue<int[]> queue = new LinkedList<>();
                queue.offer(new int[]{i, j});

                while (!queue.isEmpty()) {
                    int[] curr = queue.poll();

                    // iterate 4 possible neighbors
                    for (int[] dir: dirs) {
                        int dx = curr[0] + dir[0];
                        int dy = curr[1] + dir[1];
                        if (dx < 0 || dx >= m || dy < 0 || dy >= n) continue;
                        if (grid[dx][dy] != '1') continue;
                        
                        queue.offer(new int[]{dx, dy});
                        grid[dx][dy] = '0'; // mark as visited (drown the island)
                    }
                    // System.out.println(Arrays.deepToString(grid));
                }
                // finish BFS of a tree
                res ++;
            }
        }
        return res;
    }

    // DFS - drown each island one by one
    // private int m, n;
    // public int numIslands(char[][] grid) {
    //     m = grid.length;
    //     n = grid[0].length;
    //     int res = 0;
    //     for (int i = 0; i < m; i ++) {
    //         for (int j = 0; j < n; j ++) {
    //             if (grid[i][j] == '0') continue;
    //             dfs(grid, i, j);
    //             // finish dfs of a tree
    //             res ++;
    //         }
    //     }
    //     return res;
    // }

    // // mark as visited (set from 1 to 0), until 4 possible neighbors are all 0
    // private void dfs(char[][] grid, int i, int j) {
    //     if (i < 0 || i >= m || j < 0 || j >= n) return;
    //     if (grid[i][j] == '0') return;

    //     // mark curr node as visited
    //     grid[i][j] = '0';

    //     // iterate 4 possible neighbors
    //     dfs(grid, i, j + 1);
    //     dfs(grid, i, j - 1);
    //     dfs(grid, i + 1, j);
    //     dfs(grid, i - 1, j);
    // }

}