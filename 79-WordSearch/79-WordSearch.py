# Last updated: 8/23/2026, 4:50:22 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        m, n = len(board), len(board[0])
4
5        # start from board[i][j], if can find word[idx:]
6        def backtrack(i: int, j: int, idx: int) -> bool:
7            # exit: if already checks all char in words
8            if idx == len(word):
9                return True
10            
11            # border check & word[idx] check
12            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx]:
13                return False
14            
15            # select current node
16            temp = board[i][j]
17            board[i][j] = "#"   # placeholder
18
19            # iterate 4 dirs for word[idx+1]
20            found = False
21            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
22                found |= backtrack(i + dr, j + dc, idx + 1)
23            
24            # cancel selection
25            board[i][j] = temp
26
27            return found
28        
29        # iterate all possible start points
30        for i in range(m):
31            for j in range(n):
32                if backtrack(i, j, 0):
33                    return True
34        return False
35        