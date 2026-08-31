# Last updated: 8/30/2026, 9:31:27 PM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        # DFS from O on 4 edges
7        # find all connected Os -> those Os will be kept
8        # not visited Os should be replaced as X
9
10        # states: O, X, # (kept in final)
11
12        m, n = len(board), len(board[0])
13
14        def dfs(r, c):
15            if board[r][c] != 'O':
16                return
17
18            board[r][c] = '#'
19
20            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
21                nr, nc = r + dr, c + dc
22                if 0 <= nr < m and 0 <= nc < n:
23                    dfs(nr, nc)
24        
25        # 1: dfs from 4 edges
26        for r in range(m):
27            dfs(r, 0)
28            dfs(r, n - 1)
29        for c in range(n):
30            dfs(0, c)
31            dfs(m - 1, c)
32        
33        # 2: scan whole board, # -> O, O -> X
34        for r in range(m):
35            for c in range(n):
36                if board[r][c] == '#':
37                    board[r][c] = 'O'
38                elif board[r][c] == 'O':
39                    board[r][c] = 'X'
40        
41        
42        