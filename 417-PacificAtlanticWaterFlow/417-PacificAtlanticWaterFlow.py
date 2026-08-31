# Last updated: 8/30/2026, 8:43:37 PM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        # if dfs from each node -> O(mn*mn)
4        # dfs from 4 edges, find height >= curr_height
5
6        m, n = len(heights), len(heights[0])
7
8        # from [r,c], find all possible nodes, add into visited
9        def dfs(r, c, visited):
10            visited.add((r, c))
11
12            for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
13                nr, nc = r + dr, c + dc
14                # dfs only when new_h >= curr_h, and not visited before
15                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
16                    dfs(nr, nc, visited)
17        
18        pacific, atlantic = set(), set()
19
20        for i in range(m):
21            dfs(i, 0, pacific)
22            dfs(i, n-1, atlantic)
23        
24        for j in range(n):
25            dfs(0, j, pacific)
26            dfs(m-1, j, atlantic)
27        
28        res = []
29        for i in range(m):
30            for j in range(n):
31                if (i, j) in pacific and (i, j) in atlantic:
32                    res.append([i, j])
33        
34        return res
35
36
37