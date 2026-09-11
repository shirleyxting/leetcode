# Last updated: 9/10/2026, 5:57:31 PM
1class Solution:
2    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
3        # dijkstra, max-heap, d[tgt] = prob * d[src]
4
5        # build non-directed graph, u -> list of (v, prob)
6        g = [[] for _ in range(n)]
7
8        for (u, v), prob in zip(edges, succProb):
9            g[u].append((v, prob))
10            g[v].append((u, prob))
11        
12        best = [0.0] * n
13        best[start_node] = 1.0
14
15        heap = [(-1.0, start_node)] # for now, reach node's max prob
16
17        while heap:
18            neg_p, u = heapq.heappop(heap)
19            p = -neg_p
20
21            if u == end_node:
22                return p
23            
24            if p < best[u]: # p is worse than best[u] (curr best max prb to reach u) -> expired record
25                continue
26            
27            for v, w in g[u]:
28                new_p = p * w
29                if new_p > best[v]:
30                    best[v] = new_p
31                    heapq.heappush(heap, (-new_p, v))
32        
33        return 0.0
34        
35
36