# Last updated: 9/10/2026, 5:28:46 PM
1class Solution:
2    def minCostConnectPoints(self, points: List[List[int]]) -> int:
3        # greedy, eveytime pull the nearest point
4
5        n = len(points)
6        if n <= 1:
7            return 0
8
9        total = count = 0
10        visited = [False] * n
11        # minheap, (cost, point_idx)
12        heap = [(0,0)]  
13
14        while count < n:
15            cost, i = heapq.heappop(heap)
16
17            if visited[i]:      # skip expired records
18                continue
19            
20            # add to connected tree
21            visited[i] = True
22            count += 1
23            total += cost
24
25            # add remaining points (connecting to 'i') to heap
26            xi, yi = points[i]
27            for j in range(n):
28                if not visited[j]:
29                    xj, yj = points[j]
30                    heapq.heappush(heap, (abs(xj-xi) + abs(yj-yi), j))
31        
32        return total
33