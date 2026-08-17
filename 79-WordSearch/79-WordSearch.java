// Last updated: 8/16/2026, 9:52:45 PM
class Solution {
    private int m, n, l;
    private HashSet<List<Integer>> path = new HashSet<>();
    public boolean exist(char[][] board, String word) {
        m = board.length;
        n = board[0].length;
        l = word.length();
        
        for(int r = 0; r < m; r ++) {
            for(int c = 0; c < n; c ++) {
                if(dfs(r, c, 0, board, word)) return true;
            }
        }
        return false;
    }

    // starting from board(r,c), if word[i:] can be found
    private boolean dfs(int r, int c, int i, char[][] board, String word) {
        if (i == l) return true; // finish exploring, word[i:] is already found.
        if ((r < 0 || r >= m || c < 0 || c >= n) ||
            (board[r][c] != word.charAt(i)) ||
            (path.contains(List.of(r, c))) // already in current path
        ) return false;

        // now, we found the char we want, add it to path
        path.add(List.of(r, c));
        // check if next char (i+1) can be found
        boolean res = dfs(r+1, c, i+1, board, word) ||
            dfs(r-1, c, i+1, board, word) ||
            dfs(r, c+1, i+1, board, word) ||
            dfs(r, c-1, i+1, board, word);
        // finish exploring (r, c), remove from curr path
        path.remove(List.of(r, c));

        return res;
    }

}