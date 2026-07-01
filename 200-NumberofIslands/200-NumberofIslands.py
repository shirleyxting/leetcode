# Last updated: 7/1/2026, 4:48:39 PM
1class Solution:
2    # def numIslands(self, grid: List[List[str]]) -> int:
3    #     # BFS
4    #     # visited set to -1, when to stop traverse? when all values in grid = -1
5    #     if not grid: return 0
6        
7    #     res = 0
8    #     while len(self.findFirstOne(grid)) != 0:
9    #         i, j = self.findFirstOne(grid)
10    #         # print(i, j)
11    #         self.expandIsland(grid, i, j)
12    #         # print(grid)
13    #         res += 1
14    #     return res
15
16    
17    # def findFirstOne(self, grid: List[List[int]]) -> List[int]:
18    #     m, n = len(grid), len(grid[0])
19    #     for i in range(m):
20    #         for j in range(n):
21    #             if grid[i][j] == "1":
22    #                 return [i, j]
23    #     return []
24
25
26    # def expandIsland(self, grid: List[List[int]], i: int, j: int):
27    #     dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
28    #     m, n = len(grid), len(grid[0])
29        
30    #     queue = deque()
31    #     queue.append([i, j])
32    #     while queue:
33    #         i, j = queue.popleft()
34    #         # mark as visited
35    #         grid[i][j] = -1
36    #         for d in dirs:
37    #             ii = i + d[0]
38    #             jj = j + d[1]
39    #             if ii < m and ii >= 0 and jj < n and jj >= 0 and grid[ii][jj] == "1":
40    #                 queue.append([ii, jj])
41
42
43    # above codes has lots of issues
44    def numIslands(self, grid: List[List[int]]) -> int:
45        res = 0
46        m, n = len(grid), len(grid[0])
47
48        for i in range(m):
49            for j in range(n):
50                if grid[i][j] == "1":
51                    # expand island starting at [i, j] and mark visited nodes as "-1"
52                    self.expand(grid, i, j)
53                    res += 1
54        
55        return res
56    
57    def expand(self, grid: List[List[int]], i: int, j: int):
58        queue = deque()
59        queue.append([i, j])
60
61        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
62        m, n = len(grid), len(grid[0])
63        while queue:
64            i, j = queue.popleft()
65            # check neighbors
66            for d in dirs:
67                p = i + d[0]
68                q = j + d[1]
69                if p >= 0 and p < m and q >= 0 and q < n and grid[p][q] == "1":
70                    queue.append([p, q])
71                    # mark as visited when pushing to queue, to avoid overlapping
72                    grid[p][q] = "-1"
73
74        
75            
76
77            
78
79        
80