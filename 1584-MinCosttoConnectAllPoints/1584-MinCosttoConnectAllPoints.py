# Last updated: 9/10/2026, 5:39:00 PM
1class Solution:
2    def minCostConnectPoints(self, points: List[List[int]]) -> int:
3        # # greedy, eveytime pull the nearest point
4
5        # n = len(points)
6        # if n <= 1:
7        #     return 0
8
9        # total = count = 0
10        # visited = [False] * n
11        # # minheap, (cost, point_idx)
12        # heap = [(0,0)]  
13
14        # while count < n:
15        #     cost, i = heapq.heappop(heap)
16
17        #     if visited[i]:      # skip expired records
18        #         continue
19            
20        #     # add to connected tree
21        #     visited[i] = True
22        #     count += 1
23        #     total += cost
24
25        #     # add remaining points (connecting to 'i') to heap
26        #     xi, yi = points[i]
27        #     for j in range(n):
28        #         if not visited[j]:
29        #             xj, yj = points[j]
30        #             heapq.heappush(heap, (abs(xj-xi) + abs(yj-yi), j))
31        
32        # return total
33
34
35        # DSU, union find
36        n = len(points)
37        if n <= 1: return 0
38
39        parent = list(range(n))
40
41        def find(x):
42            while x != parent[x]:
43                parent[x] = parent[parent[x]]  #path halving
44                x = parent[x]
45            return x
46        
47        def union(x, y):
48            rx, ry = find(x), find(y)
49            if rx == ry:
50                return False    # cycle found
51            parent[ry] = rx
52            return True
53        
54        # build all edges: (cost, i, j) (i,j are index)
55        edges = []
56        for i in range(n):
57            for j in range(i+1, n):
58                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
59                edges.append((w, i, j))
60        
61        edges.sort()
62        # greedy to pick min every time
63
64        total = used = 0
65        for w, i, j in edges:
66            if union(i, j):
67                # only pick edge when not cycle
68                total += w
69                used += 1
70            
71                if used == n-1:     # n-1 edges to make a tree
72                    break
73        
74        return total