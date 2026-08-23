# Last updated: 8/23/2026, 4:53:10 PM
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
22                # found |= backtrack(i + dr, j + dc, idx + 1)   # slow, break immedaitely when found it
23                if backtrack(i + dr, j + dc, idx + 1):
24                    found = True
25                    break
26            
27            # cancel selection
28            board[i][j] = temp
29
30            return found
31        
32        # iterate all possible start points
33        for i in range(m):
34            for j in range(n):
35                if backtrack(i, j, 0):
36                    return True
37        return False
38        