# Last updated: 8/16/2026, 9:48:59 PM
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi-source BFS: level traversal

        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # s-1: enqueue all rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        time = 0

        # fresh > 0 is required, otherwise, we will traverse one more round, and needs return time-1
        # also when no fresh oranges left, thats the right moment we need to calcualte the time
        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2 # mark as visited during enqueue
                        fresh -= 1
                        q.append((x, y))
            # print(q)
            time += 1
        
        return time if fresh == 0 else -1