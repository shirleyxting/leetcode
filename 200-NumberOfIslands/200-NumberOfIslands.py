# Last updated: 8/16/2026, 9:51:24 PM
class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     # DFS
    #     if not grid:
    #         return 0
    #     m, n = len(grid), len(grid[0])
    #     count = 0

    #     def dfs(i: int, j: int):
    #         # recursion exit
    #         if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
    #             return
            
    #         # mark as visited
    #         grid[i][j] = "0"
    #         dfs(i+1, j)
    #         dfs(i-1, j)
    #         dfs(i, j +1)
    #         dfs(i, j -1)

    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == "1":
    #                 dfs(i, j)
    #                 count += 1
        
    #     return count

    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        from collections import deque 

        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0

        def bfs(i: int, j: int):
            queue = deque([(i, j)])
            # sink the land
            grid[i][j] = "0"

            while queue:
                r, c = queue.popleft()
                # check neighbors
                for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    n_r = r + dr
                    n_c = c + dc
                    if 0 <= n_r < m and 0 <= n_c < n and grid[n_r][n_c] == "1":
                        # before pushing to the queue, mark as visited, to avoid duplicates in queue
                        grid[n_r][n_c] = "0"
                        queue.append((n_r, n_c))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        
        return count