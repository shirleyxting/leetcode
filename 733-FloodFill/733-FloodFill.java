// Last updated: 8/16/2026, 9:49:36 PM
class Solution {
    // public int[][] floodFill(int[][] image, int sr, int sc, int color) {
    //     // connected components -> BFS
    //     if(image[sr][sc] == color) return image; // no color change required

    //     int m = image.length, n = image[0].length;
    //     int[][] res = image;
    //     int[][] directions = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    //     int oldColor = image[sr][sc], newColor = color;

    //     Queue<int[]> queue = new LinkedList<int[]>();
    //     queue.offer(new int[]{sr, sc});
        
    //     while(!queue.isEmpty()) {
    //         int[] curr = queue.poll();
    //         res[curr[0]][curr[1]] = newColor;

    //         // iterate 4 directions
    //         for(int[] dir: directions) {
    //             int row = curr[0] + dir[0];
    //             int col = curr[1] + dir[1];
    //             // if [row, col] is valid (within matrix and value = oldColor)
    //             if(row >= 0 && row <= m-1 && col >= 0 && col <= n-1
    //                 && image[row][col] == oldColor) {
    //                     queue.offer(new int[]{row, col});
    //                 }
    //         }
    //     } 
    //     return res;
    // }

    // DFS recursion - faster than BFS
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int oldColor = image[sr][sc];
        if (oldColor == newColor) return image;
        
        int[][] res = image;
        dfs(sr, sc, image, res, oldColor, newColor);
        return res;
    }

    private void dfs(int row, int col, int[][] image, int[][] res, int oldColor, int newColor) {
        int m = image.length, n = image[0].length;
        if(row >= 0 && row <= m-1 && col >=0 && col <= n-1 
            && image[row][col] == oldColor) {
            res[row][col] = newColor;
            dfs(row - 1, col, image, res, oldColor, newColor);
            dfs(row, col - 1, image, res, oldColor, newColor);
            dfs(row + 1, col, image, res, oldColor, newColor);
            dfs(row, col + 1, image, res, oldColor, newColor);
        }

    }
}