# Last updated: 8/16/2026, 9:49:34 PM
# 后序遍历累加模式识别 / Post-order accumulation pattern
# 如果发现"要算当前节点的答案，必须先知道子节点/相邻节点的答案"，
# 那就是后序遍历累加——写法上一定是"先递归子节点拿到返回值，
# 再用这些返回值组合出当前的返回值"。
# If computing the current node's answer requires knowing the children's
# (or neighbors') answers first, it's post-order accumulation —
# recurse into children to get their return values first,
# then combine those values into the current node's return value.

# # DFS
# # dfs[i,j] = area size of land [i,j]
# #  = 1 + (4 dirs of child dfs[,])
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         if not grid:
#             return 0

#         m, n = len(grid), len(grid[0])
#         def dfs(i: int, j: int) -> int:
#             # dfs exit
#             if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
#                 return 0

#             # mark as visited (0), sink the island
#             grid[i][j] = 0

#             # recursion of the childrens
#             return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

#         max_area = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     max_area = max(max_area, dfs(i, j))
        
#         return max_area

# BFS
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        def bfs(i:int, j:int) -> int:
            # mark as visited during enqueue, never wait until dequeue, 
            # to avoid appending same node multiple time
            grid[i][j] = 0
            area = 0
            q = deque([(i, j)])

            while q:
                r, c = q.popleft()
                # 每弹出一个陆地格子，面积+1
                area += 1
                for dr, dc in [[-1,0], [1,0], [0,1], [0,-1]]:
                    nr, nc = r + dr, c + dc
                    # DO NOT FORGET to check nr, nc eligibilty
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        # mark as visited during enqueue
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            return area

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))
        
        return max_area

